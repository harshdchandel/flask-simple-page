from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def home():
	return render_template('home.jade')

if __name__ == '__main__':
	app.run(debug=True)