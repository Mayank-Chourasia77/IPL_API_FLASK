#what is api? -> a function that is online anyone can hit on url give input and can take output
#it is like pipeline between two software help eachother to communicate
from math import degrees

from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)
@app.route('/')
def home():
    return 'hello'
@app.route('/api/teams')
def teams():
    team = ipl.teamsAPI()
    return jsonify(team)

@app.route('/api/teamvteam')
def TeamVTeam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    result = ipl.teamVteam(team1, team2)
    return jsonify(result)

@app.route('/api/number-of-final-won')
def finalWon():
    team = request.args.get('team')
    result = ipl.won_team_count(team)
    return jsonify(result)

@app.route('/api/batsman-season-runs')
def batter_runs():
    player = request.args.get('player')
    result = ipl.player_runs(player)
    return jsonify(result)

app.run(debug=True)