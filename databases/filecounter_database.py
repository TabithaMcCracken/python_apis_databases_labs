'''
Collect the same information you saved to a CSV file before into a database instead. 
You can use a file-based SQLite database or a server-based database such as PostgreSQL or MySQL.

Additionally, look into Python's datetime module and attempt to track the times when you ran your script.
Once your script is set up to save its run data into your database, you'll next 
write a script to analyze your collected desktop statistics.

Use your Python skills to calculate:

The total number of files that was on your desktop since you started tracking it
The total number for each file type
On what day you had the most items on your desktop
The most common file type ever to clutter your desktop
Write your results to a new table in your database and set your analysis script 
up so that it keeps updating this table on each execution.

Tasks
Write a script that stores the information returned from your file counter script in a SQL database.
Read the saved data from your database and analyze it.
Write the results of your analysis to another table in your database.
'''

# Get tools
import pathlib
import datetime

# Find the path to my desktop
desktop = pathlib.Path('/Users/tabithamccracken/Desktop')

# Create new list
file_list = []


for filepath in desktop.iterdir(): # Loop through each file
    #if filepath.suffix == '.jpg': # Filter files with .jpg
    file_list.append(str(filepath.name)) #Add to file list
    
    time_tracker = datetime.datetime.now()

print(file_list) # Print the file list
print(f"This list update occured at : {time_tracker}")

