import os
from random import sample
from src.table import Table, Seat

class OpenSpace:
# The class allows to organize the default spaces (24) seats randomly over the available tables.

    def __init__(self, number_of_tables: int, tables: list=[]):
        self.tables = tables
        self.number_of_tables = number_of_tables
        self.tables = [Table() for i in range(self.number_of_tables)]
        self.persons = 0

    def organize(self, names: list):
        # Randomly assign people to the Seat objects in the different Table objects
        names = sample(names, len(names))
        for name in names: 
            for table in self.tables:
                # go to the next table if table is full
                if table.has_free_spot() == False:
                    continue
                table.assign_seat(name)
                self.persons += 1
                break
        if len(names) > len(self.tables)*4:

# raise a ValueError("There are too many persons in the room to be seated!!! The default amount is 24 seats, please add a table")

            def display(self):
        # Displays the different tables and their occupants in a nice and readable way
                for i, table in enumerate(self.tables):
                    print(f"At table {i+1} sits:")
            for person in table.seats:
                print(person)

        def free_seats(self):
        # returns the total free seats available
            seats = [table.capacity_left() for table in self.tables]
            seats = sum(seats)
            return seats

def persons_in_room(self):
        return self.persons
    
def store(self):
        # Store the repartition in an Excel file
        pass
