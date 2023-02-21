@echo off
GOTO:MAIN

:cleanup
    rmdir  /s /q result
    rmdir  /s /q build
    rmdir  /s /q dist
    rmdir  /s /q keywords
    rmdir  /s /q robotframework_flaui.egg-info
EXIT /b 0

:dependency
    call python -m pip install --upgrade pip setuptools wheel
    call pip install -r requirements-dev.txt
EXIT /B %ERRORLEVEL%

:build
    call:cleanup
    call:dependency
    call python setup.py sdist bdist_wheel
    call python libdoc.py
EXIT /B %ERRORLEVEL%

:install
    call:build
    call pip install .
EXIT /B %ERRORLEVEL%

:test_uia2
    call cd atests
    call robot --name "UIA2" --variable UIA:UIA2 --outputdir ../result/uia2 .
    call cd ..
EXIT /B %ERRORLEVEL%

:test_uia3
    call cd atests
    call robot --name "UIA3" --variable UIA:UIA3 --outputdir ../result/uia3 .
    call cd ..
EXIT /B %ERRORLEVEL%

:test
    call:install
    call:pylint
    call:test_uia2
    set /A result = %ERRORLEVEL%
    call:test_uia3
    if %result%==0 set /A result = %ERRORLEVEL%
    call rebot --name ATests --outputdir result -x rebot_xunit.xml result/uia2/output.xml result/uia3/output.xml
    call python parsly.py
EXIT /B %result%

:pylint
  mkdir result
  pylint src > result/pylint.json
  pylint-json2html result/pylint.json > result/pylint.html
EXIT /B %ERRORLEVEL%


:MAIN
IF NOT "%~1" == "" call:%1
