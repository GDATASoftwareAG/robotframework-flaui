param(
    [Parameter(Mandatory = $true)]
    [string]$PythonPath,
    [Parameter(Mandatory = $true)]
    [ValidateSet('x86', 'x64')]
    [string]$Platform
)

$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$version = '3.15.0rc1'
$releasePath = '3.15.0'
$urlPlatform = if ($Platform -eq 'x64') { '-amd64' } else { '' }
$downloadUrl = "https://www.python.org/ftp/python/$releasePath/python-$version$urlPlatform.exe"
$installerPath = "$env:TEMP\python-$version$urlPlatform.exe"

Write-Host "Installing Python $version $Platform to $PythonPath..."
Write-Host "Downloading $downloadUrl..."
(New-Object Net.WebClient).DownloadFile($downloadUrl, $installerPath)

Write-Host "Running installer..."
$process = Start-Process -FilePath $installerPath -ArgumentList @(
    '/quiet',
    "TargetDir=$PythonPath",
    'PrependPath=1',
    'Shortcuts=0',
    'Include_launcher=1',
    'InstallLauncherAllUsers=1'
) -Wait -PassThru
Remove-Item $installerPath

if ($process.ExitCode -ne 0) {
    throw "Python $version installer failed with exit code $($process.ExitCode)"
}

$env:PATH = "$PythonPath;$PythonPath\Scripts;$env:PATH"

& "$PythonPath\python.exe" --version

# pip PATH warnings go to stderr and would abort under ErrorActionPreference Stop.
$savedEap = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
try {
    & "$PythonPath\python.exe" -m pip install --upgrade pip
    if ($LASTEXITCODE -ne 0) {
        throw "pip upgrade failed with exit code $LASTEXITCODE"
    }
} finally {
    $ErrorActionPreference = $savedEap
}

Write-Host "Installed Python $version to $PythonPath"
