if($env:APPVEYOR_REPO_TAG -eq 'true') {
    Write-Output ("Deploying " + $env:APPVEYOR_REPO_TAG_NAME + " to PyPI...")
    python -m twine upload --skip-existing dist/*.whl
    python -m twine upload --skip-existing dist/*.tar.gz
}
else
{
    Write-Output "No tag for deployment"
}