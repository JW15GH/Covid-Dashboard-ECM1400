# Covid-Dashboard-ECM1400
# **Introduction**
A covid dashboard displaying weekly covid cases in exeter and across England. Total deaths and current patients in hospital across England too. There is a news headline where relevant and current Covid news is displayed. The most recent and up to date data is displayed using the publichealthengland COVID-19 API Service



# **Installation**
You will need to import the following modules in order to run the program.  They are:
* csv 
* sched
* time
* logging
* uk_covid19
* json
* requests


# **Info**
The program is designed to run on python 3.9.7

There is a config file called config.json -  where you can input your API key. You can get an API key from https://newsapi.org/
You can also put a title in there, to customize your dashboard too.

All errors are logged to a file called logging.log


# **Usage**
To run the program run website.py from the python terminal

Next on a web browser go to http://127.0.0.1:5000/index 

# **Testing**
There are 2 testing files to make sure functions return correct values and data types

# **Developer**
James White - ECM1400 University of Exeter



