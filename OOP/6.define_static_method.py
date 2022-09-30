class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c/5 +32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f-32)/9


f = TemperatureConverter.celsius_to_fahrenheit(30)
print(f)

f1 = TemperatureConverter.fahrenheit_to_celsius(100)
print(f1)
