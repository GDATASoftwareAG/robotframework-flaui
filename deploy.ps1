if ($env:APPVEYOR_REPO_TAG -eq 'true') {
    Write-Output ("Deploying " + $env:APPVEYOR_REPO_TAG_NAME + " to PyPI...")

    python -m pip install -r requirements-dev.txt
    if ($LASTEXITCODE -ne 0) { exit -1 }

    python -m twine upload --skip-existing dist/*.whl
    if ($LASTEXITCODE -ne 0) { exit -1 }

    python -m twine upload --skip-existing dist/*.tar.gz
    if ($LASTEXITCODE -ne 0) { exit -1 }
}
else {
    Write-Output "No tag for deployment"
}
