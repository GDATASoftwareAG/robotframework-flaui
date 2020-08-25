@echo off

REM project cleanup
rmdir  /s /q result
rmdir  /s /q build
rmdir  /s /q dist
rmdir  /s /q keywords
rmdir  /s /q robotframework_flauilibrary.egg-info

REM remove files from possible previous installation
if exist "files.txt" (
  for /f "delims=" %%f in (files.txt) do (
    if exist "%%f" (
	  del "%%f"
	)
  )
)

REM create wheel file
call python -m pip install -r requirements-dev.txt
call python setup.py bdist_wheel
call python libdoc.py

REM install & test module
call pip install .
call cd atests
call python -m robot -x xunit.xml --outputdir ../result .
call cd ..
