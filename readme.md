# WeezSite

Welcome to WeezSite. If you have found this, you are almost certainly lost. Please turn back now otherwise 
go straight to the Gulag. Do not collect 200.

![Weez](static/img/die.jpg)

This is Flask based web application and extends the functionality of the Warzone data collected by 
[Weez](https://github.com/rumeeahmed/Weez). The link to the live web application can be found 
[here](http://weezingtonsilva.herokuapp.com/). This is hosted on Heroku, uses Firebase as the database,
with HTML, CSS,  Bootstrap and Chart.js for the frontend and Python for the backend.

---

# Homepage

The homepage is a simple bootstrap grid that provides an overview of what the app has to offer. The link
to this page can be found [here](http://weezingtonsilva.herokuapp.com/). The navigation bar is a bootstrap
element that is being extended into the base template using the Jinja templating language.

---

# Player

The player page is a set of bootstrap cards elements contained within the bootstrap carousel element
which provides a high level overview of the players stats; games_played, kills, deaths, assists and K/D.
Each card links to a page for the full player stats. A link to this page can be found 
[here](http://weezingtonsilva.herokuapp.com/players)

Once taken to a players stats a line chart from the Charts.js library will be rendered for the following stats
over time:

- Score
- Kills
- Deaths
- Assists
- K/D
- Damage
- Damage Taken
- Headshots
- Revives
- Teams Wiped

---

# Awards

The Awards page serves the awards data stored in the firebase database under the `awards` collection. The
link to the awards page can be found [here](http://weezingtonsilva.herokuapp.com/awards). The Awards are
a list of categories achieved by player per Warzone session. The awards are as listed below:

- `Bullet Bitch`: The player that received the most damage.
- `Gummy Bear`: The player that takes the least damage taken per death.
- `Headmaster`: The player with the most headshots.
- `Lethal Killer`: The player that has the least amount of damage per kill.
- `Least Lethal Killer`: The player that has the most amount of damage per kill.
- `Medic`: The player with the most revives.
- `Tank`: The player that takes the most damage per death.
- `Team Demolisher`: The player with the most team wipes.
- `Team Lover`: The player with the highest score.
- `Team Hater`: The player with the lowest score.
- `Top Assister`: The player with the most assists.
- `Team Demolisher`: Cheen.

---

# Team Stats

There are two pages under team stats: [Total Team Stats](http://weezingtonsilva.herokuapp.com/team_stats) 
and [Team Stats per Game](http://weezingtonsilva.herokuapp.com/team_stats_per_game). The former logs the 
cumulative values of all stats per player for that night whilst the latter averages out the data per game 
played for the session. The Charts are Line Charts from the Charts.js library and they display the standard
game stats per session played.