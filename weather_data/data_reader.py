import json
import csv


class DataReader:

    def __init__(self, file_type, file_path):
        self.file_type = file_type
        self.file_path = file_path

    def __call__(self):
        if self.file_type == 'json':
            return self.read_weather_data_json()
        elif self.file_type == 'csv':
            return self.read_weather_data_csv()

    def read_weather_data_json(self):
        with open(self.file_path, "r") as f:
            read = f.read()
            temperatures = []
            weather = []
            precipitations = []
            new_read = read.split("{")
            for i in range(1, len(new_read)):
                if not ("temperature" in new_read[i] and "weather" in new_read[i] and "precipitation" in new_read[i]):
                    raise ValueError
            temp_read = read.split("temperature")
            temp_read.remove(temp_read[0])
            for item in temp_read:
                item = item.replace(",", "")
                temp_val = item[2:5]
                temperatures.append(temp_val)
            weather_read = read.split("weather")
            weather_read.remove(weather_read[0])
            for item in weather_read:
                item = item.replace(",", "")
                weather_val = item[4:6]
                if weather_val == "su":
                    weather.append("sunny")
                elif weather_val == "sn":
                    weather.append("snowy")
                elif weather_val == "ra":
                    weather.append("rainy")
                elif weather_val == "ov":
                    weather.append("overcast")
                elif weather_val == "pa":
                    weather.append("partly cloudy")
            pre_read = read.split("precipitation")
            pre_read.remove(pre_read[0])
            for item in pre_read:
                item = item.replace(",", "")
                pre_val = item[2:6]
                precipitations.append(pre_val)
            reader = {
                "temperatures": temperatures,
                "weather": weather,
                "precipitations": precipitations
            }
            return reader

    def read_weather_data_csv(self):
        with open(self.file_path, "r") as f:
            read = f.readline()
            new_read = read.split(",")
            if new_read[0] == "temperature" and new_read[1] == "weather" and new_read[2].strip() == "precipitation":
                temperatures = []
                weather = []
                precipitations = []
                for line in f:
                    csv_lines = line.split(",")
                    temperatures.append(csv_lines[0])
                    weather.append(csv_lines[1])
                    precipitations.append(csv_lines[2])
                reader = {
                    "temperatures": temperatures,
                    "weather": weather,
                    "precipitations": precipitations
                }
                return reader
            else:
                raise ValueError

