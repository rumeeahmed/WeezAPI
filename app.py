from flask import Flask, render_template
from views.home import Home

app = Flask(__name__)

app.add_url_rule('/', view_func=Home.as_view('home'))
if __name__ == '__main__':
    app.run(debug=True)
