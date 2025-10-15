Write-Host "Build failed. Uploading debug artifacts..."
$ErrorActionPreference = 'Continue'
if (Test-Path "result") {
    Write-Host "Zipping result folder..."
    Compress-Archive -Path "result" -DestinationPath "results.zip" -Force
    Push-AppveyorArtifact "results.zip" -FileName "results.zip"
}
Write-Host "Failure artifacts uploaded successfully."
