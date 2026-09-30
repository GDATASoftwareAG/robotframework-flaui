param(
    [Parameter(Mandatory = $true)]
    [string]$PythonPath,
    [Parameter(Mandatory = $true)]
    [ValidateSet('x86', 'x64')]
    [string]$Platform,
    [Parameter(Mandatory = $true)]
    [string]$Version
)

$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# python.org installer filename (may include rc/a/b) and FTP folder, keyed by major.minor.
# Preinstalled AppVeyor versions never hit this script; add a mapping when a new CPython
# is declared in appveyor.yml before the image ships it.
$installerVersions = @{
    '3.15' = @{ Installer = '3.15.0rc2'; FtpDir = '3.15.0' }
}

$release = $installerVersions[$Version]
if (-not $release) {
    throw "No python.org installer mapping for Python $Version. Add it to ci/install_python.ps1."
}

$installerVersion = $release.Installer
$ftpDir = $release.FtpDir
$urlPlatform = if ($Platform -eq 'x64') { '-amd64' } else { '' }
$downloadUrl = "https://www.python.org/ftp/python/$ftpDir/python-$installerVersion$urlPlatform.exe"
$installerPath = "$env:TEMP\python-$installerVersion$urlPlatform.exe"

Write-Host "Installing Python $installerVersion $Platform to $PythonPath..."
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
    throw "Python $installerVersion installer failed with exit code $($process.ExitCode)"
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

Write-Host "Installed Python $installerVersion to $PythonPath"
