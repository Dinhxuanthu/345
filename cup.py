class Cup:
    def __init__(self, size: int, quantity: int):
        
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters: int) -> None:
        
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters
        

    def status(self) -> int:
       
        return self.size - self.quantity

# Test Code
cup = Cup(100, 50)
print(cup.status())  
cup.fill(40)
cup.fill(20)
print(cup.status()) 
