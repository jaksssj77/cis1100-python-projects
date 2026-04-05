"""
Name: Jax Jiang
PennKey: jiang13
Recitation: 201
Program Execution: python food_recommender_main.py restaurants.csv
Description: The program loads restaurant data from a CSV file and allows
             users to filter restaurants based on distance, TA endorsements,
             and cuisine type, as well as returning the most recommended
             restaurant for each cuisine.
"""

RestaurantInfo = tuple[str, int, float, int]


def load_restaurant_csv(
    filename: str,
) -> dict[str, RestaurantInfo]:
    """
    Description: loads the data from the specified
    csv file. The CSV file should have the expected restaurant format.
    Returns a dictionary mapping restaurant names to tuples containing
    the cuisine, price, distance and number of endorsements for that
    restaurant.

    Input: str, representing the name of a file containing restaurant data

    Output: dictionary of tuples representing restaurants
    """

    # creates a dict
    restaurants = dict()

    # open and read the file
    file = open(filename, "r")
    file.readline()

    for line in file:
        line = line.strip()
        line_parts = line.split(",")

        name = line_parts[0]
        cuisine = line_parts[1]
        price = len(line_parts[2])
        distance = float(line_parts[3])
        endorsements = int(line_parts[4])

        # add each restaurant and its info to the dict
        restaurants[name] = (cuisine, price, distance, endorsements)

    # close the file
    file.close()

    # return the dict
    return restaurants


def get_cuisines(
    restaurants: dict[str, RestaurantInfo],
) -> set[str]:
    """
    Description: Returns a set containing all unique cuisines from the
                 restaurants dictionary

    Input: restaurants: a dictionary mapping restaurant names to tuples
           containing (cuisine, price, distance, endorsements).

    Output: A set of strings representing all cuisines available in the
            restaurants data.
    """

    # creates a set
    cuisines_set = set()

    # stores each unique cuisine into the set
    for v in restaurants.values():
        cuisine = v[0]
        cuisines_set.add(cuisine)

    # returns the set
    return cuisines_set


def max_distance(
    restaurants: dict[str, RestaurantInfo], dist: float
) -> set[str]:
    """
    Description: Returns the names of restaurants whose distance is less
                 than or equal to the input dist

    Input: restaurants: dictionary mapping restaurant names
           to restaurant info tuples
           dist: maximum allowed distance

    Output: A set of restaurant names within the given distance
    """

    # creates a set
    res = set()

    # stores name of restaurant which fulfills requirement in the set
    for k, v in restaurants.items():
        if v[2] <= dist:
            res.add(k)

    # returns the set
    return res


def ta_endorsements(
    restaurants: dict[str, RestaurantInfo], min_rating: int
) -> set[str]:
    """
    Description: Returns the names of restaurants whose TA endorsement count
                 is greater than or equal to the given minimum rating

    Input: restaurants: dictionary mapping restaurant names to restaurant
           info tuples
           min_rating: minimum number of endorsements required

    Output: A set of restaurant names that meet the endorsement requirement
    """

    # creates a set
    res = set()

    # stores name of restaurant which fulfills requirement in the set
    for k, v in restaurants.items():
        if v[3] >= min_rating:
            res.add(k)

    # returns the set
    return res


def filter_cuisine(
    restaurants: dict[str, RestaurantInfo], cuisine: str
) -> set[str]:
    """Description: Returns the names of restaurants that serve the
                    specified cuisine. The comparison ignores differences
                    in letter case

    Input: restaurants: dictionary mapping restaurant names to restaurant
           info tuples
           cuisine: the cuisine type to filter for

    Output: A set of restaurant names that serve the specified cuisine
    """

    # creates a set
    res = set()
    cuisine = cuisine.lower()

    # stores name of restaurant which fulfills requirement in the set
    for k, v in restaurants.items():
        each_cuisine = v[0].lower()
        if each_cuisine == cuisine:
            res.add(k)

    # returns the set
    return res


def most_recommended_diverse(
    restaurants: dict[str, RestaurantInfo],
) -> set[str]:
    """
    Description: Returns a set containing the most endorsed restaurant for
                 each cuisine. If two restaurants in the same cuisine tie
                 for endorsements, the one found first is kept

    Input: restaurants: dictionary mapping restaurant names to restaurant
           info tuples

    Output: A set of restaurant names, one per cuisine, with the highest
            endorsements
    """

    # creates a dict
    best = dict()

    # stores wanted names of restaurants in the dict
    for k, v in restaurants.items():
        cuisine = v[0]
        endorsements = v[3]

        if cuisine not in best:
            best[cuisine] = (k, endorsements)
        else:
            current_name, current_endorsements = best[cuisine]
            if endorsements > current_endorsements:
                best[cuisine] = (k, endorsements)

    res = set()
    for cuisine in best:
        res.add(best[cuisine][0])

    # returns the dict
    return res
