:start
call miniconda3\Scripts\activate.bat
goto :run

:run
python server\src\env_check.py -a

pause