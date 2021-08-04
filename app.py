from flask import Flask, render_template
from views.home import Home
from views.player import Players
from datetime import datetime

app = Flask(__name__)

app.add_url_rule('/', view_func=Home.as_view('home'))
app.add_url_rule('/players', view_func=Players.as_view('players'))


@app.context_processor
def inject_year() -> dict:
    """
    Generate the current year and send it across to all of the templates.
    :return: a dictionary object that contains the year.
    """
    year = datetime.now().strftime('%Y')
    return dict(year=year)


if __name__ == '__main__':
    app.run(debug=True)
