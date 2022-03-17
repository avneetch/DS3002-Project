# Avneet Chhabra, akc7yr

import os
import pandas as pd
import sqlite3

#Real_Estate_(Residential_Details).csv
# Please note that this code is tailored to the above CSV, located in a folder called "data" on a local disk.
# This python file's objective is to ingest a CSV and convert it to either a JSON or SQL table.
# Users may also receive summaries of data.

# this data processor will accept the name of a local CSV file (Benchmark 1)
data_source = input('What is the name of the CSV on your disk you would like to use? ')
data_dir = os.path.join(os.getcwd(), 'data')
data_file = os.path.join(data_dir, data_source)
df = pd.read_csv(data_file)
print(df.head())


#here is where users can get a brief summary of the data they have input (if they want one). (Benchmark 5)
summary_request = input("Would you like to view a summary of your data? Y or N? ")
if summary_request == "Y":
    columns_in_data = df.columns
    print("The number of columns in your data is equal to ", len(columns_in_data))
    print("The number of records in your data is equal to ",len(df))
if summary_request == "N":
    print("Please proceed.")

# from here, users can decide how they want to convert the file (Benchmark 2)
conversion = input('What format do you wish to save this file in? JSON, CSV, or SQL database? ')

if conversion == "JSON":
    real_estate_json = df.to_json(path_or_buf='RealEstate_JSON', orient='records', lines=True)
    real_estate_json
    print("JSON file has been created. Please check your local disk.")
elif conversion == "CSV":
    print("File is already saved as a CSV. Please try something else.")
elif conversion == "SQL Database":
    con = sqlite3.connect('housing.db')
    sql_housing = df.to_sql('housing.db',con)
    sql_housing
    print("SQL conversion has occurred. Please check your local disk.")
else:
    print("Error: Invalid file type. Please try again.")




