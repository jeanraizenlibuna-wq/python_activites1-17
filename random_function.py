import random
import time
fruits = ["Apple", "banana", "mango", "rambutan", "SANTOL"]

fruit_choice = random.choice(fruits)
random_num = random.randint(1,10)
print("random number:  ",random_num)
time.sleep(1)
print("random fruit:   ", fruit_choice)