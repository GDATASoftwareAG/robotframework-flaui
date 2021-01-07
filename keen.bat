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
    call pip install -r requirements-dev.txt
EXIT /B %ERRORLEVEL%

:build
    call:cleanup
    call:dependency
    call python setup.py bdist_wheel
    call python libdoc.py
EXIT /B %ERRORLEVEL%

:install
    call:build
    call pip install .
EXIT /B %ERRORLEVEL%

:test
    call:install
    call:pylint
    call cd atests
    call robot -x xunit.xml --outputdir ../result .
    set /A result = %ERRORLEVEL%
    call cd ..
EXIT /B %result%

:pylint
  mkdir result
  pylint src/ > result/lint.json
  pylint-json2html -f jsonextended -o result/pylint.html < result/lint.json
EXIT /B %ERRORLEVEL%


:MAIN
IF NOT "%~1" == "" call:%1
