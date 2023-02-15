from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/project')
def project():
    return render_template('portfolio.html')

@app.route('/single')
def single():
    return render_template('single.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)