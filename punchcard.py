#!/usr/bin/env python

from datetime import datetime
import pygal
from pygal.style import DarkSolarizedStyle
import json

days_lookup = ["monday",  "tuesday", "wednesday", "thursday", "friday",\
        "saturday", "sunday"]
days_order = [6,0,1,2,3,4,5]
hours_order = ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00",\
        "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00",\
        "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",\
        "22:00", "23:00"]

def draw_graph(days_dict):
    dot = pygal.Dot(x_label_rotation=20, show_legend=False, style=DarkSolarizedStyle)
    dot.title = "Git Commits by time of day"
    dot.x_labels = hours_order
    for day in days_order:
        print days_dict[day]
        dot.add(days_lookup[day], days_dict[day])
    dot.render_to_file("punchcard.svg")

def setup_days_dict():
    hours = [0 for x in range(24)]
    days_dict = {}
    for x in range(7):
        days_dict[x] = list(hours)
    return days_dict

def bin_dates(dates):
    days_dict = setup_days_dict()
    for date in dates:
        # Python does not have support for timezones in datetime.. huh
        dt = datetime.strptime(date[:19], "%Y-%m-%d %H:%M:%S")
        #print days_dict[dt.weekday()][dt.hour]
        days_dict[dt.weekday()][dt.hour] += 1
    return days_dict

with open("log.json") as r:
    git_log = json.loads(r.read())

dates = []
for commit in git_log:
    dates.append(commit["date"])

days_dict = bin_dates(dates)
draw_graph(days_dict)
