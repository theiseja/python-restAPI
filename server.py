from flask import (
    Flask,
    render_template
)

# Creates application instance
app = Flask(__name__, template_folder="template")

# Creates a URL route for "/"
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)