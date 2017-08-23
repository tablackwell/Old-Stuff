# Proj2.py
# Thomas Blackwell
# Compsci 141

# This program serves as an inventory manager for Clipper Manufacturing Company. 
# The program prints a main menu that presents users with four options for
# managing the inventory. The main menu will continue to prompt users for input
# until the user quits the program with an input of Q or q. 
# Users can add items to inventory, remove items from inventory, or print a
# bar chart with the quantity of items represented by asterisks. 

# The warehouse may only keep 50 of an item at any particular time, and will 
# print an error message if a user attempts bring the inventory past 50 for a 
# particular item, or if the user attempts to withdraw more items than are 
# present in inventory. The items tracked are Bicycles, Unicycles, Mopeds, 
# Skateboards, and Skates. An input of A or a allows for adding items to 
# inventory, R or r for removing items from inventory, G or g for printing the
# inventory's chart (which displays both number of items and charts where 
# asterisks represent quantity, and Q or q for quitting the program.

# The following code sets the quantity of items to zero, sets item types to ints, 
# and sets actionType to a string type. 

bicycles = 0
unicycles = 0
mopeds = 0
skateboards = 0
skates = 0

bicycles = int(bicycles)
unicycles = int(unicycles)
mopeds = int(mopeds)
skateboards = int(skateboards)
skates = int(skates)


actionType = str

# This prints the main menu, and presents the user with four options. The menu
# will loop until "Q" or "q" is inputted, upon which an exit message is printed. 
# Each individual option corresponds to a distinct if statement. Valid inputs
# are "A", "R", "G", and "Q". An invalid input results in an error message. Both
# lowercase and uppercase inputs are acceptable, as all inputs are converted
# to lowercase.

while actionType != "q":
    print("\nClipper Manufacturing Company\n")
    print("  Main Menu")
    print("A) Add a number of items to a product's inventory.")
    print("R) Remove a number of items from a product's inventory.")
    print("G) Graph the number of all products by using a bar graph.")
    print("Q) Quit the program\n")
    actionType = input("Enter choice: ").lower()
    print(actionType)

# The section codes for adding items to the inventory. An error will be printed
# should the requested addition amount result in an inventory > 50. 
# Mathematically, the requested amount to add is simply added to the original 
# quantity. 

    if actionType == "a":
        itemType = input("Inventory item to add to: ").lower() 
        print(itemType)
        itemQuantity = int(input("Number to add: "))
        print(itemQuantity)
        
        if itemType == "bicycles" or itemType == "unicycles" or itemType == \
           "mopeds" or itemType == "skateboards" or itemType == "skates":
            
            if itemType == "bicycles":
                if itemQuantity + bicycles <= 50:
                    bicycles = bicycles + itemQuantity
                    print("Current inventory for bicycles:",bicycles)
                else:
                    print("*** ERROR: maximum items exceeded ***")  
                    
            if itemType == "unicycles":
                if itemQuantity + unicycles <= 50:
                    unicycles = unicycles + itemQuantity
                    print("Current inventory for unicycles:",unicycles)
                else:
                    print("*** ERROR: maximum items exceeded ***") 
                    
            if itemType == "mopeds":
                if itemQuantity + mopeds <= 50:
                    mopeds = mopeds + itemQuantity
                    print("Current inventory for mopeds:",mopeds)
                else:
                    print("*** ERROR: maximum items exceeded ***")  
                    
            if itemType == "skateboards":
                if itemQuantity + skateboards <= 50:
                    skateboards = skateboards + itemQuantity
                    print("Current inventory for skateboards:",skateboards)
                else:
                    print("*** ERROR: maximum items exceeded ***")  
                    
            if itemType == "skates":
                if itemQuantity + skates <= 50:
                    skates = skates + itemQuantity
                    print("Current inventory for skates:",skates)
                else:
                    print("*** ERROR: maximum items exceeded ***")
                    
        else:
            print("*** ERROR: Illegal item  ***")

# This section codes for removing items from inventory. An error will be printed
# should the requested amount to remove cause the inventory to drop below 0.
# The mathematical operations are rather simple: requested amount subtracted 
# from original amount.

    if actionType == "r":
        itemType = input("Inventory item to remove from: ").lower()
        print(itemType)
        itemQuantity = int(input("Number to remove: "))        
        print(itemQuantity)
        
        if itemType == "bicycles" or itemType == "unicycles" or itemType == \
           "mopeds" or itemType == "skateboards" or itemType == "skates":
            
            if itemType == "bicycles":
                if bicycles - itemQuantity >= 0:
                    bicycles = bicycles - itemQuantity
                    print("Current inventory for bicycles:",bicycles)
                else:
                    print("*** ERROR: minimum items exceeded ***") 
                    
            if itemType == "unicycles":
                if unicycles - itemQuantity >= 0:
                    unicycles = unicycles - itemQuantity
                    print("Current inventory for unicycles:",unicycles)
                else:
                    print("*** ERROR: minimum items exceeded ***")     
                    
            if itemType == "mopeds":
                if mopeds - itemQuantity >= 0:
                    mopeds = mopeds - itemQuantity
                    print("Current inventory for mopeds:",mopeds)
                else:
                    print("*** ERROR: minimum items exceeded ***")     
                    
            if itemType == "skateboards":
                if skateboards - itemQuantity >= 0:
                    skateboards = skateboards - itemQuantity
                    print("Current inventory for skateboards:",skateboards)
                else:
                    print("*** ERROR: minimum items exceeded ***") 
                    
            if itemType == "skates":
                if skates - itemQuantity >= 0:
                    skates = skates - itemQuantity
                    print("Current inventory for skates:",skates)
                else:
                    print("*** ERROR: minimum items exceeded ***")
                    
        else:
            print("*** ERROR: Illegal item  ***")
            
# This section creates 5 new variables to represent the stars that will be 
# printed in the chart, and prints the chart upon user request. The chart
# prints number of items in inventory, along with the chart. 

    if actionType == "g":
        
        bicyclestars = "* " * bicycles
        unicyclestars = "* " * unicycles
        mopedstars = "* " * mopeds
        skateboardstars = "* " * skateboards
        skatestars = "* " * skates
        
        print("Item        Number\tChart")
        print("Bicycle{:7d}\t\t{:5s}".format(bicycles,bicyclestars))
        print("Unicycle{:6d}\t\t{:5s}".format(unicycles,unicyclestars))
        print("Moped{:9d}\t\t{:5s}".format(mopeds,mopedstars))
        print("Skateboard{:4d}\t\t{:5s}".format(skateboards,skateboardstars))
        print("Skates{:8d}\t\t{:5s}".format(skates,skatestars))
    
# The following prints an error statement if the user select an inappropriate
# input. 
    
    if actionType not in ["a","r","g","q"]:
        print("You've entered an incorrect choice. Please try again")
    

# This final line displays a quit message upon ending the loop (entering Q)
        
print("Thank you for using the inventory program")
