from Flask import flask, render_template

app = flask(__name__)

@app.route('/')
def home():
    """Display homme page"""
    return render_template('0-index.html')
