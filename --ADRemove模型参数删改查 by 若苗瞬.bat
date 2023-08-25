@echo off

echo *** ModelParams Viewer ***

@REM set input=""
@REM if "%1"=="" goto error
@REM set input=%1

:doing
call _internal\setenv.bat

cd _internal\model_param\
@REM "%PYTHON_EXECUTABLE%" ModelParams.py %input%
"%PYTHON_EXECUTABLE%" ModelParams.py
goto done

:error
set /p input=Please input model full name in [workspace\model] folder: 
@REM [no need a input, select them in py]
@REM if %input%=="" goto error
goto doing

:done
goto end

:end
pause
@echo.