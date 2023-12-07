# CrowdCompassUI 🧭 
# Overview
Crowd Compass is a web application designed to help users assess the crowdedness level at different restaurants, aiding them in making informed decisions about their dining plans. The user-friendly interface displays a bar chart representing the crowdedness level, calculated based on the current and maximum capcity of each restaurant. Additionally, restaurant administrators can log in to edit the live and maximum capacities for their establishments.

# Prerequisites 
Ensure you have the following installed:

Python 3.x
Streamlit library 

# Initializaiton and set up
Take the project files out of the repository by performing a Clone the Repository.

Install Dependencies: Install the Python modules that are necessary: shown in requirements.txt

# Usage

To run the Crowd Compass application, execute the following command in your terminal: streamlit run crowd_compass.py

User Roles
1. User:
Allows users to view the crowdedness levels of different restaurants.
2. Admin:
Enables restaurant administrators to log in and edit live and maximum capacities.
Admin Credentials
Username: Admin
Password: CROWD

# Application Overview

Upon launching the application, users are presented with a login page where they can choose their role—either "User" or "Admin." Admins can log in using the provided credentials to access editing functionalities.

Admin Features
Add new restaurants with live and maximum capacities.
Visual representation of crowdedness levels through a dynamic progress bar.
Data is saved in a json file and can be used for the user view.

User Features
View current and maximum capacities of different restaurants.
Real-time crowdedness levels displayed through color-coded progress bars.

# Code Structure

The application code is organized into functions and follows best practices for readability and maintainability. The app() function acts as the entry point, launching the Streamlit app based on the selected role. 



