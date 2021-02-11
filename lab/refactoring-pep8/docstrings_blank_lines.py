# by Kami Bigdely
# Docstrings and blank lines
""" This file is designed for the functionaility of a carbon monoxide sensor"""

class OnBoardTemperatureSensor:
    """Returns the temperature of the onboard temperature sensor."""
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        pass

    def read_voltage(self):        
        return 2.7

    def get_temperature(self):
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
  
class CarbonMonoxideSensor:
    """Returns the current carbon monoxide level

        This class uses the sensor to return a carbon monoxide level using
        the voltage, temperature, and voltage to carbon factor in order to
        calulate the carbon monoxide level
    """
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        """Inittializer creates instance of the temperature sensor."""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Returns the carbon monoxide lebel from the sensor"""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = self.convert_voltage_to_carbon_monoxide_level
                               (sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Sensor voltage"""
        # In real life, it should read from hardware.        
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        """Converts the sensors voltage to carbon monoxide level"""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    def __init__(self):
        self.string = ''

    def display(self,msg):
        """Creates the display"""
        print(msg)

class CarbonMonoxideDevice():
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit  

    def Display(self):
        """Shows what the monoxide level is"""
        msg = 'Carbon Monoxide Level is : ' +  str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
    