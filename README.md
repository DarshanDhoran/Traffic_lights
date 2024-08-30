1. Import the time Module: The time module provides the sleep() function, which is used to pause the program execution for a specific duration.

2. Define Traffic Light States: We create a list, traffic_lights, containing three states: "Red", "Green", and "Yellow".

3. Initialize State Index: We initialize current_state_index to 0 to keep track of the current traffic light state.

4. Infinite Loop: The while True loop creates an infinite loop that will run continuously.

5. Get and Print Current State: In each iteration, we retrieve the current traffic light state using the current_state_index and print it.

6. Pause Execution: The time.sleep(30) function pauses the execution for 30 seconds, simulating the time delay between light changes.

7. Move to the Next State: We update current_state_index to move to the next state. The modulo operator (%) ensures that the index cycles back to 0 after reaching the end of the list.


Running the Program
This program will continuously change the traffic light state every 30 seconds, printing the current state to the console.
