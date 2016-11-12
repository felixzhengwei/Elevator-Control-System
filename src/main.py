from System import System

number = input("Enter the number of elevators in the system, up to 16: ")
system = System(number)
end = False

while not end:
    command = input("Enter commands:\n Enter 1 for adding pick up request,\n Enter 2 for step simulating the system,\n Enter 3 to query the state of the system,\n Enter 4 to exit the system.\n")
    if command == 1:
        floor = input("Enter floor to be picked up: ")
        direction = input("Enter direction, 1 for up and -1 for down: ")
        finalFloor = input("Enter destination floor: ")
        system.pickup(floor, direction, finalFloor)
    elif command == 2:
        print("Simulating...\nDone")
        system.step()
    elif command == 3:
        system.query()
    elif command == 4:
        end = True
    else:
        print('invalid command')
