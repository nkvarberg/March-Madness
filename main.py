# import the necessary libraries

import pandas as pd  # this is for data processing with dataframes
import numpy as np   # this is for various number things like the random choice and the zeros array

from team_path_map import BracketMap    # this allows us to access the data in the other file


# ******** Prep Data *****************

# Creates an instance of the class described in team_path_map, giving us access to all the map data.
path_data = BracketMap()

# load the data and take only the columns we need.
all_forecast_data = pd.read_csv('./fivethirtyeight_ncaa_forecasts.csv')
round_wins_all = all_forecast_data[['rd1_win', 'rd2_win', 'rd3_win', 'rd4_win', 'rd5_win', 'rd6_win', 'rd7_win']]
round_wins = round_wins_all[69: 136]
team_names = all_forecast_data['team_name']

# create empty bracket
bracket = np.zeros(63)

# ******** Algorithm ****************

# loop that runs 10,000 iterations

# loop that iterates through the empty games

# choose winner of championship
winner = np.random.choice(team_names, 1, p=round_wins[:, 7])

games = path_data.map_dict[winner]

for game in games:
    bracket[game] = winner







