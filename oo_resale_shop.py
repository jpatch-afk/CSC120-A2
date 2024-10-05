class ResaleShop:

    item_ID: int 
    inventory: list
    new_os: str 


    def __init__(self, item_ID: int, inventory:list, new_os:str):
        self.item_ID = item_ID 
        self.inventory = [] 
        self.new_os = new_os

    def sell (self, c):
        print("Trying to remove", c, "from inventory...")
        self.inventory.remove(c)
        print("Success!")


    def refurbish (self, c, new_os: str):
        print("Trying to refurbish item",c)
        
        

    #GOAL: add c to self.inventory
    def buy(self, c):
        print("Trying to add", c, "to inventory...")
        self.inventory.append(c)
        print("Success!")

    def printinventory(inventory:list):
        print(inventory)


def main():
    myShop: ResaleShop = ResaleShop()
    print("There are", len(myShop.inventory), "items in stock.")
    c = "MY COMPUTER"
    myShop.buy(c)
    print("There are now", len(myShop.inventory), "items in stock.")
    

if __name__ == "__main__":
    main()