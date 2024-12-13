class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

inventory = []

def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    product = Product(product_id, name, description, price, quantity)
    inventory.append(product)
    print("Product added successfully!")

def update_quantity():
    product_id = input("Enter the product ID to update: ")
    for product in inventory:
        if product.product_id == product_id:
            new_quantity = int(input("Enter the new quantity: "))
            product.quantity = new_quantity
            print("Product quantity updated!")
            return
    print("Product not found!")

def display_products():
    if inventory:
        print("\nInventory:")
        for product in inventory:
            print(product)
    else:
        print("No products in inventory!")

def calculate_total_value():
    total_value = sum(product.price * product.quantity for product in inventory)
    print(f"\nTotal Inventory Value: {total_value}")

def inventory_menu():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product Quantity")
        print("3. Display Products")
        print("4. Calculate Total Inventory Value")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            update_quantity()
        elif choice == "3":
            display_products()
        elif choice == "4":
            calculate_total_value()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    inventory_menu()
