# CSV Report Processing
This project changes given information to the .csv
Changes
```
from
01/21/2019,Fāryāb,919,0.67%
to
2019-01-21,AFG,919,6
```
## Installing
Be sure that you have got virtualenvironment module on computer installed. <br/>
```
pip install virtualenv
```
Firstly you need to make virtual environment
```
python3 -m venv /path/to/new/virtual/environment
```
Then clone git repository to this virtual environment path
```
$ git clone https://github.com/asplia/CSV-Report-Processing.git
```
Let's go inside venv
```
/path/to/new/virtual/environment/venv/scripts/activate.bat
```
You should now install all required files
If you are not in 
```
 /path/to/new/virtual/environment/CSV-Report-Processing
```
Go there.
Then
```
pip install -r requirements.txt
```
Good job! You can now run CSV Report Processing by running the command in command line <br/>
Remember that you need to be in this directory nad you have to run virtual environment also!
```
csv_report_processing.py
```
## Tests
To run tests you need to run
```
pytest
```

