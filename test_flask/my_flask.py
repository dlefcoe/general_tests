import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    # a standard homepage
    return flask.render_template('index.html')

@app.route('/<name>')
def user(name):
    # example of parsing part of url into the function
    return flask.render_template('second_page.html', content=name)

# @app.route('/admin')
# def admin():
#     # example of redirect to the home page
#     return flask.redirect(flask.url_for('home'))




if __name__=='__main__':
    app.run()

