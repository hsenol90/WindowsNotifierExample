import datetime
import time
import requests
from plyer import notification

covidStats = None
try:
    covidStats = requests.get("https://covid-19.dataflowkit.com/v1/turkey")
except:
    print("Consider Checking the internet connection")

if covidStats is not None:
    while True:
        notification.notify(
            title="COVID19 Stats on {}".format(datetime.date.today()),
            message="Country:{0}\nTotal cases:{1}\nTotal deaths:{2}\nTotal Last Update:{3}".format(
                covidStats.json()['Country_text'], covidStats.json()['Total Cases_text'],
                covidStats.json()['Total Deaths_text'], covidStats.json()["Last Update"]),
            app_icon="",
            timeout=30, toast=False
        )
        time.sleep(60)
