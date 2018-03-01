# import the necessary libraries

import pandas as pd  # this is for data processing with dataframes
import numpy as np   # this is for various number things like the random choice and the zeros array
import datetime
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
date = "2017-03-15"
#date = datetime.datetime.now().strftime("%Y-%m-%d")

gender = "mens"
correct_date_gender_data = all_forecast_data[all_forecast_data['forecast_date'].str.match(date) & all_forecast_data['gender'].str.match(gender) & (all_forecast_data['rd1_win'] !=0)]
round_wins = correct_date_gender_data[['rd1_win', 'rd2_win', 'rd3_win', 'rd4_win', 'rd5_win', 'rd6_win', 'rd7_win']]
round_wins_named = round_wins.set_index(correct_date_gender_data['team_name'])

my_brackets = pd.DataFrame({'hudson':  ['Gonzaga', 'Gonzaga', 'Kansas', 'Villanova', 'Gonzaga', 'Kansas', 'UCLA', 'Villanova', 'Baylor', 'Gonzaga', 'Arizona', 'Kansas', 'Louisville', 'Minnesota', 'UCLA', 'Villanova', 'North Carolina-Wilmington', 'Baylor', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State', 'Arizona', 'Kansas', 'Purdue', 'Oregon', 'Louisville', 'North Carolina', 'Minnesota', 'UCLA', 'Kentucky', 'Villanova', 'Virginia Tech', 'North Carolina-Wilmington', 'Florida', 'Southern Methodist', 'Baylor', 'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Xavier', 'Florida State', 'Virginia Commonwealth', 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue', 'Rhode Island', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Minnesota', 'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky'],
               'nick':  ['Florida', 'Florida', 'Kansas', 'Florida', 'Gonzaga', 'Kansas', 'North Carolina', 'Florida', 'Duke', 'Gonzaga', 'Florida State', 'Kansas', 'Louisville', 'North Carolina', 'Kentucky', 'Villanova', 'Florida', 'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State', 'Arizona', 'Kansas', 'Iowa State', 'Creighton', 'Louisville', 'North Carolina', 'Butler', 'Cincinnati', 'Kentucky', 'Villanova', 'Wisconsin', 'North Carolina-Wilmington', 'Florida', 'Southern Methodist', 'Baylor', 'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Xavier', 'Florida State', 'Virginia Commonwealth', 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue', 'Creighton', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Middle Tennessee', 'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky'],
                            'snate': ['Duke', 'Duke', 'Louisville', 'Duke', "Saint Mary's (CA)", 'Louisville',
                                     'Wichita State', 'Villanova', 'Duke', 'Gonzaga', "Saint Mary's (CA)", 'Iowa State',
                                     'Louisville', 'North Carolina', 'Wichita State', 'Villanova', 'Virginia',
                                     'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State',
                                     "Saint Mary's (CA)", 'Kansas', 'Iowa State', 'Oregon', 'Louisville',
                                     'North Carolina', 'Butler', 'UCLA', 'Wichita State', 'Villanova', 'Virginia Tech',
                                     'Virginia', 'East Tennessee State', 'Southern Methodist', 'Baylor', 'Marquette',
                                     'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Maryland',
                                     'Florida State', "Saint Mary's (CA)", 'Arizona', 'Kansas', 'Miami (FL)',
                                     'Iowa State', 'Purdue', 'Creighton', 'Oregon', 'Michigan', 'Louisville',
                                     'North Carolina', 'Arkansas', 'Middle Tennessee', 'Butler', 'Cincinnati', 'UCLA',
                                     'Wichita State', 'Kentucky'],

                            'nate':  ['Duke', 'Duke', 'Louisville', 'Duke', "Saint Mary's (CA)", 'Louisville', 'Wichita State', 'Villanova', 'Duke', 'Gonzaga', "Saint Mary's (CA)", 'Iowa State', 'Louisville', 'North Carolina', 'Wichita State', 'Villanova', 'Virginia', 'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State', "Saint Mary's (CA)", 'Kansas', 'Iowa State', 'Oregon', 'Louisville', 'North Carolina', 'Butler', 'UCLA', 'Wichita State', 'Villanova', 'Virginia Tech', 'Virginia', 'East Tennessee State', 'Southern Methodist', 'Baylor', 'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Maryland', 'Florida State', "Saint Mary's (CA)", 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue', 'Creighton', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Middle Tennessee', 'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky'],
               'Dr. I':  ['Duke', 'Duke', 'Louisville', 'Duke', "Saint Mary's (CA)", 'Louisville', 'Wichita State', 'Villanova', 'Duke', 'Gonzaga', "Saint Mary's (CA)", 'Iowa State', 'Louisville', 'North Carolina', 'Wichita State', 'Villanova', 'Virginia', 'Southern Methodist', 'Duke', 'Gonzaga', 'West Virginia', 'Florida State', "Saint Mary's (CA)", 'Kansas', 'Iowa State', 'Oregon', 'Louisville', 'North Carolina', 'Butler', 'UCLA', 'Wichita State', 'Villanova', 'Virginia Tech', 'Virginia', 'East Tennessee State', 'Southern Methodist', 'Baylor', 'Marquette', 'Duke', 'Gonzaga', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Maryland', 'Florida State', "Saint Mary's (CA)", 'Arizona', 'Kansas', 'Miami (FL)', 'Iowa State', 'Purdue', 'Creighton', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Middle Tennessee', 'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky'],
               'Dr. Ryken': ['Villanova', 'Villanova', 'Kansas', 'Villanova', 'Arizona', 'Kansas', 'Kentucky', 'Villanova', 'Southern Methodist', 'Vanderbilt', 'Arizona', 'Kansas', 'Louisville', 'Butler', 'Kentucky', 'Villanova', 'Virginia', 'Southern Methodist', 'Duke', 'Vanderbilt', 'Notre Dame', 'Florida State', 'Arizona', 'Kansas', 'Nevada', 'Oregon', 'Louisville', 'North Carolina', 'Butler', 'UCLA', 'Kentucky', 'Villanova', 'Wisconsin', 'Virginia', 'Florida', 'Southern Methodist', 'Baylor', 'South Carolina', 'Duke', 'South Dakota State', 'Vanderbilt', 'Notre Dame', 'West Virginia', 'Xavier', 'Florida State', 'Virginia Commonwealth', 'Arizona', 'Kansas', 'Miami (FL)', 'Nevada', 'Vermont', 'Rhode Island', 'Oregon', 'Michigan', 'Louisville', 'North Carolina', 'Arkansas', 'Minnesota', 'Butler', 'Cincinnati', 'UCLA', 'Wichita State', 'Kentucky']})

results = pd.DataFrame(index=['total_points', 'wins', 'average_score', 'win_perc'], columns=my_brackets.columns)
results = results.fillna(0)

num_sims = 1000

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


def user_bracket_score(espn_bracket, player_bracket):
    states = espn_bracket == player_bracket
    true_index = np.where(states)[0]
    player_score = 0
    for game in true_index:
        player_score = player_score + get_score(game)
    return player_score


# ******** Algorithm ****************

brackets = pd.DataFrame()
# loop that runs 10,000 iterations
for i in range(num_sims):


    # loop that iterates through the empty games
    # create empty bracket
    bracket = list(np.zeros(63))
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
        full = 0 not in bracket


    # score each player for the current bracket
    player_score = {player: user_bracket_score(bracket, my_brackets[player]) for player in my_brackets}

    # add player score of to each player's total score
    for player in my_brackets:
        results[player]['total_points'] += player_score[player]

    # Assign a win to the winner or tied winners in my_brackets
    for player in my_brackets:
        if player_score[player] == max(player_score.values()):
            results[player]['wins'] += 1


# ******** Post Processing ****************
for player in results:
    results[player]['average_score'] = float(results[player]['total_points'])/num_sims
    results[player]['win_perc'] = float(results[player]['wins'])/num_sims * 100



print('done')