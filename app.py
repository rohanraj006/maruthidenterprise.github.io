from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the security page
@app.route('/about')
def security():
    return render_template('security.html')

#Route to utility page 
@app.route('/utility')
def utility():
    return render_template('utility.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
