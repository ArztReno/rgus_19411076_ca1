# date : 13/11/2020
# Author : Renato Gusani
# Student no. : x19411076
# Question : 1a

# To work with JSON or CSV, I need to import these module before I can use them.
import json
import csv

# Function to open the JSON file with exception handling clauses.
try:
    f = open("c:/Users/renat/Documents/BSc. (Honours) in Data Science/Year 2/Semester 1/Programming II/CA/Programs/DublinAirport090220.json")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print ('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing File...")


# printing certain attributes from the JSON file
with open("c:/Users/renat/Documents/BSc. (Honours) in Data Science/Year 2/Semester 1/Programming II/CA/Programs/DublinAirport090220.json", 'r') as f:
    DublinAirport090220_dict = json.load(f)

# Printing the Temperature attribute in the JSON file
for temperature in DublinAirport090220_dict:
    print(temperature['temperature'])

# Printing the weatherDescription attribute in the JSON file
for weatherDescription in DublinAirport090220_dict:
    print(weatherDescription['weatherDescription'])

# Printing the reportTimeattribute in the JSON file
for reportTime in DublinAirport090220_dict:
    print(reportTime['reportTime'])

# Converting data above to CSV
with open ("c:/Users/renat/Documents/BSc. (Honours) in Data Science/Year 2/Semester 1/Programming II/CA/Programs/DublinAirport090220.json", 'r') as file:
    data = json.load(file)

fname  = "output.csv"

with open (fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["temperature", "weatherDescription", "reportTime"])
    for item in data ["result"]:
        csv_file.writerow([item['temperature'], item['weatherDescription', ['reportTime']]])