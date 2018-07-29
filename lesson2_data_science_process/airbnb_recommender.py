# Goal: Aid users in their discovery if relevant listings

import csv
import collections as coll

# open and parse csv files
reviews_file = open('../data/airbnb/seattle_reviews_17May2018.csv', newline='')
listings_file = open('../data/airbnb/seattle_listings_17May2018.csv', newline='')

reviews_reader = csv.reader(reviews_file)
listings_reader = csv.reader(listings_file)

reviews_headers = next(reviews_reader)
listings_headers = next(listings_reader)

reviews_records = list(reviews_reader)
listings_records = list(listings_reader)

# set user for recommendations
randomUserId = '677093'


def find_listings(records, user_id):
    listings = set()

    # find listings of user
    for row in records:
        if row[3] == user_id:
            listings.add(row[0])

    return listings


def find_travelers(records, listings):
    fellow_travelers = set()

    # find fellow travelers
    for row in records:
        if row[0] in listings:  # row[0] => listing_id
            fellow_travelers.add(row[3])  # row[3] => reviewer_id

    return fellow_travelers


def count_triangles(records, fellow_travelers):
    triangles = []

    # find triangles user is part of
    for row in records:
        if row[3] in fellow_travelers:
            triangles.append(row[0])

    return coll.Counter(triangles)


def recommend_listings(counts, user_listings, number_of_recommendations=10):
    for listing in user_listings:
        if listing in counts:
            counts.pop(listing)

    return counts.most_common(number_of_recommendations)


# get the baseline (most popular) listings, in the case we don't have a good number of user recommendations!
def get_baseline():
    records = [(row[0], row[76]) for row in listings_records]
    ratings = [(tup[0], float(tup[1])) for tup in records if tup[1] != '']
    popular_listings = sorted(ratings, key=lambda x: x[1], reverse=True)
    return popular_listings


def get_top_popular_listings(number_of_listings=10):
    return get_baseline()[:number_of_listings]


# the final recommender method
def recommend(user_id, number_of_recommendations=10):
    custom_recommendation_number = int(0.7 * number_of_recommendations)
    custom_listings = find_listings(reviews_records, user_id)
    fellow_travelers = find_travelers(reviews_records, custom_listings)
    counts = count_triangles(reviews_records, fellow_travelers)
    recommendations = recommend_listings(counts, custom_listings, number_of_recommendations)
    popularity_recommendation_number = abs(custom_recommendation_number - len(recommendations))
    recommendations.extend(get_top_popular_listings(popularity_recommendation_number))
    return recommendations
