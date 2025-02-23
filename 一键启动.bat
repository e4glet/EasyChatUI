:start
call miniconda3\Scripts\activate.bat
goto :run

:run
python server\src\main.py -a

pause