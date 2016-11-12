# Coding Challenge
Elevator system to handle and perform pickup requests up to 16 elevators.

The interface provides 4 major functions: adding pickup requests, step simulating the system, querying the state of the system, and updating each elevator.  

## scheduling
The system handles pickup requests by using 2 hashmaps, one for requests going up and one for requests going down. The pick up floors are stored as the keys and the destination floors are stored as an array for those particular key values.

Each individual elevator has its own up and down queues and the system will schedule the pickup requests by adding different requests to different elevator's down or up queues. There are three main cases being considered:

1. The first case is when a user requests to go up or down and there is already an elevator on the same floor, if this is the case then the system will simply append the destination floors to that elevator and continue operating.
2. The second case is when there are no elevators on the current floor the user is being picked up at but there is at least one elevator passing through that floor in the given direction. The system will calculate the shortest distance between the elevators and append the destination floors to that specific elevator.
3. If no elevators are on the current floor and no elevator is passing through the floor, then the request will be held in the queue until at least one elevator finishes operating.

The switching of directions for the elevators is implemented inside each individual elevator class.

# Assumptions
1. The building is assumed to have 100 floors.
2. The elevators run in unison and stop at their respective floors the same time, the system neglects pick up and drop off time for each elevator.
3. To simulate a real system, we will input the destination floor when an pickup request is picked up and use that information for when the passenger has been actually picked up


## Running the application
Navigate to the src directory and run:
```
python main.py
```
The program will prompt for inputs starting from there, there are no error checks currently implemented in the program, so please make sure to enter valid commands.
