#!/usr/bin/env python3
# Purpose: Convert the CSV file to a SQLite database.
# Author: Abdallah Abdelazim
# Features:
# - Convert the CSV file to a SQLite database.
# - The input CSV file is expected to be in the same folder as this script.
# - The output SQLite database is named 'quran.db'.
# - The output SQLite database is saved to the same folder as this script.
# Pre-requisites:
# - Python 3.6 or higher.
# - SQLite package (pip install db-sqlite3).
#
import os
import sqlite3
import csv

# Open the CSV file and read the data
script_folder = os.path.dirname(__file__)
csv_file = os.path.join(script_folder, "data.csv")
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Connect to the database (creates a new database if it doesn't exist)
quran_db = os.path.join(script_folder, "quran.db")
conn = sqlite3.connect(quran_db)

# Create a table with the same columns as the CSV file
columns = data[0]
query = 'CREATE TABLE ayas ({})'.format(', '.join(columns))
cursor = conn.cursor()
cursor.execute(query)

# Insert the data into the table
for row in data[1:]:
    query = 'INSERT INTO ayas ({}) VALUES ({})'.format(
        ', '.join(columns),
        ', '.join(['?']*len(columns))
    )
    cursor.execute(query, row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Done!")
