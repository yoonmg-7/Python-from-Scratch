class RestaurantTable:

    menus ={
        'pizza' : 3000,
        'apple juice': 2000,
        'drinking water': 1000,
        'string' : 1500,
        'sharp':2500
    }
    

    def __init__(self):
        self.total = 0
        self.orders = []

    def addorder(self,order):
        if order in self.menus:
            self.orders.append(order)
            self.total += self.menus[order]
        else:
            print(f"Sorry, '{order}' is not in the menu.")

    def printbill(self):
        print("\n--- Your Bill ---")
        for order in self.orders:
            print(f"{order} :  {self.menus[order]}")
        print(f"Total amount : {self.total}")

def startProgram():
     table = RestaurantTable()

     while True:
        order = input('order :')
        table.addorder(order)

        while True:  # keep asking until valid input
            another = input("Order again? (y/n): ")
            if another == 'y':
                break  # ask for another order
            elif another == 'n':
                table.printbill()
                return  # end program
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

startProgram();

         


