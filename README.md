---

# CO2 Emission Tracker

## Introduction

The **CO2 Emission Tracker** is a web application designed to display, analyze, and track CO2 emission trends over time using data fetched from a public API. The purpose of the project is to raise awareness of global CO2 concentration trends and provide accessible data for researchers, students, and the general public.

## Purpose of the Project

This project aims to provide:
- Easy access to global CO2 concentration data.
- A platform for visualizing CO2 trends over time.
- Tools for users to analyze CO2 data by date or range, making it useful for environmental researchers and activists.

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)

## Project Description

The **CO2 Emission Tracker** fetches data from a third-party API (carbon-dioxide API) and displays it in a user-friendly way. It provides functionalities such as searching CO2 levels by specific dates or date ranges, visualizing trends over time, and comparing data for different periods.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: MySQL
- **API**: Carbon-dioxide API
- **Visualization**: JavaScript (Vanilla)
- **Hosting**: Deployed using ALX-provided servers

## Features

- **CO2 Data Search by Date**: Users can input a specific date or date range to view CO2 levels for that period.
- **Trend Visualization**: Graphical representation of CO2 concentration over time, allowing users to observe patterns.
- **Date Comparison**: Users can compare CO2 data from two different dates.
- **Pagination**: Although not implemented, pagination was considered to limit the data shown on each page.

## Setup and Installation

### Prerequisites

- Python 3.7+
- Flask
- MySQL
- JavaScript-enabled web browser

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/oladapsy/CO2_Emission_Tracker.git
    ```
2. Set up a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database:
    - Create a MySQL database and update the configuration in `config.py`.
5. Run the Flask app:
    ```bash
    flask run
    ```

### API Integration
This application pulls CO2 data from the [Carbon-dioxide API](https://rapidapi.com).

## Challenges Faced

1. **Flask_SQLAlchemy**: Initially, there were issues using SQLAlchemy, which were resolved by reading the documentation and using assistance from ChatGPT.
2. **Data Visualization**: The original plan was to use Matplotlib and Pandas, but after advice from a frontend designer, JavaScript was used instead for simplicity and better integration with the frontend.
3. **Deployment Issues**: There were multiple issues with deploying the app using Gunicorn, particularly on the second server provided by ALX. SSH access was lost, and a replacement server has not yet been provisioned.
4. **Load Balancer Configuration**: The round-robin setup still attempts to route traffic to the unavailable server, an issue currently being worked on.
5. **Mobile Responsiveness**: The web application's mobile responsiveness is a work in progress and is being improved continuously.

## Future Improvements

- Implement pagination for better data management and user experience.
- Optimize load balancer configuration to handle server outages effectively.
- Complete mobile responsiveness for a more user-friendly experience on all devices.
- Add more sophisticated data visualizations for deeper analysis.

---
