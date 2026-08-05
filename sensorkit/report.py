"""
Module: sensorkit/report.py
Contributor: Abner Nikoi Ashie
Student ID: 11262029
Date: 5 August, 2026
Role: Produce a printed summary of calibrated readings for one sensor.

This module ties together a sensor (from sensors.py) and the statistics
functions (from stats.py). Complete the TODOs below.
"""
from .stats import mean, minimum, maximum, spread


def summarise(sensor, raw_readings):
    try:
       with open(raw_readings, 'r') as raw_readings:
            count =1
            cal_list = []
            for r in raw_readings:
               cal_list.append(sensor.read(r))
               count+=1
            u = sensor.units() 
            mean = mean(cal_list)
            minmum = minimum(cal_list)
            maximum = maximum(cal_list)
            spread = spread(cal_list)
            
            print(f"Report for {sensor.name}")
            print(f"    count:   {count}")
            print(f"    mean:   {cal_list.mean()}{u}")
            print(f"    min:       {minimum}{u}")
            print(f"    max:      {maximum}{u}")
            print(f'    spread:  {spread}{u}')

    except FileNotFoundError as err :
         print(err)
