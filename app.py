from flask import Flask, render_template, jsonify
from flask_table import Table, Col
import fetch_db
import time

app = Flask(__name__)

class MyTable(Table):
    State_Name = Col('State Name')
    District_Name = Col('District Name')
    Crop_Year = Col('Crop Year')
    Season = Col('Season')
    Crop = Col('Crop')
    Area = Col('Area')
    Production = Col('Production')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/chart_data')
def get_chart_data():
    data = MyTable([{
        'State_Name': 'Andaman and Nicobar Islands',
        'District_Name': 'NICOBARS',
        'Crop_Year': 2000,
        'Season': 'Kharif',
        'Crop': 'Rice',
        'Area': 102,
        'Production': 321
    }, {
        'State_Name': 'Andaman and Nicobar Islands',
        'District_Name': 'NICOBARS',
        'Crop_Year': 2001,
        'Season': 'Kharif',
        'Crop': 'Rice',
        'Area': 120,
        'Production': 412
    }])
    
    labels = [row['State_Name'] for row in data.items]
    area_data = [row.get('Area', 0) for row in data.items]
    production_data = [row['Production'] for row in data.items]
    
    chart_data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Area',
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1,
                'data': area_data,
            },
            {
                'label': 'Production',
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1,
                'data': production_data,
            },
        ]
    }
    
    response = jsonify(chart_data)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/show_table')
def show_table():
    data = fetch_db.full_db()
    table = MyTable(data)
    return render_template('table.html', table=table)

@app.route('/getjson')
def get_json():
    return fetch_db.get_json_data()

@app.route('/visual')
def visual():
    chart_data = get_chart_data()
    return render_template('visual.html', chart_data=chart_data)


if __name__ == '__main__':
    while True:
        app.run(debug=True, port=5000)
        time.sleep(86400)
