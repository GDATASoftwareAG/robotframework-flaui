@echo off
GOTO:MAIN

:cleanup
    rmdir  /s /q result
    rmdir  /s /q build
    rmdir  /s /q dist
    rmdir  /s /q keywords
    rmdir  /s /q robotframework_flaui.egg-info
EXIT /B 0

:dependency
    call python -m pip install --upgrade pip setuptools wheel
    call python -m pip install -r requirements-dev.txt
EXIT /B %ERRORLEVEL%

:build
    call:cleanup
    call:dependency
    call python -m build
    call python libdoc.py
EXIT /B %ERRORLEVEL%

:install
    call:build
    call python -m pip install .
EXIT /B %ERRORLEVEL%

:test_uia2
    call cd atests
    call python -m robot --name "UIA2" --variable UIA:UIA2 --outputdir ../result/uia2 .
    set /A result_uia2 = %ERRORLEVEL%
    call cd ..
EXIT /B %result_uia2%

:test_uia3
    call cd atests
    call python -m robot --name "UIA3" --variable UIA:UIA3 --outputdir ../result/uia3 .
    set /A result_uia3 = %ERRORLEVEL%
    call cd ..
EXIT /B %result_uia3%

:pylint
  mkdir result
  python -m pylint src
EXIT /B %ERRORLEVEL%

:tidy
  python -m robotidy atests --check
EXIT /B %ERRORLEVEL%

:tidy-fix
  python -m robotidy atests
EXIT /B %ERRORLEVEL%

:robocop
  python -m robocop atests --configure return_status:quality_gate:E=0:W=0:I=0
EXIT /B %ERRORLEVEL%

:test
    call:install
    set /A result = %ERRORLEVEL%
    call:robocop
    if %result%==0 set /A result = %ERRORLEVEL%
    call:pylint
    if %result%==0 set /A result = %ERRORLEVEL%
    call:tidy
    if %result%==0 set /A result = %ERRORLEVEL%
    call:test_uia2
    if %result%==0 set /A result = %ERRORLEVEL%
    call:test_uia3
    if %result%==0 set /A result = %ERRORLEVEL%
    call python -m robot.rebot --name ATests --outputdir result -x rebot_xunit.xml result/uia2/output.xml result/uia3/output.xml
    if %result%==0 set /A result = %ERRORLEVEL%
    call xcopy .\result\uia2\screenshots .\result\screenshots\
    if %result%==0 set /A result = %ERRORLEVEL%
    call xcopy .\result\uia3\screenshots .\result\screenshots\
    if %result%==0 set /A result = %ERRORLEVEL%
    call python parsly.py
    if %result%==0 set /A result = %ERRORLEVEL%
EXIT /B %result%

:MAIN
IF NOT "%~1" == "" call:%1
