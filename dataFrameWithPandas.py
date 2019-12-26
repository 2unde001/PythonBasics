import pandas as pd

# Get the csv path
weather_path = "PythonBasics\weather-stations.csv"
# assign the path to read_csv function
df = pd.read_csv(weather_path)
#print the first five rows 
print(df.head())

# Create a dataframe from a dictionary

songs = {
    "Album": ["Thriller", "Back in Black", "The Dark Side of the Moon", \
    "The Bodyguard", "Bat Out of Hell"],
    "Released": [1982, 1980, 1973, 1992, 1977],
    "Length":["00:42:19", "00:42:11", "00:42:49", "00:57:44", "00:46:33"]

}

songs_frame = pd.DataFrame(songs)
print(songs_frame)

# Create a new dataframe
# y = df[["Artist", "Genre"]]
# print(y)
