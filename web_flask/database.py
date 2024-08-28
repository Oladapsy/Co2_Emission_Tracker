#!/usr/bin/python3
""" to avoid circular import create a database file"""
from flask_sqlalchemy import SQLAlchemy


""" create the extension"""
db = SQLAlchemy()
