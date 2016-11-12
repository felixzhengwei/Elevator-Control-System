#Querying the state of the elevators (what floor they are on and where they are going),
# receiving an update about the status of an elevator,
# receiving a pickup request,
# time-stepping the simulation.

from Elevator import Elevator

class System(object):

    pickUpUpQueue = {}
    pickUpDownQueue = {}
    #create 16 elevators
    def __init__(self, number):
        self.elevatorList = []
        self.requests = []
        for i in range(number):
            obj = Elevator(i)
            self.elevatorList.append(obj)

    def query(self):
        for i in self.elevatorList:
            print i.currentState()

    def update(self, upQueue, downQueue):
        #going up
        #check to see if anyone required pick up is on the same floor
        if upQueue:
            for i in self.elevatorList:
                if upQueue.has_key(i.getFloor()) and i.getDirection() >= 0:
                    i.addUpQueueFloor(upQueue[i.getFloor()])
                    if i.getDirection() == 0:
                        i.setDirection(1)
                    del upQueue[i.getFloor()]

            #if there are still passengers waiting see where the closest elevator is, see if any elevators are going through
            for key in upQueue.keys():
                lowest = 101
                index = 17
                for i in self.elevatorList:
                    if i.getDirection() >= 0 and key > i.getFloor():
                        diff = key - i.getFloor()
                        if diff < lowest:
                            lowest = diff
                            index = i.id
                if index != 17:
                    self.elevatorList[index].addUpQueueFloor([key])
                    self.elevatorList[index].addUpQueueFloor(upQueue[key])
                    if self.elevatorList[index].getDirection() == 0:
                        self.elevatorList[index].setDirection(1)
                    del upQueue[key]

            #if the user requested up but all elevators are currently above the floor, wait till the elevator is out of business and check again
            for key in upQueue.keys():
                for i in self.elevatorList:
                    if i.getDirection() == 0:
                        i.setDirection(-1)
                        i.addDownQueueFloor([key])
                        i.addUpQueueFloor(upQueue[key])
                        del upQueue[key]
                        break

        #going down
        #check to see if anyone required pick up is on the same floor
        if downQueue:
            for i in self.elevatorList:
                if downQueue.has_key(i.getFloor()) and i.getDirection() <= 0:
                    i.addDownQueueFloor(downQueue[i.getFloor()])
                    if i.getDirection() == 0:
                        i.setDirection(-1)
                    del downQueue[i.getFloor()]

            #see if any elevators are passing through
            for key in downQueue.keys():
                lowest = 101
                index = 17
                for i in self.elevatorList:
                    if i.getDirection() <= 0 and key < i.getFloor():
                        diff = i.getFloor - key
                        if diff < lowest:
                            lowest = diff
                            index = i.id
                if index != 17:
                    self.elevatorList[index].addDownQueueFloor([key])
                    self.elevatorList[index].addDownQueueFloor(downQueue[key])
                    if self.elevatorList[index].getDirection() == 0:
                        self.elevatorList[index].setDirection(1)
                    del downQueue[key]

            #if all elevators are below where the floor is
            for key in downQueue.keys():
                for i in self.elevatorList:
                    if i.getFloor() < key and i.getDirection() <= 0:
                        i.addUpQueueFloor([key])
                        i.setDirection(1)
                        i.addDownQueueFloor(downQueue[key])
                        del downQueue[key]
                        break

    def pickup(self, floor, direction, goalFloor):
        if direction > 0:
            if self.pickUpUpQueue.has_key(floor):
                self.pickUpUpQueue[floor]+=[goalFloor]
            else:
                self.pickUpUpQueue[floor]=[goalFloor]
        else:
            if self.pickUpDownQueue.has_key(floor):
                self.pickUpDownQueue[floor]+=[goalFloor]
            else:
                self.pickUpDownQueue[floor]=[goalFloor]

    def step(self):
        for i in self.elevatorList:
            i.moveOneStep()
        self.update(self.pickUpUpQueue, self.pickUpDownQueue)
