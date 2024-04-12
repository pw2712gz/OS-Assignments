# Ayub Yusuf
# Date: 4/09/2024
# Computer Operating Systems Assignment #7
# This program implements a producer and consumer model where both share an integer variable 'data'.
# The producer and consumer use a lock to ensure mutual exclusion when accessing 'data'.

import threading
import time
import random

# Shared variables
data = 0
lock = threading.Lock()


# Producer thread function
def producer():
    global data
    counter = 0
    while counter < 8:
        time.sleep(random.randint(1, 2))  # Random wait between 1 and 2 seconds
        with lock:  # Acquire the lock
            if data == 0:
                counter += 1
                if counter == 8:
                    data = -1  # Signal consumer to terminate
                else:
                    data = counter


# Consumer thread function
def consumer():
    global data
    total = 0
    while True:
        time.sleep(random.randint(1, 2))  # Random wait between 1 and 2 seconds
        with lock:  # Acquire the lock
            if data > 0:
                total += data
                data = 0
            elif data == -1:
                print("Ayub Yusuf\nComputer Operating Systems Assignment #7\nThe sum is", total)
                return  # Terminate thread


def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    main()
