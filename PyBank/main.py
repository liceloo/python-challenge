#PyBank
'''
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

1) The total number of months included in the dataset
2) The net total amount of "Profit/Losses" over the entire period
3) The changes in "Profit/Losses" over the entire period, and then the average of those changes
4) The greatest increase in profits (date and amount) over the entire period
5) The greatest decrease in profits (date and amount) over the entire perio
'''

import os, csv

#budget_path = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')
file = r"C:\Users\alice\Downloads\python-challenge\Starter_Code\PyBank\Resources\budget_data.csv"

#initializing lists
total_months = []
total_profit = []
profit_change = []

#open csv
with open(file) as budget:
    reader = csv.reader(budget)
    header = next(reader)
    #fill month and profit lists
    for row in reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    #fill profit change
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1] - total_profit[i])
    #average change
    average_change = sum(profit_change)/len(profit_change)
    #greatest inc/dec values
    max_profit = max(profit_change)
    min_profit = min(profit_change)
    #find index of greatest inc/dec in profits
    max_index = profit_change.index(max_profit)
    min_index = profit_change.index(min_profit)

    

#printing into terminal
print('Financial Analysis') 
print(f'----------------------------')
print(f'Total Months: {len(total_months)}')
print(f'Total: {sum(total_profit)}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {total_months[max_index + 1]} (${max_profit})')
print(f'Greatest Decrease in Profits: {total_months[min_index + 1]} (${min_profit})')  
  
#txt file 
txt_file = r"C:\Users\alice\Downloads\python-challenge\Starter_Code\PyBank\Resources\PyBank_output.txt"
with open(txt_file, 'w') as text_file:
    print(f'Financial Analysis', file = text_file)
    print(f'-------------------------', file = text_file)
    print(f'Total Months: {len(total_months)}', file = text_file)
    print(f'Total: {sum(total_profit)}', file = text_file)
    print(f'Average Change: ${average_change:.2f}', file = text_file)
    print(f'Greatest Increase in Profits: {total_months[max_index + 1]} (${max_profit})', file = text_file)
    print(f'Greatest Decrease in Profits: {total_months[min_index + 1]} (${min_profit})', file = text_file)
 
