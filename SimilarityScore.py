from __future__ import print_function
import math
import pandas as pd
import numpy as np
import cfbd
from cfbd.rest import ApiException

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'ADD API KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.StatsApi(cfbd.ApiClient(configuration))
year = 2022 # int | Year filter (required if no team specified) (optional)
# team = 'team_example' # str | Team filter (required if no year specified) (optional)
# exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)
# start_week = 56 # int | Starting week filter (optional)
# end_week = 56 # int | Starting week filter (optional)

try:
    # Advanced team metrics by season
    teams = api_instance.get_advanced_team_season_stats(year=year)
except ApiException as e:
    print("Exception when calling StatsApi->get_advanced_team_season_stats: %s\n" % e)

history = pd.read_csv('HistoricalTeamStats.csv')
history['season_team'] = history['season'].astype(str) + ' ' + history['team']
history.set_index('season_team', inplace=True)

print(history.head())
    
teamlist = pd.json_normalize([t.to_dict() for t in teams])
num_list = ['offense.ppa',
               'offense.success_rate',
               # 'offense.explosiveness',
               # 'offense.power_success',
               # 'offense.stuff_rate',
               # 'offense.line_yards',
               # 'offense.second_level_yards',
               # 'offense.open_field_yards',
               'offense.points_per_opportunity',
               # 'offense.field_position.average_start',
               # 'offense.field_position.average_predicted_points',
               # 'offense.standard_downs.rate',
               # 'offense.standard_downs.ppa',
               # 'offense.standard_downs.success_rate',
               # 'offense.standard_downs.explosiveness',
               # 'offense.passing_downs.rate',
               # 'offense.passing_downs.ppa',
               # 'offense.passing_downs.success_rate',
               # 'offense.passing_downs.explosiveness',
               'offense.rushing_plays.rate',
               'offense.rushing_plays.ppa',
               'offense.rushing_plays.success_rate',
               # 'offense.rushing_plays.explosiveness',
               'offense.passing_plays.rate',
               'offense.passing_plays.ppa',
               'offense.passing_plays.success_rate',
               # 'offense.passing_plays.explosiveness',
               'defense.ppa',
               'defense.success_rate',
               # 'defense.explosiveness',
               # 'defense.power_success',
               # 'defense.stuff_rate',
               # 'defense.line_yards',
               # 'defense.second_level_yards',
               # 'defense.open_field_yards',
               'defense.points_per_opportunity',
               # 'defense.field_position.average_start',
               # 'defense.field_position.average_predicted_points',
               # 'defense.standard_downs.rate',
               # 'defense.standard_downs.ppa',
               # 'defense.standard_downs.success_rate',
               # 'defense.standard_downs.explosiveness',
               # 'defense.passing_downs.rate',
               # 'defense.passing_downs.ppa',
               # 'defense.passing_downs.success_rate',
               # 'defense.passing_downs.explosiveness',
               # 'defense.rushing_plays.rate',
               'defense.rushing_plays.ppa',
               'defense.rushing_plays.success_rate',
               # 'defense.rushing_plays.explosiveness',
               # 'defense.passing_plays.rate',
               'defense.passing_plays.ppa',
               'defense.passing_plays.success_rate']
               # 'defense.passing_plays.explosiveness']
col_list = ['season', 'team','offense.ppa',
               'offense.success_rate',
               # 'offense.explosiveness',
               # 'offense.power_success',
               # 'offense.stuff_rate',
               # 'offense.line_yards',
               # 'offense.second_level_yards',
               # 'offense.open_field_yards',
               'offense.points_per_opportunity',
               # 'offense.field_position.average_start',
               # 'offense.field_position.average_predicted_points',
               # 'offense.standard_downs.rate',
               # 'offense.standard_downs.ppa',
               # 'offense.standard_downs.success_rate',
               # 'offense.standard_downs.explosiveness',
               # 'offense.passing_downs.rate',
               # 'offense.passing_downs.ppa',
               # 'offense.passing_downs.success_rate',
               # 'offense.passing_downs.explosiveness',
               'offense.rushing_plays.rate',
               'offense.rushing_plays.ppa',
               'offense.rushing_plays.success_rate',
               # 'offense.rushing_plays.explosiveness',
               'offense.passing_plays.rate',
               'offense.passing_plays.ppa',
               'offense.passing_plays.success_rate',
               # 'offense.passing_plays.explosiveness',
               'defense.ppa',
               'defense.success_rate',
               # 'defense.explosiveness',
               # 'defense.power_success',
               # 'defense.stuff_rate',
               # 'defense.line_yards',
               # 'defense.second_level_yards',
               # 'defense.open_field_yards',
               'defense.points_per_opportunity',
               # 'defense.field_position.average_start',
               # 'defense.field_position.average_predicted_points',
               # 'defense.standard_downs.rate',
               # 'defense.standard_downs.ppa',
               # 'defense.standard_downs.success_rate',
               # 'defense.standard_downs.explosiveness',
               # 'defense.passing_downs.rate',
               # 'defense.passing_downs.ppa',
               # 'defense.passing_downs.success_rate',
               # 'defense.passing_downs.explosiveness',
               # 'defense.rushing_plays.rate',
               'defense.rushing_plays.ppa',
               'defense.rushing_plays.success_rate',
               # 'defense.rushing_plays.explosiveness',
               # 'defense.passing_plays.rate',
               'defense.passing_plays.ppa',
               'defense.passing_plays.success_rate']
               # 'defense.passing_plays.explosiveness'

teamlist = teamlist[col_list]
teamlist['season_team'] = teamlist['season'].astype(str) + ' ' + teamlist['team']
teamlist.set_index('season_team', inplace=True)
teamlist['SimilarTeam'] = np.nan
teamlist['SimilarityScore'] = np.nan


 
def euclidean_distance(t,h):
    
    dist = math.sqrt(sum(pow(a-b,2) for a, b in zip(t, h)))
    
    return dist

######################################################################
#MAIN SCRIPT
######################################################################



for t_index, row in teamlist.iterrows(): 
    history['SimilarityScore'] = np.nan 
    team = row[num_list].values.tolist()
    
    for h_index, row in history.iterrows():
    
        histteam = row[num_list].values.tolist()
        
        team_norm = [i / i for i in team]
        histteam_norm = [histteam[j] / team[j] for j in range(0,len(histteam))]
    
        sim = 1/(1+euclidean_distance(team_norm,histteam_norm))
        
        print(t_index + ': ' + h_index + ' - ' + str(sim))
    
        history.at[h_index,'SimilarityScore'] = sim
        
    print(t_index + ': ' + history['SimilarityScore'].idxmax())
    teamlist.at[t_index,'SimilarTeam'] = history['SimilarityScore'].idxmax()
    teamlist.at[t_index,'SimilarityScore'] = history['SimilarityScore'].max()

teamlist.to_csv('TeamSimilarities.csv')