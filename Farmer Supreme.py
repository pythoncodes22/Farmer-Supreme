import random
import time
import threading
class Farm:
    def __init__(self):
        self.gold = 0
        self.food = 100
        self.land = 10
        self.population = 1
        self.slave = 0
        self.shop = 0      
        self.gold_generation_thread = threading.Thread(target=self.generate_gold)
        self.gold_generation_thread.daemon = True
        self.gold_generation_thread.start()
        self.lose_food_thread = threading.Thread(target=self.lose_food)
        self.lose_food_thread.daemon = True
        self.lose_food_thread.start()
            
    def generate_gold(self):
        while True:
            # Wait for 2 seconds
            time.sleep(2)

            # Calculate the total gold contribution from workers
            gold_contribution = self.population
           

            # Add the gold contribution to the total gold
            self.gold += gold_contribution
            self.gold += self.shop * 2 
   
    def lose_food(self):
        while True:
            time.sleep(60)
            
            self.food -= self.population * 2
    
    
    def show_status(self):
        print("=== Farm Status ===")
        print(f"Gold: {self.gold}")
        print(f"Food: {self.food}")
        print(f"Land: {self.land}")
        print(f"Shops: {self.shop}")
        print(f"Slaves: {self.slave}")
        print(f"Population: {self.population}")
        print("===================")

    def harvest(self):
        self.food += self.land * 2
        print(f"You harvested {self.land * 2} food.")
        time.sleep(1)

    def sell_food(self):
        if self.food >= 10:
            sell_amount = min(self.food, 10)
            self.gold += sell_amount
            self.food -= sell_amount
            print(f"You sold {sell_amount} food for {sell_amount} gold.")
        else:
            print("Not enough food to sell.")
        time.sleep(1)

    def buy_land(self):
        land_cost = 10
        if self.gold >= land_cost:
            self.land += 1
            self.gold -= land_cost
            print("You bought 1 plot of land.")
        else:
            print("Not enough gold to buy land.")
        time.sleep(1)
    
    def buy_shop(self):
        shop_cost = 100
        if self.gold >= shop_cost:
            self.shop += 1
            self.gold -= shop_cost
            print("You bought 1 shop.")
        else:
            print("Not enough gold to buy a shop.")
        time.sleep(1)
        
    def hire_worker(self):
        worker_cost = 20
        if self.gold >= worker_cost:
            self.population += 1
            self.gold -= worker_cost
            print("You hired 1 worker.")
        else:
            print("Not enough gold to hire worker.")
        time.sleep(1)
        
        
    def buy_slave(self):
        slave_cost = 10
        if self.gold >= slave_cost:
            self.population += 1
            self.slave += 1
            self.gold -= slave_cost
            print("You bought 1 slave.")
        else:
            print("Not enough gold to buy a slave.")
        time.sleep(1)
    price = ("10","11","12")       
    def sell_slave(self):
        if self.slave >= 1:
            sell_amount = min(self.slave, 1)
            self.gold += sell_amount
            self.population -= 1
            self.slave -= sell_amount
            print(f"You sold {sell_amount} slave for {sell_amount} gold.")
        else:
            print("No slaves to sell.")
        time.sleep(1)

    def next_year(self):
        self.food -= self.population * 20
        if self.food < 0:
            self.food = 0
        self.gold += self.population * 5
        self.population += int(self.food / 50)
        print("One year has passed.")
        time.sleep(1)

def main():
    farm = Farm()
    while True:
        print("\n=== Farmer Supreme ===")
        print("1. Show Farm Status")
        print("2. Harvest Food")
        print("3. Sell Food")
        print("4. Buy Land")
        print("5. Hire Worker")
        print("6. Next Year")
        print("7. Buy Slave")
        print("8. Sell Slave")
        print("9. Buy Shop")
        print("10. Help")
        print("11. Quit")
        print("version: 1.2")

        choice = input("Enter your choice: ")

        if choice == "1":
            farm.show_status()
        elif choice == "2":
            farm.harvest()
        elif choice == "3":
            farm.sell_food()
        elif choice == "4":
            farm.buy_land()
        elif choice == "5":
            farm.hire_worker()
        elif choice == "6":
            farm.next_year()
        elif choice == "7":
            farm.buy_slave()
        elif choice == "8":
            farm.sell_slave()
        elif choice == "9":
            farm.buy_shop()
        elif choice == "10":
            print("Shop: $100 \nWorker: $20 \nSlave: $10\n")
            print("You and workers makes 1 gold every 2 seconds.")
            print("Each slave makes 1 gold every 2 seconds.")
            print("Selling a slave makes 1 gold.")
            print("Each shop makes 2 times the amount of owned shops per 2 seconds.")
        elif choice == "11":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
