# import the necessary libraries

import pandas as pd  # this is for data processing with dataframes
import numpy as np  # this is for various number things like the random choice and the zeros array
import time
from team_path_map import BracketMap  # this allows us to access the data in the other file


def weighted_choice(sequence, weights):
    x = np.random.randint(0, 1e8)
    weights = [weight * 1e8 for weight in weights]
    weights_dict = {el: prob for (el, prob) in zip(sequence, weights)}

    place = 0
    for el, prob in weights_dict.items():

        place = place + prob

        if place > x:
            return el


def get_score(game):
    if game == 0:
        return 32
    elif game <= 2:
        return 16
    elif game <= 6:
        return 8
    elif game <= 14:
        return 4
    elif game <= 30:
        return 2
    else:
        return 1


# ******** Prep Data *****************

# Creates an instance of the class described in team_path_map, giving us access to all the map data.
path_data = BracketMap()

# load the data and take only the columns we need.
all_forecast_data = pd.read_csv('./fivethirtyeight_ncaa_forecasts.csv')
round_wins_all = all_forecast_data[['rd1_win', 'rd2_win', 'rd3_win', 'rd4_win', 'rd5_win', 'rd6_win', 'rd7_win']]
round_wins = round_wins_all[136: 200]
team_names = all_forecast_data['team_name'][136:200]
round_wins_named = round_wins.set_index(team_names)

# ******** Algorithm ****************

brackets = pd.DataFrame()
# loop that runs 10,000 iterations
iterations = 1000
for i in range(iterations):

    # loop that iterates through the empty games
    # create empty bracket
    bracket = list(np.zeros(63))
    # print(bracket)
    full = False
    while not full:
        game = bracket.index(0) + 1  # because of zero indexing

        # makes list of all teams playing in game
        possible_teams = [team for team in path_data.map_dict if game in path_data.map_dict[team]]

        # Find the round
        one_team = possible_teams[0]  # pick a random team from the possible ones (the first one)
        that_map = path_data.map_dict[one_team]  # get the map of that team
        round = that_map.index(game) + 2  # all teams

        # the probabilites of each of the teams winning in this round
        probabilities = list(round_wins_named['rd{}_win'.format(round)][possible_teams])

        # choose winner of game
        # winner = np.random.choice(possible_teams, 2, p=probabilities)[0]
        winner = weighted_choice(possible_teams, probabilities)

        # fill in upstream games with this winner
        games = path_data.map_dict[winner]
        for gam in games:
            if bracket[gam - 1] == 0:
                bracket[gam - 1] = winner

        # decide whether or not the bracket is full
        if 0 not in bracket:
            full = True

    bracket_frame = pd.DataFrame([bracket])
    brackets = brackets.append(bracket_frame, ignore_index=True)
    # print(bracket_frame)

# print(brackets)
print('done')

# ********Score user bracket**********


# Making a dictionary of all the brackets
y_brackets = {
    'hudson': ['Gonzaga', 'Gonzaga', 'Kansas', 'Villanova', 'Gonzaga', 'Kansas', 'UCLA', 'Villanova', 'Baylor',
               'Gonzaga', 'Arizona', 'Kansas', 'Louisville', 'Minnesota', 'UCLA', 'Villanova',
               'North Carolina-Wilmington', 'Baylor', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State', 'Arizona',
               'Kansas', 'Purdue', 'Oregon', 'Louisville', 'North Carolina', 'Minnesota', 'UCLA', 'Kentucky',
               'Villanova', 'Virginia Tech', 'North Carolina-Wilmington', 'Florida', 'Southern Methodist', 'Baylor',
               'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Xavier', 'Florida State',
               'Virginia Commonwealth', 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue', 'Rhode Island',
               'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Minnesota', 'Butler', 'Cincinnati',
               'UCLA', 'Wichita State', 'Kentucky'],
    'nick': ['Florida', 'Florida', 'Kansas', 'Florida', 'Gonzaga', 'Kansas', 'North Carolina', 'Florida', 'Duke',
             'Gonzaga', 'Florida State', 'Kansas', 'Louisville', 'North Carolina', 'Kentucky', 'Villanova', 'Florida',
             'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State', 'Arizona', 'Kansas',
             'Iowa State', 'Creighton', 'Louisville', 'North Carolina', 'Butler', 'Cincinnati', 'Kentucky', 'Villanova',
             'Wisconsin', 'North Carolina-Wilmington', 'Florida', 'Southern Methodist', 'Baylor', 'Marquette', 'Duke',
             'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Xavier', 'Florida State', 'Virginia Commonwealth',
             'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue', 'Creighton', 'Oregon', 'Michigan', 'Louisville',
             'North Carolina', 'Arkansas', 'Middle Tennessee', 'Butler', 'Cincinnati', 'UCLA', 'Wichita State',
             'Kentucky'],
    'nate': ['Duke', 'Duke', 'Louisville', 'Duke', "Saint Mary's (CA)", 'Louisville', 'Wichita State', 'Villanova',
             'Duke', 'Gonzaga', "Saint Mary's (CA)", 'Iowa State', 'Louisville', 'North Carolina', 'Wichita State',
             'Villanova', 'Virginia', 'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State',
             "Saint Mary's (CA)", 'Kansas', 'Iowa State', 'Oregon', 'Louisville', 'North Carolina', 'Butler', 'UCLA',
             'Wichita State', 'Villanova', 'Virginia Tech', 'Virginia', 'East Tennessee State', 'Southern Methodist',
             'Baylor', 'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Maryland',
             'Florida State', "Saint Mary's (CA)", 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue',
             'Creighton', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Middle Tennessee',
             'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky'],
    'Dr. I': ['Duke', 'Duke', 'Louisville', 'Duke', "Saint Mary's (CA)", 'Louisville', 'Wichita State', 'Villanova',
              'Duke', 'Gonzaga', "Saint Mary's (CA)", 'Iowa State', 'Louisville', 'North Carolina', 'Wichita State',
              'Villanova', 'Virginia', 'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State',
              "Saint Mary's (CA)", 'Kansas', 'Iowa State', 'Oregon', 'Louisville', 'North Carolina', 'Butler', 'UCLA',
              'Wichita State', 'Villanova', 'Virginia Tech', 'Virginia', 'East Tennessee State', 'Southern Methodist',
              'Baylor', 'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Maryland',
              'Florida State', "Saint Mary's (CA)", 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue',
              'Creighton', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Middle Tennessee',
              'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky'],
    'Dr. Ryken': ['Villanova', 'Villanova', 'Kansas', 'Villanova', 'Arizona', 'Kansas', 'Kentucky', 'Villanova',
                  'Southern Methodist', 'Vanderbilt', 'Arizona', 'Kansas', 'Louisville', 'Butler', 'Kentucky',
                  'Villanova', 'Virginia', 'Southern Methodist', 'Duke', 'Vanderbilt', 'Notre Dame', 'Florida State',
                  'Arizona', 'Kansas', 'Nevada', 'Oregon', 'Louisville', 'North Carolina', 'Butler', 'UCLA', 'Kentucky',
                  'Villanova', 'Wisconsin', 'Virginia', 'Florida', 'Southern Methodist', 'Baylor', 'South Carolina',
                  'Duke', 'South Dakota State', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Xavier', 'Florida State',
                  'Virginia Commonwealth', 'Arizona', 'Kansas', 'Miami (FL)', 'Nevada', 'Vermont', 'Rhode Island',
                  'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Minnesota', 'Butler', 'Cincinnati',
                  'UCLA', 'Wichita State', 'Kentucky']}

user_brackets = pd.DataFrame(y_brackets)  # Convert the dictionary to a dataframe

user_names = list(user_brackets)  # Make a list that contains the name of each player

kmax = len(user_brackets.columns)  # number of users

bracket_scores = pd.DataFrame(index=np.arange(iterations),
                              columns=user_names)  # Initializing a data frame to fill with user's scores
# K is the user bracket number
# J is the simulated bracket number
# I is the game number
for k in range(0, kmax):  # Iterate through each person's bracket one at a time
    for j in range(0, iterations):  # Iterate through each simulated bracket one at a time
        score = 0
        for i in range(0, 62):  # Iterate through each game
            if user_brackets.iloc[i, k] == brackets.iloc[j, i]:
                game = i
                score = score + get_score(game)

        bracket_scores.iloc[j, k] = score  # Need to store each users score in a DataFrame with the other users.

num_of_wins = pd.DataFrame(index=['# of wins', 'Total score', 'Average score', 'Probability of win'],
                           columns=user_names)  # Make a dataframe to store how many times each person won

for k in range(0, kmax):  # Iterate through each person's bracket one at a time
    wins = 0
    for j in range(0, iterations):  # Iterate through each simulated bracket one at a time
        if bracket_scores.iloc[j, k] == bracket_scores.iloc[j].max():
            wins = wins + 1
    num_of_wins.iloc[0, k] = wins  # fill in the total number of wins
    num_of_wins.iloc[1, k] = np.sum(bracket_scores.iloc[:, k])  # fill in the sum of the wins
    num_of_wins.iloc[2, k] = np.average(bracket_scores.iloc[:, k])  # average score

for k in range(0, kmax):  # Assign probabilities
    num_of_wins.iloc[3, k] = num_of_wins.iloc[0, k] / np.sum(num_of_wins.iloc[0, :])  # Probability of person winning the bracket pool
