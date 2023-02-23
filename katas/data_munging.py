import re

import pandas as pd


def get_smallest_spread(first_series, second_series):
    first_series_cleaned = first_series.apply(_remove_non_alphanumeric)
    second_series_cleaned = second_series.apply(_remove_non_alphanumeric)

    spread_series = abs(
        first_series_cleaned.astype(float) - second_series_cleaned.astype(float)
    )
    minimum_spread = spread_series.dropna().min()

    return spread_series.tolist().index(minimum_spread)


def _remove_non_alphanumeric(text):
    try:
        pattern = re.compile("\W")
        return re.sub(pattern, "", text)
    except:
        return text


# reading the data
weather_data = pd.read_fwf("/Users/isabel/Downloads/weather.dat", sep=" ")
football_data = pd.read_fwf("/Users/isabel/Downloads/football.dat", sep=" ").drop(
    columns=["Unnamed: 0", "Unnamed: 7"]
)

print(
    "The day with the smallest spread between highest and lowest temperatures is: {}".format(
        get_smallest_spread(weather_data["MxT"], weather_data["MnT"])
    )
)
print(
    "The football team with the smallest spread between for and against goals is: {}".format(
        get_smallest_spread(football_data["F"], football_data["A"])
    )
)
