import requests# allows us to use the json module
import ast# to convert response to a dict.
import datetime# allows us to use the date time module


key = {'token': '31ffebf069ebed28cd2ceb3b62ad6787'}#request

dictionary = requests.post('http://challenge.code2040.org/api/dating', json = key)#Gives me back a response

print(dictionary)

time = ast.literal_eval(dictionary.text) #converting the request to a time Dict
#format for the time object
timeFormat = '%Y-%m-%dT%H:%M:%SZ'
# storing the date and the seconds
date = time['datestamp']
secondsInterval = time['interval']

#storing the time, extracting the string from our time object
time = datetime.datetime.strptime(date, timeFormat)

# adding our seconds to the time object
time = time + datetime.timedelta(seconds = secondsInterval)
result = time.isoformat()
result = str(result) + 'Z'

timeResult = {'token': '31ffebf069ebed28cd2ceb3b62ad6787', 'datestamp' :result}# datestamp for an ISO 8601 datestamp string
timeResult = requests.post('http://challenge.code2040.org/api/dating/validate', json = timeResult)

print(timeResult.text)
