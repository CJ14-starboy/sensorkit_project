"""
Driver script for the sensorkit package.
Run it from the project root folder:

    python main.py

Feel free to swap in a different sensor once all modules are complete.
"""
from sensorkit import Thermocouple, load_readings, summarise


def main():
    raw = load_readings("readings.csv")

    tc = Thermocouple("Furnace TC1")
    tc.describe()
    summarise(tc, raw)


if __name__ == "__main__":
    main()
