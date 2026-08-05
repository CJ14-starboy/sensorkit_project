"""
Module: sensorkit/dataio.py
Contributor: <full name>
Student ID: <id>
Date: <date>
Role: Load raw sensor readings from a text/CSV file, safely.

Uses pathlib for the file path and exceptions to handle problems.
Complete the TODOs below.
"""
from pathlib import Path


def load_readings(filepath):
    """
    Read a file of raw numeric readings, one value per line, and return
    a list of floats.

    Rules:
      - If the file does not exist, raise FileNotFoundError.
      - Ignore blank lines.
      - If a line is not a valid number, skip it and print a short message
        instead of letting the program crash.
    """
    path = Path(filepath)

    # TODO : if the path does not exist, raise FileNotFoundError
    #
    
    if path.exists():
        
        readings = []
        #TODO : Complete the loop to read in the file content
            # TODO : try to convert `line` to a float and append it to readings.
            #         If it raises ValueError, print:
           #         f"Skipping invalid line: {line!r}"
        with open(filepath,'r') as file:
            try:
                for line in file:
                    lines=line.strip()
                    if not lines:
                        continue
                
                    reading=float(lines)
                    readings.append(reading)
                    
            except ValueError:
                    print(f'Skipping invalid line: {line!r}')


        return readings
    else:
        raise FileNotFoundError


