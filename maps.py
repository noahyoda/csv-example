import json
import csv

# read json file
file = open('sandiego_data.json')
jdata = json.load(file)

# variables to label file with
vars = ['Name', 'Rating', 'Reviews', 'Cost']

# open csv we are creating
with open('sd.csv', 'a', newline='') as csvfile:
    # write variables to file head
    writer = csv.writer(csvfile)
    writer.writerow(vars)

    # iterate over json and write to csv
    for i in jdata:
        try:
            cost = i['price'].count('$')
        except:
            cost = "NA"
        curr = [i['title'], i['totalScore'], i['reviewsCount'], cost]
        writer.writerow(curr)

file.close()