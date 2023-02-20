from flask import Flask, render_template, request, url_for, redirect, session
from bson.objectid import ObjectId
import db_details

app = Flask(__name__)

client = db_details.client

db = client.budget
expense = db.expense


# @app.route('/', methods=('GET', 'POST'))
# def index():
#     if request.method == 'POST':
#         name = request.form['name']
#         price = request.form['price']
#         payment = request.form['payment']
#         expense.insert_one({'name': name, 'price': price, 'payment': payment})
#         return redirect(url_for('index'))
#
#     all_expenses = expense.find()
#     return render_template('test.html', expense=all_expenses)
#
#
# @app.post('/<id>/delete')
# def delete(id):
#     expense.delete_one({"_id": ObjectId(id)})
#     return redirect(url_for('index'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/budgets')
def budgets():
    if 'username' in session:
        return render_template('pages/budgets.html')
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the username and password are correct
        if request.form['username'] == 'your_username' and request.form['password'] == 'your_password':
            session['username'] = request.form['username']
            # Redirect to the Budgets page if the login is successful
            return redirect(url_for('budgets'))
        else:
            # Display an error message if the login is unsuccessful
            error = 'Invalid username or password. Please try again.'
            return render_template('pages/login.html', error=error)
    else:
        return render_template('pages/login.html')


# Define a route for logging out
@app.route('/logout')
def logout():
    # Remove the username from the session if it exists
    session.pop('username', None)
    # Redirect to the home page
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
