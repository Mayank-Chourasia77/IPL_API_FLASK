#what is api? -> a function that is online anyone can hit on url give input and can take output
#it is like pipeline between two software help eachother to communicate
from math import degrees

from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the IPL Stats API!",
        "endpoints": {
            "Get Teams": "/api/teams",
            "Compare Teams": "/api/teamvteam?team1=CSK&team2=MI",
            "Finals Won": "/api/number-of-final-won?team=CSK",
            "Player Runs": "/api/batsman-season-runs?player=Virat Kohli"
        },
        "status": "Running",
        "author": "Your Name",
        "documentation": "https://your-docs-link.com"  # Optional, if you create docs
    })

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

import os

port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
app.run(host="0.0.0.0", port=port, debug=False)
