import requests
import  _datetime as dt
import smtplib
import  time

MY_LAT = 27.700769 # Your latitude
MY_LONG = 85.300140 # Your longitude
email = "atishtest2060@gmail.com"
password = "pzch mfxp mvwn fiwu"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def check_latitude():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 > iss_latitude < MY_LAT and MY_LONG - 5 > iss_longitude < MY_LONG + 5:
        return  True


def check_time():
    response_time = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_time.raise_for_status()
    data_time = response_time.json()
    sunrise = int(data_time["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_time["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = int(str(dt.datetime.now()).split(" ")[1].split(":")[0])
    if sunrise >= current_time or current_time >= sunset:
        return  True


while True:
    time.sleep(60)
    if check_latitude() and check_time():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                to_addrs="thapasinghatish2060@gmail.com",
                                msg=f"Subject: Look Above!!\n\nThe ISS is above you")
    print("Look")





#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



