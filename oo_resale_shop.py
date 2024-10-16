class ResaleShop:
 
    inventory: list

    def __init__(self, inventory:list):
        self.inventory = ["Computer #1"] 


    def sell (self, c):
        if (c in self.inventory): 
            print("Trying to remove", c, "from inventory...")
            self.inventory.remove(c)
            print("Success!")
        else: 
            print(f"{c} is not in the inventory!")


    def refurbish(self, c, new_os: str):
        print("Trying to refurbish item...")

        
    def buy(self, c):
        print("Trying to add", c, "to inventory...")
        self.inventory.append(c)
        print("Success!")

    def printinventory(inventory:list):
        print(inventory)


def main():
    myShop: ResaleShop = ResaleShop()
    print("There are", len(myShop.inventory), "items in stock.")
    c = "MY NEW COMPUTER"
    myShop.buy(c)
    print("There are now", len(myShop.inventory), "items in stock.")
    

if __name__ == "__main__":
    main()