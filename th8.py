import threading
import time

class Generator:
    def print_numbers(self, name, start_at, limit):
        for i in range(start_at, limit + 1, 2):
            print(f"{name}: {i}")
            time.sleep(0.1) # Small pause so we can see them "racing"

#the object
gen = Generator()
even_thread = threading.Thread(target=gen.print_numbers, args=("EVEN", 0, 10))
odd_thread = threading.Thread(target=gen.print_numbers, args=("ODD", 1, 10))
even_thread.start()
odd_thread.start()