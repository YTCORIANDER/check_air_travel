class Airport:
    # set init information
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country
        self._airport = []

    # store raw information
    def __repr__(self):
        return str(self._code) + " (" + str(self._city) + ", " + str(self._country) + ")"

    # get code
    def getCode(self):
        return self._code

    # get flight number
    def getFlightNumber(self):
        return self._code

    # get city
    def getCity(self):
        return self._city

    # get country
    def getCountry(self):
        return self._country

    # set city
    def setCity(self, newCity):
        self._city = newCity

    # set country
    def setCountry(self, newCountry):
        self._country = newCountry
