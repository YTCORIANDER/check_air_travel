from Airport import *


class Flight:
    def __init__(self, flightNo, origin, destination):
        #check origin and destination in Airport
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError("the origin and destination must be airport objects")

    def __repr__(self):
        if str(self._origin._country) == str(self._destination._country):
            return "Flight: " + self._flightNo + " from " + str(self._origin._city) + " to " + str(
                self._destination._city) + " {domestic} "
        else:
            return "Flight: " + self._flightNo + " from " + str(self._origin._city) + " to " + str(
                self._destination._city) + " {international} "


    def __eq__(self, other):
        if str(self._origin) == str(other._origin) and str(self._destination) == str(other._destination):
            return True

    #get flight number
    def getFlightNumber(self):
        return self._flightNo

    #get origin
    def getOrigin(self):
        return self._origin

    #get destination
    def getDestination(self):
        return self._destination

    #check country in origin equal to country in destination
    def isDomesticFlight(self):
        if str(self._origin._country) == str(self._destination._country):
            return True

    #set origin
    def setOrigin(self, origin):
        self._origin = origin

    #set destination
    def setDestination(self, destination):
        self._destination = destination


