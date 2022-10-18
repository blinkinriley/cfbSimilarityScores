from __future__ import print_function

import cfbd
from cfbd.rest import ApiException

import pandas as pd

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'ADD API KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.StatsApi(cfbd.ApiClient(configuration))
years = range(2001,2022) # int | Year filter (required if no team specified) (optional)
# team = 'team_example' # str | Team filter (required if no year specified) (optional)
# exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)
# start_week = 56 # int | Starting week filter (optional)
# end_week = 56 # int | Starting week filter (optional)
allstats = pd.DataFrame()

for y in years:
    try:
        # Advanced team metrics by season
        teams = api_instance.get_advanced_team_season_stats(year=y)
    except ApiException as e:
        print("Exception when calling StatsApi->get_advanced_team_season_stats: %s\n" % e)
    

    stats = pd.json_normalize([t.to_dict() for t in teams])
    stats = stats[['season', 'team','offense.ppa',
                   'offense.success_rate',
                   'offense.explosiveness',
                   'offense.power_success',
                   'offense.stuff_rate',
                   'offense.line_yards',
                   'offense.second_level_yards',
                   'offense.open_field_yards',
                   'offense.points_per_opportunity',
                   'offense.field_position.average_start',
                   'offense.field_position.average_predicted_points',
                   'offense.standard_downs.rate',
                   'offense.standard_downs.ppa',
                   'offense.standard_downs.success_rate',
                   'offense.standard_downs.explosiveness',
                   'offense.passing_downs.rate',
                   'offense.passing_downs.ppa',
                   'offense.passing_downs.success_rate',
                   'offense.passing_downs.explosiveness',
                   'offense.rushing_plays.rate',
                   'offense.rushing_plays.ppa',
                   'offense.rushing_plays.success_rate',
                   'offense.rushing_plays.explosiveness',
                   'offense.passing_plays.rate',
                   'offense.passing_plays.ppa',
                   'offense.passing_plays.success_rate',
                   'offense.passing_plays.explosiveness',
                   'defense.ppa',
                   'defense.success_rate',
                   'defense.explosiveness',
                   'defense.power_success',
                   'defense.stuff_rate',
                   'defense.line_yards',
                   'defense.second_level_yards',
                   'defense.open_field_yards',
                   'defense.points_per_opportunity',
                   'defense.field_position.average_start',
                   'defense.field_position.average_predicted_points',
                   'defense.standard_downs.rate',
                   'defense.standard_downs.ppa',
                   'defense.standard_downs.success_rate',
                   'defense.standard_downs.explosiveness',
                   'defense.passing_downs.rate',
                   'defense.passing_downs.ppa',
                   'defense.passing_downs.success_rate',
                   'defense.passing_downs.explosiveness',
                   'defense.rushing_plays.rate',
                   'defense.rushing_plays.ppa',
                   'defense.rushing_plays.success_rate',
                   'defense.rushing_plays.explosiveness',
                   'defense.passing_plays.rate',
                   'defense.passing_plays.ppa',
                   'defense.passing_plays.success_rate',
                   'defense.passing_plays.explosiveness']]
    
    allstats = pd.concat([allstats,stats])
    print(y)

allstats.to_csv('HistoricalTeamStats.csv')