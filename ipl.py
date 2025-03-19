import pandas as pd
import numpy as np

matches = pd.read_csv('ipl-matches (1).csv')
players = pd.read_csv('IPL_Ball_by_Ball_2008_2022.csv')

def teamsAPI():
    team = list(set(list(matches['Team1'])+list(matches['Team2'])))
    team_dict = {
        'Teams': team
    }
    return team_dict

def teamVteam(team1,team2):
    valid_team = team = list(set(list(matches['Team1'])+list(matches['Team2'])))
    if team1 in valid_team and team2 in valid_team:
        temp_df = matches[(matches['Team1'] == team1) & ( matches['Team2'] == team2 ) | (matches['Team1'] == team2) & ( matches['Team2'] == team1 )]
        total_match = temp_df.shape[0]
        team1_won = int(temp_df['WinningTeam'].value_counts()[team1])
        team2_won = int(temp_df['WinningTeam'].value_counts()[team2])
        draw = total_match - (team1_won + team2_won)
        response = {
              'total_match':total_match,
              team1:team1_won,
              team2:team2_won,
              'draw':draw
          }
        return response
    else:
        return {'message':'Invalid team name'}

def won_team_count(team):
      final_team = matches[matches['MatchNumber']=='Final']
      won = final_team[final_team['WinningTeam'] == team ].shape[0]
      result = {
          team:won
      }
      return result

def player_runs(player):
    runs_df = players.groupby('batter')['batsman_run'].sum()
    runs = int(runs_df[player])
    return {
        player : runs
    }
