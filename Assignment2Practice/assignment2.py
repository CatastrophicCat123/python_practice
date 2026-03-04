class TemperatureData:
    # Constructor to create object
    def __init__(self, name, readings):
        self.name = name
        self.readings = readings
    
    # Calculate average temperatures
    def calculate_average_temp(self):
        return sum(self.readings) / len(self.readings)
    
    # Find highest temperature
    def find_high_temp(self):
        return max(self.readings)
    
    # Find lowest temperature
    def find_low_temp(self):
        return min(self.readings)
    
    def find_temperature_range(first, second):
        if first > second:
            return first - second
        else:
            return second - first
        
# Example Usage
# Create a name for a sensor
sensor_name = "East Forest Road Sensor"

sensor = TemperatureData(sensor_name, [75, 71, 68, 64, 88])

average_temp = sensor.calculate_average_temp()
print(f"Average temperature for sensor {sensor_name}: {average_temp} degrees Fahrenheit")

highest = sensor.find_high_temp()
lowest = sensor.find_low_temp()
print(f"Temperature extremes for sensor {sensor_name}: Highest {highest}, Lowest {lowest}") 

range = sensor.find_temperature_range(lowest, highest)
print(f"Temperature range for sensor {sensor_name}: {range} degrees Fahrenheit")