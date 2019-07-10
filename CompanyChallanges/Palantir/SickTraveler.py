class Traveler:

    def __init__(self,travelerName,healthStatus,itinerary):
        self.travelerName = travelerName
        self.healthStatus = healthStatus
        self.itinerary = itinerary
        self.numberOfLocations = len(self.itinerary)
        self.daysSick = 0

    def updateHealthStatus(self):
        if(self.healthStatus == 'SICK' and self.daysSick == 0):
            self.daysSick += 1
        elif(self.healthStatus == 'SICK' and self.daysSick == 1):
            self.healthStatus = 'RECOVERING'
            self.daysSick = 0
        elif(self.healthStatus == 'RECOVERING'):
            self.healthStatus = 'HEALTHY'
    
    def isTravelerSick(self):
        return self.healthStatus == 'SICK' or self.healthStatus == 'RECOVERING'


class Location:

    def __init__(self,locationName):
        self.locationName = locationName
        self.travelerList = []
    
    def containsSickTraveler(self):
        
        isSomeoneSick = False

        for traveler in self.travelerList:
            if(traveler.isTravelerSick()):
                isSomeoneSick = True
                break
        return isSomeoneSick
    
    def makeEveryoneSick(self):

        for traveler in self.travelerList:
            if(not traveler.isTravelerSick()):
                traveler.healthStatus = 'SICK'
                
    
    def clearLocation(self):
        self.travelerList = []
    

class TripStarter:

    listOfTravelers = []
    listOfLocations = []
    MAX_DAYS = 365
    currentDay = 1

    def convertInputToObjects(self):

        numberOfLines = input()

        lineCounter = 0
        while(lineCounter < int(numberOfLines)):
            travelerData = input()
            cleanTravelerData = travelerData.split()

            travelerName = None
            travelerHealthStatus = None
            travelerItinerary = []

            travelerName, travelerHealthStatus, *travelerItinerary = cleanTravelerData
            for i in range(0,len(cleanTravelerData)):
                if(i == 0):
                    travelerName = cleanTravelerData[i]
                elif(i == 1):
                    travelerHealthStatus = cleanTravelerData[i]
                else:
                    locationName = cleanTravelerData[i]
                    travelerItinerary.append(locationName)
                    if(self.getLocationIndex(locationName) == None):
                        newLocation = Location(cleanTravelerData[i])
                        self.listOfLocations.append(newLocation)
                    
        
            newTraveler = Traveler(travelerName,travelerHealthStatus,travelerItinerary)
            if(newTraveler.healthStatus == 'SICK'):
                newTraveler.daysSick = 1

            self.listOfTravelers.append(newTraveler)
            locationIndex = self.getLocationIndex(newTraveler.itinerary[0])
            self.listOfLocations[locationIndex].travelerList.append(newTraveler)

            lineCounter += 1

    def getLocationIndex(self,searchName):
        for index,location in enumerate(self.listOfLocations):
            if(searchName == location.locationName):
                return index
        return None

    def moveTravlersToNextLocation(self):
        for city in self.listOfLocations:
            city.clearLocation()
        
        for traveler in self.listOfTravelers:
            nextIndex = self.currentDay % traveler.numberOfLocations
            nextLocationName = traveler.itinerary[nextIndex]

            nextLocationIndex = self.getLocationIndex(nextLocationName)
            if(nextLocationIndex != None):
                newLocation = self.listOfLocations[nextLocationIndex]
                newLocation.travelerList.append(traveler)

    def spreadSickness(self):
        for location in self.listOfLocations:
            if(location.containsSickTraveler()):
                location.makeEveryoneSick()
        
    def updateAllHealthStatuses(self):
        for traveler in self.listOfTravelers:
            traveler.updateHealthStatus()

    def isEveryOneHealthy(self):
        for traveler in self.listOfTravelers:
            if(traveler.isTravelerSick()):
                return False
        return True

    def printTravelersHealthStatus(self):
        output = ''
        for traveler in self.listOfTravelers:
            output += traveler.healthStatus + ' '
        print(output)
    
    def printTravlerNames(self):
        output = ''
        for traveler in self.listOfTravelers:
            output += traveler.travelerName + ' '
        print(output)

    def isTripNotOver(self):
        return self.currentDay < 365 and not self.isEveryOneHealthy()

    def startTravelling(self):

        self.convertInputToObjects()
        self.printTravlerNames()

        while(self.isTripNotOver()):
            self.printTravelersHealthStatus()
            self.spreadSickness()
            self.moveTravlersToNextLocation()            
            self.currentDay += 1
            self.updateAllHealthStatuses()
            

        self.printTravelersHealthStatus()
        print(self.currentDay)

trip = TripStarter()
trip.startTravelling()

            

