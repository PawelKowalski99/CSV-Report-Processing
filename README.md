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
Firstly you need to make virtual environment
```
python3 -m venv /path/to/new/virtual/environment
```
Then clone git repository to this virtual environment path
```
$ git clone https://github.com/asplia/Web-Crawler.git
```
Let's go inside venv
```
/path/to/new/virtual/environment/venv/scripts/activate.bat
```
You should now install all required files
If you are not in 
```
 /path/to/new/virtual/environment
```
Go there.
Then
```
pip install -r /path/to/requirements.txt
```
Good job! You can now run CSV Report Processing by running the command in command line
Remember that you need to be in this directory nad you have to run virtual environment also!
```
CSV_Report_Processing.py
```
## Tests
To run tests you need to run
```
test_CSV_Report_Processing.py
```

