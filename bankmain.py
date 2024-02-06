#Import modules
import os
import csv
#Prime data and analysis
budget_data_csv=os.path.join("Resources", "budget_data.csv")
bank_analysis_txt=os.path.join("bankanalysis", "bankanalysis.txt")
#Define parameters
rows=[]
allprofits=[]
shift_list=[]
rowscount=0
#Open data
with open(budget_data_csv) as budget:
    csvreader=csv.reader(budget)
    header=next(csvreader)
    #Count dates and profits
    for row in csvreader:
        rows.append(row[0])
        allprofits.append(int(row[1]))
        #Calculate Average Change
        if rowscount>0:
            shift=int(row[1])-prevcount
            shift_list.append(shift)
        rowscount+=1
        prevcount=int(row[1])
#Calculate Greatest Increase and Greatest Decrease
greatest_rise=max(shift_list)
greatest_fall=min(shift_list)
riseamount=shift_list.index(greatest_rise)
fallamount=shift_list.index(greatest_fall)
risedate=rows[riseamount+1]
falldate=rows[fallamount+1]
meanchange=(sum(shift_list))/len(shift_list)
#Prepare data for txt
outcome = f"""
Financial Analysis
----------------------------
Total Months: {len(rows)}
Total: ${sum(allprofits)}
Average Change: ${meanchange:.2f}
Greatest Increase in Profits: {risedate} (${greatest_rise})
Greatest Decrease in Profits: {falldate} (${greatest_fall})
"""
#Export data to txt
print(outcome)
with open(bank_analysis_txt, "w") as stats:
    stats.write(outcome)