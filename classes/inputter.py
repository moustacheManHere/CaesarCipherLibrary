class ThreeTriesInput:
    def __init__(self,inputString):
        self.inputString = inputString
        self.tries = 0
    
    def getIntInput(self,name,range):
        key = "lolzz"
        while not isinstance(key,int) and self.tries < 3:
            key = input(f"\nEnter {name}: ")
            try:
                key = int(key)
            except:
                print("Please enter a number.")
            self.tries += 1
        if self.tries == 3 and not isinstance(key,int):
            print(f"Sorry a valid {name} was not received.")
            return None
        if range != None and not key in range:
            print("Sorry invalid number entered... Please try again.")
            return None
        return key
        
    def getStrInput(self,strInp,accept):
        choice = "f"
        tries = 0 
        while choice not in accept and tries < 3:
            choice = input(strInp)
            tries += 1
        if tries == 3 and choice not in accept:
            print("\nSorry a valid choice was not received.")
        else:
            return choice