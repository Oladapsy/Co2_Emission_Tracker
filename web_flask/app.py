#!/usr/bin/python3
""" the neccessary modules for flask and database"""
from database import db
from flask import Flask, jsonify, render_template
from flask_migrate import Migrate
import json
from models import CO2Record
import requests
from flask_cors import CORS
from datetime import datetime, timedelta
"""from routes import *"""


"""create the app"""
app = Flask(__name__)
migrate = Migrate(app, db)
""" configure the MYSQL database"""
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://oladapsy:1234@localhost/co2db"
""" initialize the app with the extension"""
db.init_app(app)
CORS(app)


@app.route('/', strict_slashes=False)
@app.route('/home.html', strict_slashes=False)
@app.route('/index.html', strict_slashes=False)
@app.route('/home', strict_slashes=False)
@app.route('/co2tracker.html', strict_slashes=False)
@app.route('/co2tracker', strict_slashes=False)
def index():
    """ the home page of the co2 record"""
    return render_template("index.html")


@app.route('/about', strict_slashes=False)
@app.route('/about.html', strict_slashes=False)
def about():
    """ the about page of the co2 record"""
    return render_template("about.html")


@app.route('/contact', strict_slashes=False)
@app.route('/contact.html', strict_slashes=False)
def contact():
    """ the contact page of the co2 record"""
    return render_template("contact.html")


@app.route('/search', strict_slashes=False)
@app.route('/search.html', strict_slashes=False)
def search():
    """ the search page of the co2 record"""
    return render_template("search.html")


@app.route('/api/co2/records/3limit', strict_slashes=False, methods=['GET'])
def get_co2_records():
    """ Returns the last three co2 records"""
    records = CO2Record.query.order_by(CO2Record.date.desc()).limit(3).all()
    return jsonify([{
        'id': record.id,
        'date': record.date,
        'cycle': record.cycle,
        'trend': record.trend
    } for record in records])


@app.route('/api/co2/records/7limit', strict_slashes=False, methods=['GET'])
def get_co2_records_7days():
    """ Returns the last seven days co2 records"""
    records = CO2Record.query.order_by(CO2Record.date.desc()).limit(7).all()
    return jsonify([{
        'id': record.id,
        'date': record.date,
        'cycle': record.cycle,
        'trend': record.trend
    } for record in records])


@app.route('/api/co2/TodayCycleValue', strict_slashes=False, methods=['GET'])
def get_co2_today_cycle_value():
    """ Returns the cycle value of co2 today"""
    records = CO2Record.query.order_by(CO2Record.date.desc()).limit(1).all()
    return jsonify({'cycle': float(records[0].cycle)})


@app.route('/api/co2/records/range/<start_date>/<end_date>', methods=['GET'])
def get_co2_records_by_range(start_date, end_date):
    """Returns CO2 records within a specific date range"""
    records = CO2Record.query.filter(
        CO2Record.date.between(start_date, end_date)).all()
    return jsonify([{
        'date': record.date,
        'cycle': record.cycle,
        'trend': record.trend
    } for record in records])


@app.route('/api/co2/records/highlow/<start_date>/<end_date>', methods=['GET'])
def get_co2_high_low_by_range(start_date, end_date):
    """ Returns the highest and lowest record within a date range"""
    records = CO2Record.query.filter(
        CO2Record.date.between(start_date, end_date)).all()
    if not records:
        return jsonify({'error': 'No record found'}), 404

    highest = max(records, key=lambda r: r.cycle)
    lowest = min(records, key=lambda r: r.cycle)

    return jsonify({
        'highest': {
            'date': highest.date,
            'cycle': highest.cycle,
            'trend': highest.trend
        },
        'lowest': {
            'date': lowest.date,
            'cycle': lowest.cycle,
            'trend': lowest.trend
            }
        })


@app.route('/api/co2/records/high-low', methods=['GET'])
def get_co2_high_low_by_overall():
    """ Returns the highest and lowest records overall"""
    records = CO2Record.query.all()
    if not records:
        return jsonify({'error': 'No record found'}), 404

    highest = max(records, key=lambda r: r.cycle)
    lowest = min(records, key=lambda r: r.cycle)

    return jsonify({
        'highest': {
            'date': highest.date,
            'cycle': highest.cycle,
            'trend': highest.trend
        },
        'lowest': {
            'date': lowest.date,
            'cycle': lowest.cycle,
            'trend': lowest.trend
            }
        })


@app.route('/api/co2/records', methods=['GET'])
def get_all_co2_records():
    """Fetches all co2 records from the database"""
    records = CO2Record.query.all()
    return jsonify([{
        'id': record.id,
        'date': record.date,
        'cycle': record.cycle,
        'trend': record.trend
    } for record in records])


@app.route('/api/co2/compare/<date1>/<date2>', methods=['GET'])
def comapre_co2_records(date1, date2):
    """ Fetches co2 records for two specific dates comparison"""
    record1 = CO2Record.query.filter_by(date=date1).first()
    record2 = CO2Record.query.filter_by(date=date2).first()

    if not record1 or not record2:
        return jsonify({'error': 'One or both dates not found in the database'}
                       ), 404
    return jsonify([
        {
            'date': record1.date,
            'cycle': record1.cycle,
            'trend': record1.trend
        },
        {
            'date': record2.date,
            'cycle': record2.cycle,
            'trend': record2.trend
            }
        ])


@app.route('/api/co2/compare/today/lastYear', methods=['GET'])
def comiaipre_co2_records():
    """ Fetches co2 records for today and last year"""
    today = datetime.today().date() - timedelta(days=2)
    last_year = (today - timedelta(days=366)).strftime('%Y-%m-%d')

    record1 = CO2Record.query.filter_by(date=today).first()
    record2 = CO2Record.query.filter_by(date=last_year).first()

    if not record1 or not record2:
        return jsonify({'error': 'One or both dates not found in the database'}
                       ), 404
    return jsonify([
        {
            'date': record1.date,
            'cycle': record1.cycle,
            'trend': record1.trend
        },
        {
            'date': record2.date,
            'cycle': record2.cycle,
            'trend': record2.trend
            }
        ])


@app.route('/co2', strict_slashes=False, methods=['GET'])
def fetch_co2_data():
    """fetch the daily co2 record"""
    url_half1 = "https://daily-atmosphere-carbon-dioxide-concentration"
    url_half2 = ".p.rapidapi.com/api/co2-api"
    url = f"{url_half1}{url_half2}"

    x_rap_host = "daily-atmosphere-carbon-dioxide-concentration.p.rapidapi.com"
    x_rap_key = "62f0ec2bfdmshdb1f8417ca787b3p179058jsn54953359a295"
    headers = {'x-rapidapi-host': x_rap_host,
               'x-rapidapi-key': x_rap_key
               }
    response = requests.get(url, headers=headers)
    data = response.json()

    """get the latest record from the database"""
    try:
        latest_record = CO2Record.query.order_by(CO2Record.date.desc()).first()
    except Exception as e:
        print(f"Error Querying database {e}")
        latest_record = None

    """loop through each record in response"""
    for record in data['co2']:
        year = record['year']
        month = str(record['month']).zfill(2)
        day = str(record['day']).zfill(2)
        date_string = f"{year}-{month}-{day}"

        """check if the record is newer than the latest"""
        if latest_record is None or date_string > latest_record.date:
            co2_record = CO2Record(date=date_string, cycle=record['cycle'],
                                   trend=record['trend'])
            db.session.add(co2_record)

    try:
        db.session.commit()
    except Exception as e:
        print(f"Error committing to database {e}")
        db.session.rollback()

    return "New CO2 records fetched and saved!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
