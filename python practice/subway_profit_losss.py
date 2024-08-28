class Subway:
	def get_sales_input(self, prompt):
	    while True:
	        try:
	            value = float(input(prompt))
	            if value > 0:
	                return value
	            else:
	                print("Please enter a positive number.")
	        except ValueError:
	            print("Invalid input. Please enter a number.")

	def calculate_profit_or_loss(self, gross_sale, net_sale, utility, rent, salary):
	    inventory_cost = 0.28 * net_sale  # Inventory is 28% of net sale
	    royalty = 0.125 * gross_sale  # Royalty is 12.5% of gross sale
	    profi_losss = net_sale - (inventory_cost + royalty + rent + salary + utility)
	    return profi_losss, inventory_cost, royalty

	def main(self):
	    gross_sale = self.get_sales_input("Enter the Gross Sale:")
	    net_sale = self.get_sales_input("Enter the Net Sale: ")
	    utility = self.get_sales_input("Enter utility(its 3000):")
	    rent = self.get_sales_input("Enter rent(its around 3600):")
	    salary = self.get_sales_input("Enter salary(usally its 6000):")

	    
	    # utility = 3000
	    # rent = 3600
	    # salary = 6000
	    
	    profi_losss, inventory_cost, royalty = self.calculate_profit_or_loss(gross_sale, net_sale, utility, rent, salary)
	    
	    print(f"\nInventory cost (28% of net sale): ${inventory_cost:.2f}")
	    print(f"Royalty (12.5% of gross sale): ${royalty:.2f}")
	    print(f"utility : ${utility:.2f}")
	    print(f"rent : ${rent:.2f}")
	    print(f"salary(it could be count base on net sale of 22%) : ${salary:.2f}")
	    print(f"Profit or Loss: ${profi_losss:.2f}")

if __name__ == "__main__":
    sub = Subway()
    sub.main()
