# What it does
Will print out list of students that are in common between 2 Excel files.

In this case repeat students. Note Excel files not saved to Github as privacy concerns. The data is accessible from Vula CEM1000W 2018 and 2019.

# How to run
`python excel_list_compare.py`

To use for different input files edit the python code (yes this is bad)
`
oldfile = "CEM1000W_2018_2019_03_07.xlsx"
newfile = "CEM1000W_2019_2019_03_07.xlsx"
`

# Dependencies
I've used Anaconda Python in Windows - https://www.anaconda.com/distribution/ .
Pandas is a requirement. Either create a new environment or install to the base environment

`conda install pandas`

# data structure
Excel files have a single sheet, 'Sheet0'.
Columns are : ``"Name"	"User ID"	"Email Address"	"Role"``
Data in columns looks like ``"Surname, Name"	"xxxyyy000"	"name@domain"	"Student"``
