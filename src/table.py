# A class is defined 

class Seat:
    def __init__(self, occupant, free=True):
        self.free = free
        self.occupant = None  # occupant is string

    # The method named __init__() is the constructor in Python. It is called always when an object is created.
#The syntax for creating an attribute is:
       # self.attribute = something
 #There is a special method called:
 #   __init__()

    def set_occupant(self, name):
        if self.free == True:
            self.occupant = name
            print(f"{name} has taken the seat.")
        else:
            print(f"The seat is already occupied by {self.occupant}.")
 #seats a person if spot is available
    def remove_occupant(self, NAME ): # working
        # Removes someone from a seat and returns the name of the person occupying the seat before
        if self.free == False and self.occupant ==NAME:
            self.free = True
            self.occupant = None
            print(f"{NAME} has left the seat.")
            return NAME
        else:
            print(f"the seat is not occupied by {NAME}.")

# Removes someone from a seat and returns the name of the person occupying the seat before

    def __str__(self):
        return self.occupant
        
def __init__(self, capacity: int=4): # takes a list of Seat objects
        self.capacity = capacity
        self.capacity_counter = capacity
        self.index = 0
        self.seats = [Seat() for i in range(self.capacity)]


#•	A class Table is defined 
class Table:
     
# The class Table creates a list of 4 empty Seat objects.
# The attributes of Table are capacity, record of people already sitting and list of empty objects Seat
 def __init__(self,  capacity: int=4): # takes a list of Seat objects
        self.capacity = capacity
        self.seats=[Seat('free','occupant') for _ in range(capacity)]
 def has_free_spot(self):
     return any(seat.free for seat in self.seats)

# Returns True or False if a spot is available
 
    # places someone at the table
 def assign_seat(self, name): # working
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
            else:
                return False
 def capacity_left(self):
       return sum(seat.free for seat in self.seats)

 def capacity_left(self): # working
        # returns integer
        return self.capacity_counter

    
