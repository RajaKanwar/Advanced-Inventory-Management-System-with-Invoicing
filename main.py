from inventory_management import InventoryManagement
from sales_returns_tracking import SalesReturnsTracking
from invoice import Invoice

def main():
    inventory_mgmt = InventoryManagement()
    sales_returns = SalesReturnsTracking()

    while True:
        # work or create a command-line interface (CLI) from the line
        # Display menu options
        print("\n1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Remove Product")
        print("5. Record Sale")
        print("6. Record Return")
        print("7. Generate Invoice")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory_mgmt.view_all_products()
        elif choice == '2':
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            inventory_mgmt.add_product(product_id, name, category, price, quantity)
        elif choice == '3':
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name (leave blank to skip): ")
            category = input("Enter Product Category (leave blank to skip): ")
            price = input("Enter Product Price (leave blank to skip): ")
            quantity = input("Enter Product Quantity (leave blank to skip): ")
            inventory_mgmt.update_product(product_id, name, category, float(price) if price else None, int(quantity) if quantity else None)
        elif choice == '4':
            product_id = input("Enter Product ID: ")
            inventory_mgmt.remove_product(product_id)
        elif choice == '5':
            transaction_id = input("Enter Transaction ID: ")
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity Sold: "))
            sale_price = float(input("Enter Sale Price: "))
            date = input("Enter Date: ")
            sales_returns.record_sale(transaction_id, product_id, quantity, sale_price, date)
            inventory_mgmt.update_product(product_id, quantity=-quantity)
        elif choice == '6':
            transaction_id = input("Enter Transaction ID: ")
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity Returned: "))
            reason = input("Enter Reason for Return: ")
            date = input("Enter Date: ")
            sales_returns.record_return(transaction_id, product_id, quantity, reason, date)
            inventory_mgmt.update_product(product_id, quantity=quantity)
        elif choice == '7':
            transaction_id = input("Enter Sale Transaction ID: ")
        
            sale = next((s for s in sales_returns.sales if s.transaction_id == transaction_id), None)  # Go to IF condition if transaction ID matches product transaction ID
            if sale:
                invoice = Invoice(sale)
                invoice.generate_invoice() # calls generate_invoice in invoice.py file
            else:
                print("Sale not found!")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
