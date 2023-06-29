from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This function will render the index.html template when the home route is accessed.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
