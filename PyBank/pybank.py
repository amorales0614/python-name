#import dependencies
import os
import csv

#read in csv file
budgetpath = os.path.join("Resources","budget_data.csv")

#set variables and empty lists to gather data
monthCount = 0
totalProLoss = 0
totalMonthlyChanges = 0
initialProLoss = 0
profit = []
monthChange = []
date = []

#open the csv file and skip header
with open(budgetpath) as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=",")
    budget_header = next(budgetreader)

    #initiate for loop
    for row in budgetreader:

    	#count rows in file to count number of months
    	monthCount = monthCount + 1
    	
    	#initiate total profit calculations, adding each profit value to the list then adding it to total
    	profit.append(row[1])
    	totalProLoss = totalProLoss + int(row[1])

    	#calculating monthly changes and storing in list for calculating max/min later
    	nextProLoss = int(row[1])
    	monthlyProLossChanges = nextProLoss - initialProLoss
    	monthChange.append(monthlyProLossChanges)

    	#counting and resetting variables	
    	totalMonthlyChanges = totalMonthlyChanges + monthlyProLossChanges
    	initialProLoss = nextProLoss

    	#calculating avg monthly change
    	avgMonthlyChange = (totalMonthlyChanges/monthCount)

    	#finding greatest and least monthly change using monthChange list
    	greatestInc = max(monthChange)
    	greatestDec = min(monthChange)

    	#finding date associated with greatest inc or dec, loop is appending each date to the date list
    	date.append(row[0])
    	incDate = date[monthChange.index(greatestInc)]
    	decDate = date[monthChange.index(greatestDec)]

    #printing results
    print("Financial Analysis")
    print("---------------------")
    print("Total Months: " + str(monthCount))
    print("Total Revenue: $" + str(totalProLoss))
    print("Average Monthly Change: $" + str(avgMonthlyChange))
    print("Greatest Monthly Increase: " + str(incDate) + " ($" + str(greatestInc) + ")")
    print("Greatest Monthly Decrease: " + str(decDate) + " ($" + str(greatestDec) + ")")
    print("---------------------")

#writing results to text file
with open('bankanalysis.txt', 'w') as text:
	text.write("-------------------------\n")
	text.write("Financial Analysis\n")
	text.write("-------------------------\n")
	text.write("Total Months: " + str(monthCount) + "\n")
	text.write("Total Revenue: $" + str(totalProLoss) +"\n")
	text.write("Average Monthly Change: $" + str(avgMonthlyChange) + "\n")
	text.write("Greatest Monthly Increase: " + str(incDate) + " ($" + str(greatestInc) + ") \n")
	text.write("Greatest Monthly Decrease: " + str(decDate) + " ($" + str(greatestDec) + ") \n")
	text.write("-------------------------\n")
