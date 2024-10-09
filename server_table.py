from models import db, Ms, app  # Ensure you import the correct model
from flask import jsonify, render_template
from flask_sqlalchemy import SQLAlchemy



@app.route('/')
def home():
    return render_template('server_table.html')

@app.route('/api/data')
def data():
    query = Ms.query.all()  # Assuming Ms is your model and you want all rows
    minilist = [ms.to_dict() for ms in query]
    total = len(minilist)  # Get total count if needed
    return jsonify({
        'data': minilist,
        'total': total,
        'x_coordinates': [ms.x_coordinates for ms in query],
        'y_coordinates': [ms.y_coordinates for ms in query]
    })


if __name__ == '__main__':
    app.run()