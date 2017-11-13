from flask import Flask, render_template,request,redirect,url_for,flash 
import urllib2
import json

app = Flask(__name__)
app.secret_key = "NOT_SECURE"

@app.route('/')
def root():
    return render_template("search_summoner.html")

@app.route('/summoner', methods = ['POST'])
def summoner():
    sname = request.form['summoner_name']
    u = urllib2.urlopen("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+sname+"?api_key=RGAPI-fdd5d9a3-e5e5-4a80-af19-83ad59460aa4")
    d = u.read()
    summ_dict = json.loads(d)
    name = summ_dict['name']
    accountId = summ_dict['accountId']
    summId = summ_dict['id']
    u2 = urllib2.urlopen("https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/"+str(summId)+"?api_key=RGAPI-fdd5d9a3-e5e5-4a80-af19-83ad59460aa4")
    d2 = u2.read()
    rank_dict = json.loads(d2)
    return render_template("summoner_welcome.html", name = name, summ_level = summ_dict['summonerLevel'], profile_icon = "http://ddragon.leagueoflegends.com/cdn/6.3.1/img/profileicon/"+str(summ_dict['profileIconId'])+".png", summId = summId, tier = rank_dict[0]['tier'], rank = rank_dict[0]['rank'], leagueName = rank_dict[0]['leagueName'], wins = rank_dict[0]['wins'], losses = rank_dict[0]['losses'], leaguePoints = rank_dict[0]['leaguePoints'])

if __name__ == "__main__":
    app.debug = True
    app.run()
