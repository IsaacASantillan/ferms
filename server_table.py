from models import db, Ms, app
from flask import jsonify, render_template, request

@app.route('/')
def home():
    return render_template('server_table.html')

@app.route('/api/data')
def data():
    try:
        # Get start and end parameters from the request
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', 100))
        
        # Query the database and limit results for pagination
        query = Ms.query.offset(start).limit(end - start).all()
        
        if not query:
            return jsonify({'rows': [], 'total': 0}), 200  # Return empty if no data
        
        minilist = [ms.to_dict() for ms in query]
        total = Ms.