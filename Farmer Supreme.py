from Farm import Farm





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
            print("Shop: 100 gold \nWorker: 20 gold \nSlave: 10 gold\nLand: 10 gold ")
            print("You and workers makes 1 gold every 2 seconds.")
            print("Each slave makes 1 gold every 2 seconds.")
            print("Selling a slave makes 1 gold.")
            print("Each shop makes 2 times the amount of owned shops per 2 seconds.")
            print("Each plot of land increases the amount of food that can be harvested by 2")
        elif choice == "11":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
            
         

if __name__ == "__main__":
    main()
