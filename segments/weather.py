# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division,
                        absolute_import, print_function)

import json

from urllib.parse import quote
from powerline.lib.url import urllib_read
# from powerline.lib.threaded import KwThreadedSegment
# from powerline.segments import with_docstring


weather_conditions_icons = {
    1000: "\ue30c",  # Sunny
    1003: "\ufa94",  # Partly cloudy
    1009: "\ue30c",  # Overcast
    1030: "\uf74e",  # Mist
    1183: "\ue316",  # Light rain
    1240: "\ue316",  # Light rain shower
    1273: "\ue31d",  # Light rain with thunder
    1276: "\ue31d",  # Light rain with thunder
}


def weather_test():
    url = 'http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no'.format(
        location=quote("Ho Chi Minh"), key="531082296db146a8a9c164828221907")
    raw_response = urllib_read(url)
    response = json.loads(raw_response)
    current = response['current']
    condition_code = (current['condition']['code'])
    temp = current['temp_c']
    icon = weather_conditions_icons[condition_code]
    feelslike = current['feelslike_c']
    humidity = current['humidity']
    print(temp, feelslike, humidity, icon)


# weather_test()


def weather(pl, key="531082296db146a8a9c164828221907", location="Ho Chi Minh"):
    url = 'http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no'.format(
        location=quote(location), key=key)
    raw_response = urllib_read(url)
    response = json.loads(raw_response)
    current = response['current']
    condition_code = int(current['condition']['code'])
    temp = current['temp_c']
    icon = weather_conditions_icons[condition_code]
    feelslike = current['feelslike_c']
    humidity = current['humidity']
    return [{

        'contents': "{icon} {temp} FL:{feelslike} H:{humidity}".format(icon=icon, temp=temp, feelslike=feelslike, humidity=humidity),
        'highlight_groups': ['weather'],
    }]
