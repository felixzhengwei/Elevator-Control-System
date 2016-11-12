#Assumptions made on the elevators:
#1. The building has a max of 100 floors
#2. The elevators run in unison and stop at their respective floors the same time.
#3. To simulate a real system, we will input the destination floor when an pickup request is picked up and use that information for when the passenger has been actually picked up

class Elevator(object):

    def __init__(self, id):
        self.id = id
        self.upQueue = []
        self.downQueue = []
        self.floor = 0
        self.direction = 0

    def updateFloor(self, floor):
        self.floor = floor
        self.checkArrival(floor, direction)

    def checkArrival(self, floor, direction):
        if self.direction > 0:
            if self.upQueue and (floor == self.upQueue[0]):
                while floor == self.upQueue[0]:
                    self.upQueue.pop(0)
                    if not self.upQueue:
                        break
        elif self.direction < 0:
            if self.downQueue and (floor == self.downQueue[0]):
                while floor == self.downQueue[0]:
                    self.downQueue.pop(0)
                    if not self.upQueue:
                        break
        if (not self.upQueue) and (not self.downQueue):
            self.setDirection(0)
        if (not self.upQueue) and self.downQueue:
            self.setDirection(-1)


    def addUpQueueFloor(self, floorArray):
        self.upQueue.extend(floorArray)
        self.upQueue.sort()

    def addDownQueueFloor(self, floorArray):
        self.downQueue.extend(floorArray)
        self.downQueue.sort(reverse=True)

    def moveOneStep(self):
        if self.direction > 0 and self.floor < 100:
            self.floor+=1
        elif self.direction < 0 and self.floor > 0:
            self.floor-=1
        self.checkArrival(self.floor, self.direction)

    def currentState(self):
        if self.direction == 0:
            print "Elevator", self.id, "at", self.floor, "floor, is empty"
        elif self.direction > 0:
            print "Elevator" , self.id , "at" , self.floor , "floor, going up to " , self.upQueue
        else:
            print "Elevator" , self.id , "at" , self.floor , "floor, going down to " , self.downQueue

    def getFloor(self):
        return self.floor

    def getDirection(self):
        return self.direction

    def setDirection(self, number):
        self.direction = number
