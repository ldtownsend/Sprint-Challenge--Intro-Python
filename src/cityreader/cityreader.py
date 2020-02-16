# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City():
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = float(lat)
    self.lon = float(lon)

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

import csv
cities = []

def cityreader(cities=[]):
  with open('cities.csv', mode='r') as file_csv:
    data = csv.reader(file_csv)
    next(data)
    for row in data:
      cities.append(City(row[0], row[3], row[4]))
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f"{c.name}, {c.lat}, {c.lon}")

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within

expected = [
  City("Seattle", 47.6217,-122.3238),
  City("Richmond", 37.5294,-77.4755),
  City("Virginia Beach", 36.7335,-76.0435),
  City("Washington", 38.9047,-77.0163),
  City("Milwaukee", 43.064,-87.9669),
  City("Orlando", 28.4801,-81.3448),
  City("Miami", 25.784,-80.2102),
  City("Tampa", 27.9937,-82.4454),
  City("Jacksonville", 30.3322,-81.6749),
  City("Albuquerque", 35.1055,-106.6476),
  City("Fort Worth", 32.7813,-97.3466),
  City("McAllen", 26.2203,-98.2457),
  City("El Paso", 31.8478,-106.431),
  City("Dallas", 32.7938,-96.7659),
  City("Austin", 30.3038,-97.7545),
  City("Houston", 29.7871,-95.3936),
  City("San Antonio", 29.4722,-98.5247),
  City("New Orleans", 30.0687,-89.9288),
  City("Charlotte", 35.208,-80.8308),
  City("Raleigh", 35.8323,-78.6441),
  City("Omaha", 41.2634,-96.0453),
  City("Memphis", 35.1047,-89.9773),
  City("Nashville", 36.1714,-86.7844),
  City("Buffalo", 42.9016,-78.8487),
  City("Queens", 40.7498,-73.7976),
  City("New York", 40.6943,-73.9249),
  City("Bronx", 40.8501,-73.8662),
  City("Brooklyn", 40.6501,-73.9496),
  City("Manhattan", 40.7834,-73.9662),
  City("Philadelphia", 40.0076,-75.134),
  City("Pittsburgh", 40.4396,-79.9763),
  City("Sacramento", 38.5666,-121.4683),
  City("Riverside", 33.9382,-117.3949),
  City("San Francisco", 37.7561,-122.4429),
  City("San Diego", 32.8312,-117.1225),
  City("San Jose", 37.302,-121.8488),
  City("Los Angeles", 34.114,-118.4068),
  City("Las Vegas", 36.2288,-115.2603),
  City("Denver", 39.7621,-104.8759),
  City("Chicago", 41.8373,-87.6861),
  City("Atlanta", 33.7627,-84.4231),
  City("Indianapolis", 39.7771,-86.1458),
  City("Oklahoma City", 35.4677,-97.5138),
  City("Phoenix", 33.5722,-112.0891),
  City("Tucson", 32.1558,-110.8777),
  City("Bridgeport", 41.1909,-73.1958),
  City("Hartford", 41.7661,-72.6834),
  City("Baltimore", 39.3051,-76.6144),
  City("Boston", 42.3189,-71.0838),
  City("Cleveland", 41.4766,-81.6805),
  City("Columbus", 39.9859,-82.9852),
  City("Cincinnati", 39.1412,-84.506),
  City("Salt Lake City", 40.7774,-111.9301),
  City("Saint Louis", 38.6358,-90.2451),
  City("Kansas City", 39.1239,-94.5541),
  City("Minneapolis", 44.9635,-93.2679),
  City("Detroit", 42.3834,-83.1024),
  City("Providence", 41.8229,-71.4186),
  City("Louisville", 38.1662,-85.6488),
  City("Portland", 45.5372,-122.65)
]

print(len(expected))
print(len(cities))

