# Write a class CITY in Python with following specification :
# Code # Numeric value
# Name # String value
# Pop # Numeric value for Population
# KM # Numeric value
# Density # Numeric value for Population Density


# Methods:
# CalDen ( ) # Method to calculate Density as Pop /KM
# Record ( ) # Method to allow user to enter values Code, Name, Pop, KM and call CalDen ( ) method
# See ( ) # Method to display all the date members also display a message “Highly Populated Area” is the Density is more than 12000.


class City:

    def CalDen(self):
        self.density = self.pop / self.km

    def record(self, code, name, pop, km):
        self.code = code
        self.name = name
        self.pop = pop
        self.km = km
        self.CalDen()

    def see(self):

        if self.density > 12_000:
            return ("Highly Populated Area")
        else:
            return ("Population is goed!")


amsterdam = City()

amsterdam.record(123,"Amsterdam", 5_000_000, 50)

print(amsterdam.see())

