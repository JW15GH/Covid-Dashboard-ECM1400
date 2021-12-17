"""Module to deal with government API for national data"""
import logging
from uk_covid19 import Cov19API
def covid_API_england ():
    """Function retrieves date, hospital admissions, total deaths
       and daily cases using government API"""
    england_only = [
        'areaType=nation',
        'areaName=England'
    ]

    dates_and_cases = {
        "date":  "date",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "newAdmissions": "newAdmissions",
        "cumDailyNsoDeathsByDeathDate":"cumDailyNsoDeathsByDeathDate"
    }

    api = Cov19API(filters=england_only, structure=dates_and_cases)
    logging.info('API has received query for national data')

    global DATA2
    DATA2 = api.get_json()
    return DATA2
