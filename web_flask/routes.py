#!/usr/bin/python3
""" extension of the app.py/app"""
from app import app
from models import CO2Record
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


@app.route('/api/co2/records/table/<start_date>/<end_date>', methods=['GET'])
def get_co2_records_table_range(start_date, end date):
    """ returns the pandas table for a given range of date"""
    records = CO2Records.query.filter(
        CO2Record.date.between(start_date, end_date)).all()
    if not records:
        return jsonify{'error': 'No records found in the specified range'}

    """creating a data frame for the record"""
    data = {
            'date': [record.date for record in records],
            'cycle': [record.cycle for record in records],
            'trend': [record.trend for record in records],
        }

    df = pd.DataFrame(data)

    return render_template('co2_table.html', records=df.to_dict(orient='records'))



@app.route('/api/co2/records/table/last-7days', methods=['GET'])
def get_co_records_last_7_days():
    """ returns the last 7 days co2 record but in a table using pandas"""
    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

    """fetch the last 7 days record"""
    records = CO2Record.query.filter(CO2Record.date >= seven_days_ago).all()

    """create a dataframe #list of dictionary"""
    data = {
            'date': [record.date for record in records],
            'cycle': [record.cycle for record in records],
            'trend': [record.trend for record in records],
        }


    df = pd.DataFrame(data)

    return render_template('co2_table.html', records=df.to_dict(orient='records'))
