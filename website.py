"""Module to combine flask and python"""
import time
import sched
import logging
from flask import Flask
from flask import render_template
from flask import request
from covid_news_handling import news_API_request
from covid_data_handler import covid_API_request
from government_api import covid_API_england


logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
#Function on covid_data_handler
a = covid_API_request()
last7dayCaseExeter = 0
for i in range(0,7):
    last7dayCaseExeter += int(a.get('data')[i].get('newCasesByPublishDate'))
logging.warning('last7dayCaseExeter calculated')

#Function on governmnet_api
b=covid_API_england()
newAdmissions  =  0
last7dayCaseEngland = 0
cumDailyNsoDeathsByDeathDate =0
for i in range(0,7):
    last7dayCaseEngland += int(b.get('data')[i].get('newCasesByPublishDate'))
logging.warning('last7dayCaseEngland calculated')

for p in range(2,9):
    newAdmissions += int(b.get('data')[p].get('newAdmissions'))
logging.warning('newAdmissions calculated')

i = 0
while True:
    try:
        cumDailyNsoDeathsByDeathDate=int(b.get('data')[i].get('cumDailyNsoDeathsByDeathDate'))
        break
    except TypeError:
        logging.warning('No data found')
        i += 1


#Function on covid_news_handling
c = news_API_request()




app = Flask(__name__)
s = sched.scheduler(time.time, time.sleep)
news = [
    {
        "title": c[0],
        "content": c[1]
    },
    {
        "title": c[2],
        "content": c[3]
    }
]
def remove_seen_news():
    """Function is meant to delete articles so news isnt repeated"""
    del c[0:2]
    return c


def add_news_article():
    """Function adds in new news articles that havent been seen yet"""
    news.append({
            'title': c[4],
            'content': c[5]
    })

def schedule_add_news (up):
    """meant to be responsible for adding new scheduled news"""
    e = s.enter(up,1,add_news_article)


update = []
def widgets():
    """Meant to display scheduled updates"""
    update.append({
        "title": (text_field),
        "content": (update_time)
    }
)



@app.route('/index')
def hello():
    """Function that controls flask template"""
    logging.warning('Website running')
    add_news_article()
    s.run(blocking=False)
    text_field = request.args.get('two')
    clear = request.args.get('notif')
    remove_seen_news()
    if text_field:
        update_time = request.args.get('update')
        update_time_sec = hhmm_to_seconds(update_time)
        schedule_add_news(update_time_sec)
        #widgets()
    if clear:#Deletes news if x is clicked
        news.pop(0)
        logging.warning('News article removed')
    return render_template('index.html',
        title='Covid-19 Dashboard',
        location='Exeter',
        nation_location='England',
        local_7day_infections=(last7dayCaseExeter),
        national_7day_infections=(last7dayCaseEngland),
        hospital_cases='Hospital admissions in last 7 days in england: '+(str(newAdmissions)),
        deaths_total='Total national Deaths in England: '+(str(cumDailyNsoDeathsByDeathDate)),
        news_articles=news,
        updates=update)

def minutes_to_seconds( minutes: str ) -> int:
    """Converts minutes to seconds"""
    return int(minutes)*60

def hours_to_minutes( hours: str ) -> int:
    """Converts hours to minutes"""
    return int(hours)*60

def hhmm_to_seconds( hhmm: str ) -> int:
    if len(hhmm.split(':')) != 2:
        print('Incorrect format. Argument must be formatted as HH:MM')
        return None
    return minutes_to_seconds(hours_to_minutes(hhmm.split(':')[0])) + \
        minutes_to_seconds(hhmm.split(':')[1])

if __name__ == '__main__':
    app.run()
