# import the necessary libraries

import pandas as pd  # this is for data processing with dataframes
import numpy as np   # this is for various number things like the random choice and the zeros array
import time
from team_path_map import BracketMap    # this allows us to access the data in the other file


def weighted_choice(sequence,  weights):
    x = np.random.randint(0,1e8)
    weights = [weight*1e8 for weight in weights]
    weights_dict = {el: prob for (el, prob) in zip(sequence, weights)}

    place = 0
    for el, prob in weights_dict.items():

        place = place + prob

        if place > x:
            return el



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
for i in range(1):


    # loop that iterates through the empty games
    # create empty bracket
    bracket = list(np.zeros(63))
    print(bracket)
    full = False
    while not full:
        game = bracket.index(0) + 1 # because of zero indexing

        # makes list of all teams playing in game
        possible_teams = [team for team in path_data.map_dict if game in path_data.map_dict[team]]

        # Find the round
        one_team = possible_teams[0]                # pick a random team from the possible ones (the first one)
        that_map = path_data.map_dict[one_team]     # get the map of that team
        round = that_map.index(game) + 2            # all teams

        # the probabilites of each of the teams winning in this round
        probabilities = list(round_wins_named['rd{}_win'.format(round)][possible_teams])

        # choose winner of game
       # winner = np.random.choice(possible_teams, 2, p=probabilities)[0]
        winner = weighted_choice(possible_teams, probabilities)

        # fill in upstream games with this winner
        games = path_data.map_dict[winner]
        for gam in games:
            if bracket[gam-1] == 0:
                bracket[gam-1] = winner

        # decide whether or not the bracket is full
        if 0 not in bracket:
            full = True


    bracket_frame = pd.DataFrame([bracket])
    #print(bracket_frame)
    brackets = brackets.append(bracket_frame)

print(brackets)
print('done')

# ********Score user bracket**********

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


def user_bracket_score(espn_bracket, user_bracket):
    score = 0
    for i in range(0,len(espn_bracket)-1):
        if espn_bracket[i] == user_bracket[i]:
            game = i+1
            score = score + get_score(game)

    return score

#
people = ["hudson", "nick"]
from hudsons_bracket import hudsons_bracket
from nicks_bracket import nicks_bracket



espn_bracket = ['Duke', 'Duke', 'Louisville', 'Duke', "Saint Mary's (CA)", 'Louisville', 'Wichita State', 'Villanova', 'Duke', 'Gonzaga', "Saint Mary's (CA)", 'Iowa State', 'Louisville', 'North Carolina', 'Wichita State', 'Villanova', 'Virginia', 'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State', "Saint Mary's (CA)", 'Kansas', 'Iowa State', 'Oregon', 'Louisville', 'North Carolina', 'Butler', 'UCLA', 'Wichita State', 'Villanova', 'Virginia Tech', 'Virginia', 'East Tennessee State', 'Southern Methodist', 'Baylor', 'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Maryland', 'Florida State', "Saint Mary's (CA)", 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue', 'Creighton', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Middle Tennessee', 'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky']

for j in range (0,iterations):
    score = 0
    for i in range(0,63):
        if espn_bracket[i] == brackets.iloc[i,j]:
            game = i
            score = score + get_score(game)
    print('Player earned a score of')

