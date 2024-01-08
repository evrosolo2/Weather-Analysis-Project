import sys
import os
from weather_data.data_reader import DataReader
from weather_data.data_calculator import DataCalculator

def main():
    try:
        if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]) and (sys.argv[1][:-3] == "csv" or sys.argv[1][:-4] == "json"):
            reader = DataReader(sys.argv[1][8:], sys.argv[1])
            weather_data = reader()
            calculator = DataCalculator(weather_data, sys.argv[2])
            calculator()
        else:
            exit(1)
    except IndexError:
        exit(1)



if __name__ == "__main__":
    main()


