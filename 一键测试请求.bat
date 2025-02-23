:start
call miniconda3\Scripts\activate.bat
goto :run

:run
python server\src\request_test.py --test stream

pause