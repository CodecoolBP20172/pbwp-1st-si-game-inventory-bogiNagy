# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
# Display7s the inventory.
import sys
import csv
import operator
inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory: \n")

    for key,value in inventory.items():
        print(value,key)

    return("Total number of items:%d"%sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    order=str(input("Please enter the type of ordering your dictionary:"))

    unsorted=sorted(inventory.items())
    sorted1=sorted(inventory.items(),key=operator.itemgetter(1))
    sorted2=sorted(inventory.items(),key=operator.itemgetter(1), reverse=True)

    while True: 
        try:
            for turn in range(1):
                if order == ' ':
                    sorting=unsorted
                elif order == 'count,desc':
                    sorting=sorted1
                elif order =='count,asc':
                    sorting=sorted2
                break
        except ValueError:
            print("Choose ' ' or 'count,desc' or 'count,asc' .")
            continue
    lst=[]
    for tup in sorting:
        lst.append(len(tup[0]))
    k=max(lst)
    j=max(lst)
    print('count'.rjust(k),'    ','item name'.rjust(j))
    for i in range(k+j+5):
        sys.stdout.write('-')
    print('\nTotal number of items: %d'%sum(inventory.values))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    file=open(filename,'r')
    reader=csv.reader(file)
    for row in reader:
          importlst=(row)
    for item in importlst:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]=1
    return (inventory)
    file.close()


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
