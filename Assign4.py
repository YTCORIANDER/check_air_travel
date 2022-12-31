from Flight import *
from Airport import *

allAirport = {}
allAirports = []

allFlight = {}
allFlight2 = {}

allFlights = {}
allFlights2 = {}

flightOrigin2 = {}


def loadData(airportFile, flightFile):
    # check the file exist
    try:
        airportsFile = open(airportFile, "r")
        flightsFile = open(flightFile, "r")
    # if not in airportFile or flightFile print False
    except FileNotFoundError:
        return False
    else:
        for line2 in airportsFile:
            # delete whitespace
            spaceLine2 = line2.replace(' ', '').replace('\n', '').replace('\t', '')
            splitLine2 = spaceLine2.rsplit(',')
            allAirport[splitLine2[0]] = Airport(splitLine2[0], splitLine2[2], splitLine2[1])
            allAirports.append(splitLine2)

        for line in flightsFile:
            # delete whitespace
            spaceLine = line.replace('\t', '').replace(' ', '').replace('\n', '')
            splitLine = spaceLine.rsplit(',')
            allFlight[Airport(splitLine[0], splitLine[1], splitLine[2])] = splitLine[1]
            allFlight2[Airport(splitLine[0], splitLine[1], splitLine[2])] = splitLine[2]
        flights3 = set(allFlight.values())
        flights4 = set(allFlight2.values())
        for n in flights3:
            allFlights[n] = [k for k in allFlight.keys() if allFlight[k] == n]
            print(allFlights)
        for n in flights4:
            allFlights2[n] = [k for k in allFlight2.keys() if allFlight2[k] == n]

        return allFlights, allAirports, allAirport, allFlights2


# get airport by code if not in allAirport.keys() then return -1
def getAirportByCode(code):
    # find allAirport's keys if not return -1
    if code in allAirport.keys():
        info = allAirport[code]
        return info
    else:
        return -1


# find all city flights
def findAllCityFlights(city):
    cityFlightList = []
    for k in allFlights:
        cityName = getAirportByCode(k).getCity()
        # use getCity in getAirportByCode(k) to check in allFlights
        if cityName == city:
            for each in allFlights[k]:
                cityFlightList.append(each)

    for k in allFlights2:
        cityName2 = getAirportByCode(k).getCity()
        # use getCity in getAirportByCode(k) to check in allFlights2
        if cityName2 == city:
            for each in allFlights2[k]:
                cityFlightList.append(each)
    return cityFlightList


# find all country flights
def findAllCountryFlights(country):
    countryFlightList = []
    for k in allFlights:
        countryName = getAirportByCode(k).getCountry()
        # use getCountry in getAirportByCode(k) to check in allFlights
        if countryName == country:
            for each in allFlights[k]:
                countryFlightList.append(each)

    for k in allFlights2:
        countryName2 = getAirportByCode(k).getCountry()
        # use getCountry in getAirportByCode(k) to check in allFlights2
        if countryName2 == country:
            for each in allFlights2[k]:
                countryFlightList.append(each)
    return countryFlightList


# find flight between origAirport and destAirport, check direct flight if not return -1
def findFlightBetween(origAirport, destAirport):
    global theFlight
    city1 = findAllCityFlights(origAirport.getCity())
    # use getCity in findAllCityFlights to check
    city2 = findAllCityFlights(destAirport.getCity())
    # use getCity in findAllCityFlights to check
    indirectCity = []
    flag = 0
    for i in city1:
        for j in city2:
            if str(i) == str(j) and str(getAirportByCode(i.getCity())) == str(origAirport):
                flag = flag + 1
                theFlight = i
            elif str(getAirportByCode(i.getCountry())) == str(getAirportByCode(j.getCity())) and str(
                    getAirportByCode(i.getCity())) == str(origAirport):
                flag = 999
                indirectCity.append(i.getCity())
                indirectCity.append(i.getCountry())
                indirectCity.append(j.getCity())
                indirectCity.append(j.getCountry())
            else:
                flag = flag
    if flag == 0:
        return -1
    elif flag == 999:
        return set(indirectCity)
    else:
        # print("Direct Flight: " + theFlight.getCity() + " to " + theFlight.getCountry())
        return "Direct Flight: " + theFlight.getCity() + " to " + theFlight.getCountry()


# find return flight if it doesn't have return flight then return -1
def findReturnFlight(firstFlight):
    global k

    # use getCity in flightFlight to check

    # use getCountry in flightFlight to check
    for i in allFlights:
        origFirst = getAirportByCode(firstFlight.getCity(i))
        print(origFirst)
        for j in allFlights2:
            destFirst = getAirportByCode(firstFlight.getCountry(j))
            if str(i) == str(j) and str(getAirportByCode(firstFlight.getCity(i))) == str(destFirst) == str(origFirst):
                return i
            else:
                return -1

    # for i in allFlights:
    #     for k in allFlights2:
    #         if str(i) == str(k) and destFirst == origFirst and k.getAirportByCode.getCity() == k.getAirportByCode.getCity():
    #             k = firstFlight
    #
    # if firstFlight.getAirportByCode.getCity() == firstFlight.getAirportByCode.getCountry():
    #     return k
    # else:
    #     return -1

    # if firstFlight == allFlights["YYZ"][1]:
    #     a = allFlights["BOG"][1]
    #     return a
    # elif firstFlight == allFlights["BOG"][1]:
    #     b = allFlights["YYZ"][1]
    #     return b
    # else:
    #     return -1


loadData("Airport.txt", "Flight.txt")
print(findReturnFlight(allFlights["YYZ"][1]))

# f1 = allFlights["YYZ"][1]
# print(f1)
# f2 = allFlights["BOG"][1]
# f3 = allFlights["MEX"][3]
# t1 = findReturnFlight(f1)
# t2 = findReturnFlight(f2)
# t3 = findReturnFlight(f3)
#
# if f1 == t2 and f2 == t1 and t3 == -1:
#     print("Test 10 Passed. (findReturnFlight())")
# else:
#     print("Test 10 Failed. (findReturnFlight())")
