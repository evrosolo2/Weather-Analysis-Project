class DataCalculator:

    def __init__(self, weather_data, file_path):
        self.weather_data = weather_data
        self.file_path = file_path

    def __call__(self):
        if self.weather_data is None or 'temperatures' not in self.weather_data or 'weather' not in self.weather_data or 'precipitations' not in self.weather_data:
            print("Invalid weather data.")
            exit(1)

        average_temp = self.calculate_average_temperature()
        max_temp = self.calculate_maximum_temperature()
        min_temp = self.calculate_minimum_temperature()
        average_precipitation = self.calculate_average_precipitation()
        weather_summary = self.summarize_weather_conditions()
        self.display_results(average_temp, max_temp, min_temp, average_precipitation, weather_summary)

    def calculate_average_temperature(self):
        count = 0
        for num in self.weather_data["temperatures"]:
            count += int(num)
        return str(round(count / len(self.weather_data["temperatures"])))

    def calculate_maximum_temperature(self):
        temp = "0"
        for num in self.weather_data["temperatures"]:
            if int(num) > int(temp):
                temp = num
        return temp

    def calculate_minimum_temperature(self):
        temp = "5000"
        for num in self.weather_data["temperatures"]:
            if int(num) < int(temp):
                temp = num
        return temp

    def calculate_average_precipitation(self):
        count = 0.0
        for num in self.weather_data["precipitations"]:
            count += float(num.strip())
        return str(round((float(count / len(self.weather_data["precipitations"]))), 2))

    def summarize_weather_conditions(self):
        weather_type = {
            # "sunny": 0,
            # "snowy": 0,
            # "partly cloudy": 0,
            # "rainy": 0,
            # "overcast": 0
        }
        for condition in self.weather_data["weather"]:
            try:
                if condition == 'sunny':
                    weather_type["sunny"] = weather_type["sunny"] + 1
                elif condition == 'snowy':
                    weather_type["snowy"] = weather_type["snowy"] + 1
                elif condition == 'overcast':
                    weather_type["overcast"] = weather_type["overcast"] + 1
                elif condition == 'rainy':
                    weather_type["rainy"] = weather_type["rainy"] + 1
                elif condition == 'partly cloudy':
                    weather_type["partly cloudy"] = weather_type["partly cloudy"] + 1
            except KeyError:
                weather_type[condition] = 1
        return weather_type

    def display_results(self, average_temp, max_temp, min_temp, average_precipitation, weather_summary):
        text = f'Average Temperature: {average_temp}\n'
        text += f'Maximum Temperature: {max_temp}\n'
        text += f'Minimum Temperature: {min_temp}\n'
        text += f'Average Precipitation: {average_precipitation}\n'
        text += f'Weather Summary: {weather_summary}'
        with open(self.file_path, "w") as f:
            f.write(text)