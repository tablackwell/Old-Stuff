# Proj1.py
# Thomas Blackwell
# Compsci 141

# This program calculates the "Passer Rating" for football quarterbacks, after
# prompting the user for the player's name, year, number of completions, passing
# attempts, number of yards, number of passing touchdowns, and number of
# interceptions. 

# The program uses the inputted statistics to conduct five calculations: comps,
# yards, touchdowns, and interceptions. The mathematical operations involved in
# calculating these intermediate values can be observed in lines 47 through 55. 
# These variables are then used to calculate the passer rating, which is a sum
# of comps, yards, touchdowns, and interceptions, all divided by 6 and multipled
# by 100. The result should not exceed 158.3


# The following prompts the user for the player's statistics, echo prints the
# inputs, and converts numeric inputs to int types. 

playerName = input("Enter the player's name: ")
print(playerName)

playerYear = input("Enter the player's year: ")
print(playerYear)

totalCompletions = int(input("Enter the total number of completions: "))
print(totalCompletions)

totalAttempts = int(input("Enter the number of passing attempts: "))
print(totalAttempts)

totalYards = int(input("Enter the total number of yards: "))
print(totalYards)

passingTouchdowns = int(input("Enter the total number of passing touchdowns: "))
print(passingTouchdowns)

totalInterceptions = int(input("Enter the number of interceptions: "))
print(totalInterceptions)

# The following section calculates the intermediate variables required to
# calculate the passer rating, then calculates the passer rating. 

comps = ((totalCompletions / totalAttempts) * 100 - 30) / 20

yards = ((totalYards / totalAttempts) - 3) / 4

touchdowns = (passingTouchdowns / totalAttempts) * 20

interceptions = 2.375 - ((totalInterceptions / totalAttempts) * 25)

passerRating = ((comps + yards + touchdowns + interceptions) / 6 ) * 100

# The following lines print the player statistics and the calculated 
# passer rating.

print()
print("-"*39)
print()

print("Statistics for {0} in {1}".format(playerName,playerYear))
print("     Completions :{:7d}".format(totalCompletions))
print("        Attempts :{:7d}".format(totalAttempts))
print("     Total Yards :{:7d}".format(totalYards))
print("      Touchdowns :{:7d}".format(passingTouchdowns))
print("   Interceptions :{:7d}".format(totalInterceptions))
print()
print("   Passer Rating :{:7.2f}".format(passerRating))
    
print()
print("-"*39)