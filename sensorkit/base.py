"""
Module: sensorkit/base.py
Contributor: Caleb Adu-Ntim
Student ID: 36612029
Date: 05/08/2026
Role: Define the abstract Sensor base class that every sensor must follow.

Complete the TODOs below.
"""
from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, name):
        # TODO: store the argument `name` on the instance as self.name
        self.name = name

    # TODO : make read and units abstract
    @abstractmethod
    def read(self, raw):
        """Convert a raw signal value into a calibrated reading."""
        pass

    @abstractmethod
    def units(self):
        """Return this sensor's unit string, e.g. 'C' or 'bar'."""
        pass

    def describe(self):
        """Concrete method shared by all sensors."""
        # TODO : print one line in the form:
        #         "<name> sensor, measured in <units>"
        return f"{self.name} sensor, measured in {self.units()}"

