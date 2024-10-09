class ResaleShop:
 
    inventory: list

    def __init__(self, inventory:list):
        self.inventory = inventory
        inventory = [""] 


    def sell (self, c, inventory:list):
        if (c in inventory): 
            print("Trying to remove", c, "from inventory...")
            inventory.remove(c)
            print("Success!")
        else: 
            print(f"{c} is not in the inventory!")


    def refurbish (self, c, new_os: str, inventory):
        if (c in inventory):
            print("Trying to refurbish item...")
            
        else:
            print(f"{c} is not in the inventory!")


        

    #GOAL: add c to self.inventory
    def buy(self, c):
        print("Trying to add", c, "to inventory...")
        self.inventory.append(c)
        print("Success!")

    def printinventory(inventory:list):
        print(inventory)


def main():
    myShop: ResaleShop = ResaleShop()
    print("There are ", len(myShop.inventory), "item(s) in stock.")
    c = "MY COMPUTER"
    myShop.buy(c)
    print("There are ", len(myShop.inventory), "item(s) in stock.")
    

if __name__ == "__main__":
    main()