# openspace-organizer
Project-1/Solo

Objective:
1. To create a Python script that runs each day and randomly assign seats to colleagues in an office with the following set up-
Tables-6
Seats -4 seats each table
2. Create a local and a GitHub project with the repository name "openspace-organizer" with predefined files and folders

Prequistes:

1. Packages:
os
pandas
random
pyarrow
openpyxl

2.Created a venv and presented the versions in requirements.txt
3.Created an Excel (text)file with the names of the colleagues

Python scripts

table.py conntains the command for generating class Seat and Table and the required attributes and methods.
The class Seat has the attributes free and occupant.
The class Table creates a list of 4 empty Seat objects.
Class Table has the attributes-capacity, record of people already sitting and list of empty objects.
The method named __init__() is the constructor in Python.

The if and else statements in the Python script allowed the function to make decisions based on the value of the input and return different outputs accordingly.

openspace.py contains the script for generating class openspace with attributes number_of_tables, tables and persons.
The class allows to organize the default spaces (24) seats randomly over the available tables
The functions were defined for organize,display, free seats, persons in room, store the output in Excel file

main.py file serves as the central script that ties together the various components of your Python application and defines its behavior. main.py contains the script that is executed when you run your Python program.
The if __name__ == "__main__": block ensures that the code inside it only runs if the script is executed directly.
When we run the main.pay file, we generate an excel file with the required commands.

![Hope everyone gets the seat:>](https://giphy.com/gifs/southparkgifs-l0HlMglmxM0tjs5Ko)
