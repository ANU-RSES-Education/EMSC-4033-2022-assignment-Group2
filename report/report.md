# Group Report

In this repository aiming to output a `MapMaker.ipynb`, `my_functions.py` and related `test_functions.py` are completed by each group member individually and this `report.md` and `README.md` are completed collaboratively.

The following content shows how this repository is created:

## Pull requests and request reviews

Record of requests and reviews.


### Dzaky

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
- Approve the indidivual task PR from Rakshith
- Add parameters for **get_events()** in `my_functions.py` and change the map area to Java Island in `MapMaker.ipynb` before create PR

### Jiarun

29/04    
 - Reviewed and approved request#1 pulled by Dzaky.  
 - Reviewed and approved request#2 pulled by Zhihan.  
 - Pulled request#3 to add my name to README.md.  
 
02/05    
 - Pulled request#5 to change my folder's name.  
 
04/05    
 - Reviewed and approved request#6 pulled by Dzaky.
 
04/05    
 - Reviewed and approved request#9 pulled by Rakshith.
 
05/05  
 - Pulled request#10 to add my information to README.md.

06/05    
 - Pulled request#11 to upload my individual work.
 
10/05  
 - Reviewed request#13 pulled by Dzaky, and pointed out some errors in his code.

13/05  
 - Reviewed and approved request#14 pulled by Zhihan.
 - Reviewed and approved request#15 pulled by Zhihan.
 - Reviewed and approved request#16 pulled by Zhihan.

16/05    
 - Pulled request#17 to do some changes in README.md.
 - Pulled request#18 to display the information table in README.md.

18/05    
 - Reviewed request#19 pulled by Rakshith and pointed out some errors and gave my comments.
 - Approved request#19 pulled by Rakshith.
 - Pulled request#21 to add examples into docstrings in my_functions.py.
 
19/05  
 - Reviewed and approved request#23 pulled by Zhihan.
 - Reviewed and approved request#24 pulled by Zhihan.

20/05  
 - Pulled request#25 to delete a needless file and propose a possible structure for our group report.

21/05  
 - Reviewed and approved request#26 pulled by Rakshith.
 
22/05  
 - Approved request#13 pulled by Dzaky.
 - Reviewed and approved request#27 pulled by Dzaky.
 - Reviewed and approved request#28 pulled by Dzaky.
 - Merged request#29 pulled by Rakshith.
 - Pulled request#31 to add my group work records into report.md.
 - Reviewed and approved request#31 pulled by Dzaky.


## Collaborative editing of documents

Editting history for `report.md` and `README.md`.

### Dzaky
5/5/2022
- Initialize the group members template for README.md

22/5/2022
- Writing individual part in `report.md`
- Initialize general description and link to individual work in `README.md`
- Add contribution report in `report.md`

23/5/2022

### Jiarun

16/05  
 - Did some changes in `README.md` to make it look better.

20/05  
 - Proposed the structure for the group report.
 
22/05 
 - Added his request and issue records to `report.md`.
 - Put his work into `README.md`.

## Creating and resolving issues

Issue records in GitHub.

### Dzaky  

19/5/2022
- Raise issues about writing report

### Jiarun

04/05  
 - Submitted issue#7 about the token used in **my_basemaps()**.

17/05  
 - Answered issue#20 submitted by Rakshith.
 
19/05  
 - Answered issue#22 submitted by Dzaky.


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
