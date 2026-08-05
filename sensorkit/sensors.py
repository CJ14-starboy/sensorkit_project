"""
Module: sensorkit/sensors.py
Contributor: <Sedinam Kwesi Gbedasi Honu>
Student ID: <68862029>
Date: <5th August, 2026>
Role: Provide concrete sensor classes built on the Sensor base class.

Each class must implement both abstract methods: read() and units().
Complete the TODOs below.
"""
from .base import Sensor
from abc import ABC, abstractmethod

class Thermocouple(Sensor):
    #@abstractmethod
    def read(self, raw):
        return raw * 24.9 - 0.4
        
    #@abstractmethod
    def units(self):
        return 'C'
    

class PressureGauge(Sensor):
    #@abstractmethod
    def read(self, raw):
        return raw * 2.5
        
    #@abstractmethod
    def units(self):
        return 'bar'


class StrainGauge(Sensor):
    #@abstractmethod
    def read(self, raw):
        return raw * 1000

    #@abstractmethod
    def units(self):
        return 'microstrain'
        


# TODO (optional, only if you have time):
# Add a third class StrainGauge where read(raw) returns raw * 1000
# and units() returns "microstrain".
