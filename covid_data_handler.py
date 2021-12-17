"""Module to handle all covid data functionalities"""
import csv
import sched
import time
import logging
from uk_covid19 import Cov19API

logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)

def parse_csv_data (csv_filename: str) -> list:

    """Returns a list of with each line of the CSV file"""

    logging.info('Opening and processing CSV file')
    with open (csv_filename, 'r', encoding="utf8") as csv_filename:
        translate = csv.reader (csv_filename)
        global DATA
        DATA = list (translate) #Using list() converts into list of lists
        return DATA


def process_covid_csv_data (covid_csv_data: list) ->int:

    """Processes data and returns the number of cases in the last 7 days,
       the total number of deaths and the current number of patients in
       hospital"""

    last7days_cases = 0
    for i in range(3,10): #4th day is used as first complete day of data
        last7days_cases = last7days_cases + int(DATA[i][6])
    logging.info('Processed last7days_cases')

    total_deaths = 0
    total_deaths = total_deaths + int(DATA[14][4])
    logging.info('Processed total_deaths')

    current_hospital_cases = 0
    current_hospital_cases = current_hospital_cases + int(DATA[1][5])
    logging.info('Processed current_hospital_cases')


    return last7days_cases, current_hospital_cases, total_deaths



def covid_API_request (location="Exeter", location_type="ltla") -> list:

    """Uses a government API to retrieve covid cases
       in Exeter by publish date"""

    england_only = [
        'areaType='+(location_type),
        'areaName='+(location)
    ]

    dates_and_cases = {
        "newCasesByPublishDate": "newCasesByPublishDate",
    }

    logging.info('Creating query for Exeter to use in API')
    api = Cov19API(filters=england_only, structure=dates_and_cases)

    global DATA2
    DATA2 = api.get_json()
    return DATA2


def schedule_covid_updates (update_interval: int, update_name = ''):

    """Allows user to allow schedule updates for refresh of function
        above"""

    schedule = sched.scheduler(time.time, time.sleep)
    update_name = schedule.enter(update_interval,1,covid_API_request)
    schedule.run()
    return update_name
    logging.info('returned update_name')
