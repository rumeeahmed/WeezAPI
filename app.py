from flask import Flask, render_template
from views.home import Home
from views.player import Players

app = Flask(__name__)

app.add_url_rule('/', view_func=Home.as_view('home'))
app.add_url_rule('/players', view_func=Home.as_view('players'))

if __name__ == '__main__':
    app.run(debug=True)
