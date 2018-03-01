# this file will contain which teams an play in which games

class BracketMap:

    def __init__(self):

        # contains the games in which it is possible for each team to play
        maps = [
            [32, 16, 8, 4, 2, 1],
            [32, 16, 8, 4, 2, 1],
            [33, 16, 8, 4, 2, 1],
            [33, 16, 8, 4, 2, 1],
            [34, 17, 8, 4, 2, 1],
            [34, 17, 8, 4, 2, 1],
            [35, 17, 8, 4, 2, 1],
            [35, 17, 8, 4, 2, 1],
            [36, 18, 9, 4, 2, 1],
            [36, 18, 9, 4, 2, 1],
            [37, 18, 9, 4, 2, 1],
            [37, 18, 9, 4, 2, 1],
            [38, 19, 9, 4, 2, 1],
            [38, 19, 9, 4, 2, 1],
            [39, 19, 9, 4, 2, 1],
            [39, 19, 9, 4, 2, 1],
            [40, 20, 10, 5, 2, 1],
            [40, 20, 10, 5, 2, 1],
            [41, 20, 10, 5, 2, 1],
            [41, 20, 10, 5, 2, 1],
            [42, 21, 10, 5, 2, 1],
            [42, 21, 10, 5, 2, 1],
            [43, 21, 10, 5, 2, 1],
            [43, 21, 10, 5, 2, 1],
            [44, 22, 11, 5, 2, 1],
            [44, 22, 11, 5, 2, 1],
            [45, 22, 11, 5, 2, 1],
            [45, 22, 11, 5, 2, 1],
            [46, 23, 11, 5, 2, 1],
            [46, 23, 11, 5, 2, 1],
            [47, 23, 11, 5, 2, 1],
            [47, 23, 11, 5, 2, 1],
            [48, 24, 12, 6, 3, 1],
            [48, 24, 12, 6, 3, 1],
            [49, 24, 12, 6, 3, 1],
            [49, 24, 12, 6, 3, 1],
            [50, 25, 12, 6, 3, 1],
            [50, 25, 12, 6, 3, 1],
            [51, 25, 12, 6, 3, 1],
            [51, 25, 12, 6, 3, 1],
            [52, 26, 13, 6, 3, 1],
            [52, 26, 13, 6, 3, 1],
            [53, 26, 13, 6, 3, 1],
            [53, 26, 13, 6, 3, 1],
            [54, 27, 13, 6, 3, 1],
            [54, 27, 13, 6, 3, 1],
            [55, 27, 13, 6, 3, 1],
            [55, 27, 13, 6, 3, 1],
            [56, 28, 14, 7, 3, 1],
            [56, 28, 14, 7, 3, 1],
            [57, 28, 14, 7, 3, 1],
            [57, 28, 14, 7, 3, 1],
            [58, 29, 14, 7, 3, 1],
            [58, 29, 14, 7, 3, 1],
            [59, 29, 14, 7, 3, 1],
            [59, 29, 14, 7, 3, 1],
            [60, 30, 15, 7, 3, 1],
            [60, 30, 15, 7, 3, 1],
            [61, 30, 15, 7, 3, 1],
            [61, 30, 15, 7, 3, 1],
            [62, 31, 15, 7, 3, 1],
            [62, 31, 15, 7, 3, 1],
            [63, 31, 15, 7, 3, 1],
            [63, 31, 15, 7, 3, 1],
            #[36, 18, 9, 4, 2, 1],    # extra seed
            #[48, 24, 12, 6, 3, 1],   # extra seed
            #[32, 16, 8, 4, 2, 1],    # extra seed
            #[60, 20, 15, 7, 3, 1]   # extra seed
        ]

        # the teams playing this year in order (top to bottom, left side first)
        this_years_teams = ['Villanova', 'Mount St. Mary\'s', 'Wisconsin', 'Virginia Tech', 'Virginia',
                            'North Carolina-Wilmington', 'Florida', 'East Tennessee State', 'Southern Methodist',
                            'Southern California', 'Baylor', 'New Mexico State', 'South Carolina', 'Marquette', 'Duke',
                            'Troy', 'Gonzaga', 'South Dakota State', 'Northwestern', 'Vanderbilt', 'Notre Dame',
                            'Princeton', 'West Virginia', 'Bucknell', 'Maryland', 'Xavier', 'Florida State',
                            'Florida Gulf Coast', 'Saint Mary\'s (CA)', 'Virginia Commonwealth', 'Arizona',
                            'North Dakota', 'Kansas', 'UC-Davis', 'Miami (FL)', 'Michigan State', 'Iowa State',
                            'Nevada', 'Purdue', 'Vermont', 'Creighton', 'Rhode Island', 'Oregon', 'Iona', 'Michigan',
                            'Oklahoma State', 'Louisville', 'Jacksonville State', 'North Carolina', 'Texas Southern',
                            'Arkansas', 'Seton Hall', 'Minnesota', 'Middle Tennessee', 'Butler', 'Winthrop',
                            'Cincinnati', 'Kansas State', 'UCLA', 'Kent State', 'Dayton', 'Wichita State', 'Kentucky',
                            'Northern Kentucky']
                            #'Providence',  'North Carolina Central', 'New Orleans', 'Wake Forest']


        # We separated the two above arrays so that "this_years_teams" can be loaded in automatically in the future.
        self.map_dict = {team: map for (team, map) in zip(this_years_teams, maps)}







