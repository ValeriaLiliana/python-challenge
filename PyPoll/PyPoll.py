import pandas as pd
from pathlib import Path

# File path
file = "Starter_Code/PyBank/Resources/budget_data.csv"

# Read CSV into DataFrame
df = pd.read_csv(file)

# Count the values in the unique list above
count = len(df["Date"].unique())

# Sum of Profit/Losses column for total net change
df_net = df["Profit/Losses"].sum()

# Calculating difference of cells
df["Profit Change"] = df["Profit/Losses"].diff()
df_avg = df["Profit Change"].mean()

# Greatest Increase
max_month_index = df["Profit Change"].idxmax()
df_inc = df["Profit Change"].max()

max_month = df.iloc[max_month_index, 0]
inc_output = f"{max_month} {df_inc}"

# Greatest Decrease
min_month_index = df["Profit Change"].idxmin()
df_dec = df["Profit Change"].min()

min_month = df.iloc[min_month_index, 0]
dec_output = f"{min_month} {df_dec}"

# Create an output DataFrame
output_df = pd.DataFrame({
    'Total Months': [count],
    'Total Net Change': [df_net],
    'Average Change': [df_avg],
    'Greatest Increase in Profits': [inc_output],
    'Greatest Decrease in Profits': [dec_output]
})

# Print results to the terminal
print(output_df)

# Specify the file path for output
analysis_path = 'output/financial_analysis.txt'

# Create the 'output' directory if it doesn't exist
output_directory = Path('output')
output_directory.mkdir(exist_ok=True)

# Write results to file
with open(analysis_path, "w") as file:
    file.write(output_df.to_string(index=False))


print("Complete")
