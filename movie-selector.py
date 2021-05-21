import csv

with open('movie-list2.csv') as f:
    movies = csv.DictReader(f)
    #for row in movies:
    #    print(row['title'])