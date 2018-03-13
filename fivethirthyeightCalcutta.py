# import the necessary libraries
import pandas as pd  # this is for data processing with dataframes
import numpy as np   # this is for various number things like the random choice and the zeros array
import datetime
from team_path_map import BracketMap    # this allows us to access the data in the other file

# load the data and take only the columns we need.
all_forecast_data = pd.read_csv('Users/nickvarberg/Downloads/fivethirtyeight_ncaa_forecasts_2018.csv')
date = "2017-03-15"
gender = "mens"
correct_date_gender_data = all_forecast_data[all_forecast_data['forecast_date'].str.match(date) & all_forecast_data['gender'].str.match(gender) & (all_forecast_data['rd1_win'] !=0)]
round_wins = correct_date_gender_data[['rd1_win', 'rd2_win', 'rd3_win', 'rd4_win', 'rd5_win', 'rd6_win', 'rd7_win']]
round_wins_named = round_wins.set_index(correct_date_gender_data['team_name'])