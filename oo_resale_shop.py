class ResaleShop:
 
    inventory:list

    def __init__(self):
        self.inventory = []
         

    #Sells a computer, or removes it from the store inventory 
    def sell (self, c, inventory:list):
        if (c in inventory): 
            print("Trying to remove", c, "from inventory...")
            inventory.remove(c)
            print("Success!")
        else: 
            print(f"{c} is not in the inventory!")

    #Refurbishes the computer based on the year it's made 
    def refurbish (self, c, new_os: str, inventory):
        if (c in inventory):
            print("Trying to refurbish item...") 
        else:
            print(f"{c} is not in the inventory!")


    #Buys a computer, or adds a computer to the inventory 
    def buy(self, c):
        print("Trying to add", c, "to inventory...")
        self.inventory.append(c)
        print("Success!")

    #Prints the inventory 
    def printinventory(inventory:list):
        print(inventory)

#Defines a shop that using the ResaleShop class and simulates transactions 
def main():
    myShop: ResaleShop = ResaleShop()
    print("There are ", len(myShop.inventory), "item(s) in stock.")
    c = "MY COMPUTER"
    myShop.buy(c)
    print("There are ", len(myShop.inventory), "item(s) in stock.")
    

if __name__ == "__main__":
    main()