import csv
RESULTS = [
    ['apple','cherry','orange','pineapple','strawberry']
]

cool = [['boy','cool']]
with open("output.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(RESULTS)
    wr.writerows(cool)
