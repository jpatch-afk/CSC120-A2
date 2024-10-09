class Computer:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    item_id:int 

    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int, item_id:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.item_id = item_id
    

    def update_price(self, new_price:int, item_id:int):
        print("Changing price...")
        self.price = new_price 
        print("Price changed successfully!")


    def update_OS(self, operating_system:str, new_OS:int, item_id:int):
        print("Changing OS...")
        self.operating_system = new_OS
        print("OS changed successfully!")


def main():
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500, 1)

if __name__ == "__main__": 
    main()