import threading
import time

# Define a function to be executed by each thread
def print_messages(delay, message, stop_event):
    while not stop_event.is_set():
        print(message)
        time.sleep(delay)

# Create a shared flag variable to control thread termination
stop_flag = threading.Event()

# Create two threads
thread1 = threading.Thread(target=print_messages, args=(1, "Thread 1: Hello!", stop_flag))
thread2 = threading.Thread(target=print_messages, args=(2, "Thread 2: Hi!", stop_flag))

# Start the threads
thread1.start()
thread2.start()

# Let the threads run for a while
time.sleep(5)

# Set the stop flag to signal threads to stop
stop_flag.set()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread exiting.")
