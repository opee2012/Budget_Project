from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId
import db_details

app = Flask(__name__)

client = db_details.client

db = client.budget
expense = db.expense


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        payment = request.form['payment']
        expense.insert_one({'name': name, 'price': price, 'payment': payment})
        return redirect(url_for('index'))

    all_expenses = expense.find()
    return render_template('test.html', expense=all_expenses)


@app.post('/<id>/delete/')
def delete(id):
    expense.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
