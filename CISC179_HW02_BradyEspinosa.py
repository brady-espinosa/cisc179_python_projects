''' Brady Espinosa
     Date: 12/10/2024
     Homework 02
     The program simulates the movement of five cars (named "Car 1" to "Car 5") in a race.
     The program displays the progress of each car using dashes ('-') on the console screen.
     The position of each car is visually represented by the number of dashes, and the current position is shown in parentheses.
     The race continues until one of the cars reaches or passes a specified finish line distance (currently set to 50 meters). 
     The winning car is declared when this condition is met.
'''


import random
import os
import time


class Car:
    def __init__(self, name) -> None:
        self.name = name
        self.pos = 0
        self.speed = random.randint(1, 5)

    def move(self):
        self.pos += self.speed
        self.speed = random.randint(1, 5)
        
    

class Race:
    def __init__(self, car_list, finish=50) -> None:
        self.car_list = car_list
        self.finish = finish

    def display_race(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Car race simulation')
        for car in self.car_list:
            print(f"{car.name}: {'-' * car.pos} ({car.pos})")
    
    def run(self):
        while True:
            for car in self.car_list:
                car.move()
                if car.pos >= self.finish:
                    self.display_race()
                    print(f"{car.name} wins the race!")
                    print('Simulation ended.')
                    return  
            self.display_race()  
            time.sleep(0.5)  

car_list = [Car(f"Car {i+1}") for i in range(5)]

race1 = Race(car_list)
race1.run()