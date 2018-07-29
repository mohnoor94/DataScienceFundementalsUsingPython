# Data Science is... just counting! but counting is very powerful.
# social search / recommendation system
# Goal: Aid users in their discovery if relevant listings

# IMPORTANT:
# please download data from
# http://data.insideairbnb.com/united-states/wa/seattle/2018-05-17/data/reviews.csv.gz
# and rename the file to 'seattle_reviews_17May2018.csv'
# then save it to '../data/airbnb/' directory
# before executing 'lesson2_data_science_process/processing_airbnb_reviews.py' example.

import csv

csvFile = open('../data/airbnb/seattle_reviews_17May2018.csv', newline='')
# print(type(csvFile))

reader = csv.reader(csvFile)
headers = next(reader)  # generator of the file, does not load entire file into memory
records = list(reader)  # in memory data structure

# rows = 0
# for row in records:
#     rows += 1

rows = len(records)
# print(rows)

# rowWithHeader = list(zip(headers, records[0]))  # zip 2 lists to a list of tuples
# print(rowWithHeader)

randomUserId = '677093'
randomUserReviews = []
for row in records:
    if row[3] == randomUserId:
        randomUserReviews.append(row)
# print(randomUserReviews)

# map, then map list to set (no duplications, constant lookups)
listings = set([review[0] for review in randomUserReviews])
# print(listings)

# find all other listing that the other guests have stayed at
# 1. find every other guest who stayed in the listings I stayed
fellowTravelers = set()
for row in records:
    if row[0] in listings:
        fellowTravelers.add(row[3])
# print(len(fellowTravelers))

# 2. for these fellow travellers, find the other listings
# we need duplications here, the more fellows stayed at the same listing the better to recommend it!
fellowListings = []
for row in records:
    if row[3] in fellowTravelers:
        fellowListings.append(row[0])
# print(len(fellowListings))

# The idea of 'Triangle Closing'
# on social media platforms -> a friend of my friends will LIKELY be my friend!
# for our case -> a listing (with the same guests) of my bookings will LIKELY be my (future) booking!

