Installing this project

1. Install python 3.11 or higher (add install dir to  the PATH)
note - restart PyCharm IDE if open

2. create new environment using venv
python -m  venv  C:\dev\python-env

3. activate environment
In windows CMD (NOT powerShell) :
>C:\dev\python-env\Scripts\activate.bat
(python-env) C:\Users\danny>
(python-env) - indicate that the "python-env" environment is active

4. check version
python --version

5. in pycharm IDE - go to settings -
project:pythonexamples -
 python interpreter -add python interpreter - select "existing" radio button -
 open dir icon and select python.exe location in virtual environment dir like - C:\dev\python-env\Scripts\python.exe

6. check libs before installing requirements- in IDE terminal
  pip list

7.installing required dependencies from requirements file
 pip install -r requirements.txt

8. check libs after installing requirements- in IDE terminal
 pip list






