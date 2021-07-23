# SQL Hawaii Weather Analysis
Using pandas, scipy, and SQLAlchemy to visualize and test data from Hawaiian weather stations SQL database.

Created by Sunny Kim

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

## Project Description
An analysis of Hawaiian climate data queried from a weather station SQL database. This project explores levels of precipitation over the course of a year, the distribution of the most active weather station's recorded temperatures, and runs t-tests to test if there is a statistically meaningful difference between the recorded temperature between June and December. Additionally, this project contains an API built with Flask that provides JSON responses of the SQL climate data.

### Built With

* Python - pandas, numpy, scipy, matplotlib, datetime
* SQLAlchemy
* Flask



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sunwoo-kim20/sql-hawaii-weather-analysis.git
   ```
2. Run Flask application from terminal
   ```sh
   python app.py
   ```
3. Run on local server http://127.0.0.1:5000/


<!-- USAGE EXAMPLES -->
## Usage

## Data Visualization
![Precipitation Bar Chart](https://github.com/sunwoo-kim20/sql-hawaii-weather-analysis/blob/main/docs/images/precipitation-chart.png?raw=true)


![Histogram of temperature data from most active station](https://github.com/sunwoo-kim20/sql-hawaii-weather-analysis/blob/main/docs/images/temp-histogram.png?raw=true)

### Home page of Flask API with available routes

![Flask API Home with routes](https://github.com/sunwoo-kim20/sql-hawaii-weather-analysis/blob/main/docs/images/api-routes.png?raw=true)

### Example of route's JSON response
![Stations Route response](https://github.com/sunwoo-kim20/sql-hawaii-weather-analysis/blob/main/docs/images/api-station-call.png?raw=true)



<!-- CONTACT -->
## Contact

Sunny Kim - s.kim32415@gmail.com

Project Link: [https://github.com/sunwoo-kim20/sql-hawaii-weather-analysis](https://github.com/sunwoo-kim20/sql-hawaii-weather-analysis)


