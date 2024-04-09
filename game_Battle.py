import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.player = Hero("Player")
        self.computer = Hero("Computer")

    def start(self):
        print(f"Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
                print(f"{self.player.name}'атакует {self.computer.name}. Здоровье{self.computer.name}: {self.computer.health}")
                if not self.computer.is_alive():
                    print(f"{self.player.name} победил!")
                    break
            else:
                self.computer.attack(self.player)
            print(f"{self.computer.name}'атакует {self.player.name}. Здоровье{self.player.name}: {self.player.health}")
            if not self.player.is_alive():
                print(f"{self.computer.name} победил")
                break



game = Game()
game.start()