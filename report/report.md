# Group Report

In this repository aiming to output a `MapMaker.ipynb`, `my_functions.py` and related `test_functions.py` are completed by each group member individually and this `report.md` and `README.md` are completed collaboratively.

The following content shows how this repository is created:

## Pull requests and request reviews

Record of requests and reviews.

# *Dzaky*
5/5/2022
- Rename the individual folder
- Create first pull request in the group repository
- Try and learn the test functions in `test_functions.py` and `RunTests.ipynb`

11/5/2022
- Approve Jiarun's individual part PR
-
12/5/2022
- Initial work on `my_functions.py`: Write and complete the beginning functions (**my_basemap()**, **my_water_features()**, **my_coastlines()**)

16/5/2022
- Comment in Pull Request: Jiarun's table fix on README.md

17/5/2022
- Completing the remaining `my_functions.py` functions
- Write full documentation on **my_documentation()** and docstrings in the later function
- Add `MapMaker.ipynb` to the github folder

20/5/2022
- Fix some mistakes and typo thanks to the comment and review from fellow group members

22/5/2022
- Approve the report template proposed by Jiarun

## Collaborative editing of documents

Editting history for `report.md` and `README.md`.

# *Dzaky*
5/5/2022
- Initialize the group members template for README.md

22/5/2022
- Writing individual part in `report.md`

## Creating and resolving issues

Issue records in GitHub.

# *Dzaky*
19/5/2022
- Raise issues about writing report


## Adding tests

Test functions are built for each of my_functions used in the MapMaker. they aim to test if these my_fucntions run successfully and return expected variables. Below shows the `test_functions.py` and `RunTests.ipynb` of each group member.
There are two Python files for test function: `test_functions.p` and `RunTests.ipynb`. The first file (test_functions.py) is where we wrote our function code for testing, while the second file is where we execute the RunTests.ipynb by typing !pytest to check whether all or some of our test functions have passed or not

Respective tests：

### *Jiarun* 

[test_functions.py](https://github.com/ANU-RSES-Education/EMSC-4033-2022-assignment-Group2/blob/0b53a6d51077740a274aae88fdfe6543279312f5/Jiarun/tests/test_functions.py)  
[RunTests.ipynb](https://github.com/ANU-RSES-Education/EMSC-4033-2022-assignment-Group2/blob/0b53a6d51077740a274aae88fdfe6543279312f5/Jiarun/RunTests.ipynb)

### *Dzaky*

[test_functions.py](https://github.com/ANU-RSES-Education/EMSC-4033-2022-assignment-Group2/blob/5631329b203db8be90cdf5ede99960a37ba87507/Dzaky/tests/test_functions.py)
[RunTests.ipynb](https://github.com/ANU-RSES-Education/EMSC-4033-2022-assignment-Group2/blob/5631329b203db8be90cdf5ede99960a37ba87507/Dzaky/RunTests.ipynb)



## Adding documentation/docstrings

### *Jiarun*

The documentation in `MapMaker.ipynb` is output from **my_documentation()**. This documentation explains the information about each of the elements in the created map, including Basemap, Coastlines and water features, Earthquake point events and Seafloor age, and the packages and methods used to output these elements.   

Docstrings written for each function in `my_functions.py` can be shown by calling **?\<function_name\>**. These docstrings demonstrate necessary information of function returns and arguments and also some important matters needing attention. A calling example is provided under each of function docstrings as well.

### *Dzaky*
Similar with the documentation from the other group members, I wrote the main documentation for a single file under **my_documentation()**. This function is exclusively made to wrote the description of subsequent functions which were prepared to execute and run `MapMaker.ipynb`. The subsequent functions in `my_functions.py` explain the fundamental informations for map, including basemap, coastlines, and water features, as well as additional data in geophysics such as earthquake events and seafloor age. 

Aside from **my_documentation()**, each function has docstrings written in the beginning of function. These docstrings give short information of function purpose and return, to guide the reader in identifying different functions. 
