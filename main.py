import pandas as pd
from src.openspace import OpenSpace
import random
import pyarrow as pa
import openpyxl

# put the main code here
if __name__ == "__main__":
   
 #read the excel file
   path = "c:/Users/admin/Desktop/openspace-organizer/src/colleagues.xlsx"
    
df = pd.read_excel(path, header = 0)
names = df.iloc[:,0].tolist()

def sitting_plan():
    return df (sitting_plan.xlsx)[["Name1", "Name2", "Condition"]].to_dict ("records")
def check_condition (name1, name2, condition):
        if condition =="next":
             return abs(name1 - name2) == 1
        elif condition == "not next":
             return abs(name1 - name2)
        else:
             return False     
    

tables = [(f"table({i+1})-seat({j+1})") for i in range(6) for j in range(4)]
print(tables)
random.shuffle(names)
# Loop through the list of names and assign them to tables and seats
with open("seating.xlsx", "w") as f:
    for i, name in enumerate(names):
        # Remove the newline character from the name
        name = name.strip()
        # Get the table and seat for the name
        table_seat = tables[i]
        # Write the name, table, and seat to the file
        f.write(f"{name} is assigned to {table_seat}\n")