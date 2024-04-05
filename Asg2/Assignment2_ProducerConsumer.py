# Ayub Yusuf
# Computer Operating Systems Assignment #2
# February 9, 2024
# This program demonstrates the producer-consumer problem using threading in Python.
# The producer writes numbers 0 through 4 to a shared variable with random waits between writes.
# The consumer reads these values with random waits and sums them. The sum is then written to a file.

import threading
import time
import random

# Initialize shared variable and lock
shared_variable = 100
lock = threading.Lock()


def producer():
    global shared_variable
    for i in range(5):
        time.sleep(random.randint(1, 3))  # Random wait between 1 to 3 seconds
        with lock:
            shared_variable = i
            print(f"Producer: Writing {i} to shared variable.")


def consumer():
    sum = 0
    for _ in range(5):
        time.sleep(random.randint(1, 3))  # Random wait
        with lock:
            value = shared_variable
            print(f"Consumer: Reading {value} from shared variable.")
            sum += value

    # Append the sum to the output file for each run
    with open("output.txt", "a") as file:
        file.write("Ayub Yusuf\nComputer Operating Systems Assignment #2\n")
        file.write(f"The sum is {sum}\n")
        file.write("\n")  # Ensure separation between runs for readability


# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for threads to complete
producer_thread.join()
consumer_thread.join()

print("Program completed. Check 'output.txt' for the result.")
