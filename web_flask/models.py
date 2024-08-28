#!/usr/bin/python3
""" importing the database from app"""
from database import db


class CO2Record(db.Model):
    """a class which becomes the table"""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(13))
    cycle = db.Column(db.Float)
    trend = db.Column(db.Float)
