#converts address into longtitude and latitude to fetch  the weather condition and then sends you an email
#By: Peter Sun

#!/usr/bin/env python3
import geocoder, requests, smtplib
from email.mime.text import MIMEText
from secrets import API_KEY, sender, recipients, email_password
#api call portion

API_BASE_URL = "https://api.darksky.net/forecast/"
API=API_BASE_URL+API_KEY

#define locations you want weather info about
locations = ['Boston, MA', 'Atlanta, GA']



def main():
# location api call portion
	email_body= get_weather_info(locations)
	#sender = email address sending from , receiver = email address receiving
	for recipient in recipients:
		send_email(sender, recipient, email_body)


def get_api(place):
	g = geocoder.arcgis(place)	
	lat=str(g.latlng[0])
	lng=str(g.latlng[1])

	full_api_url=API+lat+','+lng  #set full api
	print(full_api_url)
	return full_api_url


def get_weather_info(locations):
	
	email_body=''

	for place in locations:
	#set lat and longtitude(lng)
		full_api_url = get_api(place)
		result=requests.request('GET', full_api_url).json() #set request and assign to results

		#currently
		summary=result['currently']['summary']
		temp = result['currently']['temperature']
		#conver F to C
		temp_f = temp
		temp_c = (temp - 32)*5 /9
		current_precipProbability = result['currently']['precipProbability']

		#hourly
		hourly_summary = result['hourly']['summary']

		place_content = "{0}'s temperature is currently: {1}°C  {temp_f} , {2}\nPrecipitation probability: {3}% \nForcast: {4} \n".format(place, "%.1f" % float(temp_c), summary, current_precipProbability, hourly_summary)
		email_body += '\n\n\n'+ place_content

	return email_body



def send_email(sender, recipient, email_body):
	##convert locations variable into a string called 'location'
	location = ' & '.join(map(str, locations))

	#define the subject
	subject = 'Weather in {}'.format(location)

	#put in variables from earlier
	header = 'To:' + recipient + '\n' + 'From: ' + sender + '\n' + 'Subject:'+ subject +'\n\n'
	
	msg = header + email_body
	msg = str(msg).encode('utf-8')
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login(sender, email_password)
	mail.sendmail(sender, recipient, msg)
	mail.close()




if __name__ == '__main__':
	main()







