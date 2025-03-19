#what is api? -> a function that is online anyone can hit on url give input and can take output
#it is like pipeline between two software help eachother to communicate

import json
from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)
@app.route('/')
@app.route('/')
def home():
    response_data = {
        "message": "Welcome to the IPL Stats API!",
        "endpoints": {
            "Get Teams": "/api/teams",
            "Compare Teams": "/api/teamvteam?team1=CSK&team2=MI",
            "Finals Won": "/api/number-of-final-won?team=CSK",
            "Player Runs": "/api/batsman-season-runs?player=Virat Kohli"
        },
        "status": "Running",
    }
    # Use json.dumps with indent parameter to format the JSON response
    formatted_response = json.dumps(response_data, indent=4)
    return formatted_response, 200, {'Content-Type': 'application/json'}

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
if __name__ == "__main__":
    # Get the PORT from Render (defaults to 5000 if not found)
    port = int(os.environ.get("PORT", 5000))

    # Bind to 0.0.0.0 so Render can access it
    app.run(host="0.0.0.0", port=port)
