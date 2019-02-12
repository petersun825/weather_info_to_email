# weather_info_to_email

Python script that converts location into longitude and latitude coordinates and send an API request for weather information at the locations.  Then it parses the information from the API and logs into an email account to send the email to the recipients.  Can handle multiple locations and recipients.

# installation
 1. git download script weather.py
 2. create new file named secrets.py in the same directory
 3. go to https://darksky.net/dev and obtain API key, add the api key to secrets.py as API_KEY = '-----'
 4. install python modules geocoder, requests, smtplib
 5. go to secrets.py and create list for email_password, sender, and recipients.  email_password is for the sender in order to access the email account for sending the information.
 6. edit the locations variable in weather.py if you'd like to get locations of other places
 7. if you'd like it to run the file automatically can use cron.  here's a tutorial: https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/
 
 cron cheatsheet:
 ┌───────────── minute (0 - 59)
 │ ┌───────────── hour (0 - 23)
 │ │ ┌───────────── day of month (1 - 31
 │ │ │ ┌───────────── month (1 - 12)
 │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
 │ │ │ │ │                    7 is also Sunday on some systems)
 │ │ │ │ │
 │ │ │ │ │
 * * * * *  command_to_execute  
 
 # run
 in terminal run python3 weather.py
