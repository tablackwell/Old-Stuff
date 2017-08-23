# Proj4.py
# Thomas Blackwell
# Compsci 141
#
# This program calculates the rusher rating for National Football League
# rushers, finds the best rushers over a 2 year period, as well as which team
# has the best rushing unit during this period. The program imports raw NFL
# statistics from a file named rushers.csv. The rusher rating will be computed,
# and the 50 best rushers will be printed. In addition to rusher rating, this
# program collects the player who rushed the most yards in a year, the player
# who rushed for the most touchdowns in a year, the player who has the highest
# yardage per attempt, and the player who had the most fumbles. These additional
# statistics are all calculated in their own independent functions, with the 
# functions being called at the end of the program. They are also printed. 

# These statistics
# are limited to players who have rushed more than 10 times to remove outliers
# from the calculation. The rusher rating is calculated by first calculating
# three intermediate statistics: Yards, perTDs, and perFumbles. Yards is 
# calculated by the equation [total yards / (4.05 * attempts)]. If this number 
# is greater than 2.375, then 2.375 is used instead. This is the yards gained
# per attempt. perTDs is the percentage of touchdowns per carry. This is
# calculated by [(39.5 * touchdowns) / attempts]. This too is replaced by 2.375
# if it is greater than 2.375. perFumbles is the percentage of fumbles per carry
# this is calculated with the formula [2.375 - ((21.5 * fumbles) / attempts)]. 
# The rusher rating is finally calculated with the formula
# [Yards + perTDs + perFumbles] * (100 / 4.5). This is then printed. 

# opens the .csv file, reades first line to discard it, assigns empty lists for
# useage later

rushersFile = open('rushers.csv', 'r')
rushersFile.readline()

playerInfo = []
teamInfo2010 = []
teamInfo2011 = []


# iterates through rushersFile by line

for line in rushersFile:
    
    # removes trailing characters, forms list by splitting the lines on commas
    
    line = line.rstrip()
    tempList = line.split(',')
    attempts = int(tempList[5])
    
    # assigns variables based on index in list
    
    name = tempList[0] + ' ' + tempList[1]
    pos = tempList[2]
    year = tempList[13]
    team = tempList[3]
    totalYards = int(tempList[6])
    rushingTDs = int(tempList[7])
    fumbles = int(tempList[10])    
    
        
    
    # skips player if player rushes less than 10 times
    
    if attempts > 10:

        # calculates variables needed for rusherRating, replaces values with
        # 2.375 if they are greater than 2.375. 

        yards = (totalYards / (4.05 * attempts))
        if yards > 2.375:
            yards = 2.375
            
        # calculates perTDs
        
        perTDs = ((39.5 * rushingTDs) / attempts)
        if perTDs > 2.375:
            perTDs = 2.375
        
        # calculates perFumbles
        
        perFumbles = (2.375 - ((21.5 * fumbles) / attempts))
        
        # calculates rusherRating, rounds to nearest 2 decimals
        
        rusherRating = (yards + perTDs + perFumbles) * (100 / 4.5)
        rusherRating = round(rusherRating, 2)
        
        # creates and appends the player info in a list to a list of players
        
        individPlayerInfo = [rusherRating, name , pos, year, attempts, team]
        playerInfo.append(individPlayerInfo)
        
        # if the player's year is 2010, it appends their statistics to
        # the list of players in 2010, teamInfo2010
        
        if year == '2010':
            playerInfoTeam = [team, attempts, totalYards, rushingTDs, fumbles]
            teamInfo2010.append(playerInfoTeam)
        
        # if the player's year is 2011, it appends their statistics to
        # the list of players in 2011, teamInfo2011
        
        elif year == '2011':
            playerInfoTeam = [team, attempts, totalYards, rushingTDs, fumbles]
            teamInfo2011.append(playerInfoTeam)                    
        

# sorts players by rusherRating

playerInfo = sorted(playerInfo, reverse = True)


# prints header

print('''\nThe following statistics are only for the years 2010 and 2011.
Only those rushers who have rushed more than 10 times are included.

The top 50 rushers based on their rusher rating in individual years are:
Name                           Pos   Year  Attempts   Rating  Team''')

# prints the top 50 players by rusher rating using a for loop

for player in playerInfo[0:50]:
    print("%-30s %-2s %5s %8s %11s  %s" % (player[1],player[2],player[3],\
                                            player[4],player[0],player[5]))
    
# Adds runningbacks to a list

rbList = []

for player in playerInfo:
        if player[2] == 'RB':
            rbList.append(player)

# Prints the header

print('''\nThe top 20 running backs based on their rusher rating in individual \
years are:
Name                           Pos   Year  Attempts   Rating  Team''')


# Prints the top 20 runningbacks. No need to sort since list was sorted earlier

for player in rbList[0:20]:
    print("%-30s %-2s %5s %8s %11s  %s" % (player[1],player[2], \
                            player[3],player[4],player[0],player[5]))
    
# closes the .csv file

rushersFile.close()


def rankings(yearList, year):
    '''Sifts through player data to add up statistics for a single team, then
    calculates the rating for teams with a total attempts that are greater than 
    10. Takes a list of players and a year. The lists are teamInfo2010 and
    teamInfo2011.'''
    
    # sorts the list that is currently in use, makes an empty list for output
    
    yearList = sorted(yearList)
    outputList = []
    
    # initializes variables that act as a running total, and an index that
    # serves as a count for a while loop later on
    
    totalAttempts = 0     
    totalYards = 0
    totalTouchdowns = 0
    totalFumbles = 0
      
    index = 0
    
    # main while loop. Runs until the entire list has been evaluated.
    
    while index < (len(yearList) -1):
        
        # Assigns the team name
        
        initialTeam = yearList[index][0]
        
        # secondary while loop, runs until the team name category and the name
        # of team of the current play is being evaluated, as well as the same
        # while loop from earlier.
        
        while yearList[index][0] == initialTeam and index < (len(yearList) -1):
            totalAttempts += int(yearList[index][1])
            totalYards += int(yearList[index][2])
            totalTouchdowns += int(yearList[index][3])
            totalFumbles += int(yearList[index][4])
            index += 1
            
        # calculates the intermediary variables and the rusher rating provided
        # that the totalAttempts are greater than 10
        
        if totalAttempts > 10:
            yards = (totalYards / (4.05 * totalAttempts))
            if yards > 2.375:
                yards = 2.375
                        
            perTDs = ((39.5 * totalTouchdowns) / totalAttempts)
            if perTDs > 2.375:
                perTDs = 2.375
                    
            perFumbles = (2.375 - ((21.5 * totalFumbles) / totalAttempts))
                    
            # calculates rusherRating, rounds to nearest 2 decimals
                    
            rusherRating = (yards + perTDs + perFumbles) * (100 / 4.5)
            rusherRating = round(rusherRating, 2)
            
            outputList.append([rusherRating,initialTeam])
            
        totalAttempts = 0     
        totalYards = 0
        totalTouchdowns = 0
        totalFumbles = 0
        
    # sorts the outputList in descending order 
    
    outputList = sorted(outputList, reverse = True)
    
    # prints the No. 1 team and their rusher rating
    
    print()
    print("The best team for %5s is: %3s with an overall rusher rating of%7.2f."\
          %(year,outputList[0][1],outputList[0][0]))
    
    # prints the rest of the teams and their respective rusher ranking, as
    # well as their rank
    
    print("\nThe remainder of the teams are:")
    count = 2
    
    for team in outputList[1:33]:
        print("%2d %-3s %14.2f"%(count,team[1],team[0]))
        count += 1
        
    print()


def mostYards():
    '''this function finds the player who rushed for the most yards in a year.
    It does this by creating a list of players sorted by their total yardage, 
    then prints the first player in this list.'''
    
    # opens the rushersFile, makes the empty list described above, and reads
    # the first line in the file. 
    
    rushersFile = open('rushers.csv', 'r')
    yardages = []
    rushersFile.readline()
    
    # for loop takes each line in rushersFile, forms a temporary list, and
    # assigns variables based on the index of that variable in the temporary
    # list. 
    
    for line in rushersFile:
        line = line.rstrip()
        tempList = line.split(',')
        name = tempList[0] + ' ' + tempList[1]
        team = tempList[3]
        year = tempList[13]
        totalYards = int(tempList[6])
        attempts = int(tempList[5])
        
        # appends the previously acquired statistics to the yardages list, 
        # provided that the player's attempts are greater than 10. 
        
        if attempts > 10:
            yardages.append([totalYards,name,team,year])
    
    # sorts the yardages in descending order
    
    yardages = sorted(yardages, reverse = True)
    
    # prints the top rusher (by yardage), as well as the yardage, the player's
    # team, and the year. 
    
    print("The person who rushed for the most yardage is:")
    print("%15s rushing for %s yards for %s in %s."%(yardages[0][1],
                            yardages[0][0],yardages[0][2],yardages[0][3]))
                                                     
    print()
    
    # closes the file
    
    rushersFile.close()
    
    
def mostTouchdowns():
    '''this function finds the player who scored the most touchdowns in a year.
    It does this by creating a list of players sorted by their total touchdowns, 
    in descending order, then prints the first player in this list.'''
    
    # opens the rushersFile, makes the empty list described above, and reads
    # the first line in the file. 
    
    rushersFile = open('rushers.csv', 'r')
    tdList = []
    rushersFile.readline()
    
    # for loop takes each line in rushersFile, forms a temporary list, and
    # assigns variables based on the index of that variable in the temporary
    # list.     
    
    for line in rushersFile:
        line = line.rstrip()
        tempList = line.split(',')
        name = tempList[0] + ' ' + tempList[1]
        team = tempList[3]
        year = tempList[13]
        touchdowns = int(tempList[7])
        attempts = int(tempList[5])
        
        # appends the previously acquired statistics to the touchdown list, 
        # provided that the player's attempts are greater than 10. 
        
        if attempts > 10:
            tdList.append([touchdowns,name,team,year])
            
    # sorts the total touchdowns in descending order.
    
    tdList = sorted(tdList, reverse = True)
    
    # prints the name of the individual with the greatest number of touchdowns, 
    # their number of touchdowns, their team, and the year that the feat was 
    # achieved.
    
    print("The person who scored the most rushing touchdowns is:")
    print("%15s rushing for %s touchdowns for %s in %s "%(tdList[0][1],\
            tdList[0][0],tdList[0][3],tdList[0][3]))
    
    print()
     
    # closes the file      
    
    rushersFile.close()
    
    
def highestYardsPerAttempt():
    '''this function finds the player who has the highest yardage per attempts.
    It does this by creating a list of players sorted by their yardage per
    attempt ratio in descending order, then prints the first player in this 
    list.'''
    
    # opens the rushersFile, makes the empty list described above, and reads
    # the first line in the file.   
    
    rushersFile = open('rushers.csv', 'r')
    ratioList = []
    rushersFile.readline()
    
    # for loop takes each line in rushersFile, forms a temporary list, and
    # assigns variables based on the index of that variable in the temporary
    # list.      
    
    for line in rushersFile:
        line = line.rstrip()
        tempList = line.split(',')
        name = tempList[0] + ' ' + tempList[1]
        team = tempList[3]
        year = tempList[13]
        yardsPerAttempt = float(tempList[9])
        
        attempts = int(tempList[5])
        
        # appends the previously acquired statistics to the yards per attempt 
        # list, provided that the player's attempts are greater than 10.  
        
        if attempts > 10:
            ratioList.append([yardsPerAttempt,name,team,year])
            
    # sorts the list of yards per attempt in descending order
    
    ratioList = sorted(ratioList, reverse = True)
    
    # prints the name of the individual, their yeards per attempt ratio, their
    # team, and the year the feat was achieved. 
    
    print('The person who has the highest yards per rushing attempt with',\
          'over 10 rushes is:')
    
    print("%14s rushing with a %s yards per attempt rushing average for %s in\
    %s"%(ratioList[0][1],ratioList[0][0],ratioList[0][2],ratioList[0][3]))
    
    print()
    
    # closes the file
    
    rushersFile.close()
    
    
def mostFumbles():
    '''this function finds the player who had the most fumbles in a year.
    It does this by creating a list of players sorted by their number of fumbles
    in descending order, then prints the first two players in this list. Two 
    players are printed because they have an equal number of fumbles'''
    
    # opens the rushersFile, makes the empty list described above, and reads
    # the first line in the file.   
    
    rushersFile = open('rushers.csv', 'r')
    fumblerList = []
    rushersFile.readline()
    
    # for loop takes each line in rushersFile, forms a temporary list, and
    # assigns variables based on the index of that variable in the temporary
    # list.   
    
    for line in rushersFile:
        line = line.rstrip()
        tempList = line.split(',')
        name = tempList[0] + ' ' + tempList[1]
        team = tempList[3]
        year = tempList[13]
        fumbles = int(tempList[10])
        
        attempts = int(tempList[5])
        
        # appends the previously acquired statistics to the number of fumbles
        # list, provided that the player's attempts are greater than 10. 
        
        if attempts > 10:
            fumblerList.append([fumbles,name,team,year])
            
    # sorts the list of total number of fumbles in descending order
    
    fumblerList = sorted(fumblerList, reverse = True)
    
    # prints the top two fumblers, the number of fumbles, their team, and the
    # year in which the not-so-impressive feat occured. 
    
    print("There are 2 people with the most fumbles. They are:")
    
    print("     %s with %s fumbles for %s in %s."%(fumblerList[0][1],\
                        fumblerList[0][0],fumblerList[0][2],fumblerList[0][3]))
    
    print("     %s with %s fumbles for %s in %s."%(fumblerList[1][1],\
                        fumblerList[1][0],fumblerList[1][2],fumblerList[1][3]))
    print()
    
    rushersFile.close()

# Runs the functions involved with the program. The rankings() functions call
# rankings and pass teamInfo2010 with the year 2010, and teamInfo2011 with the
# year 2011, respectively. The lines mostYards(), mostTouchdowns(), etc. simply
# call the functions without passing any variables. 

rankings(teamInfo2010, 2010)
rankings(teamInfo2011, 2011)
mostYards()
mostTouchdowns()
highestYardsPerAttempt()
mostFumbles()