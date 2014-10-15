#!/usr/bin/env python

from datetime import datetime
import pygal
import json

days_order = ["sunday",  "monday",  "tuesday", "wednesday", "thursday",\
        "friday",  "saturday"]
hours_order = ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00",\
        "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00",\
        "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",\
        "22:00", "23:00"]

def draw_graph(days_dict):
    dot = pygal.Dot(x_label_rotation=20, show_legend=False)
    dot.title = "Week of Commits"
    dot.x_labels = hours_order
    for day in days_order:
        print days_dict[day]
        dot.add(day, days_dict[day])
    dot.render_to_file("punchcard.svg")

def bin_dates():
    hours = [1 for x in range(24)]
    days_dict = {\
            "sunday"   : list(hours),\
            "monday"   : list(hours),\
            "tuesday"  : list(hours),\
            "wednesday": list(hours),\
            "thursday" : list(hours),\
            "friday"   : list(hours),\
            "saturday" : list(hours)\
            }
    return days_dict

with open("log.json") as r:
    git_log = json.loads(r.read())
for commit in git_log:
    print commit.date

days_dict = bin_dates(dates)
draw_graph(days_dict)
