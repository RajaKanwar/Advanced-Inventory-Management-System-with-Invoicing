from transaction import Sale, Return
class SalesReturnsTracking:
    def __init__(self):
        self.sales = [] # List to store sales records
        self.returns = [] # List to store return records
        
# sale and create transaction id for sale sale record 
    def record_sale(self, transaction_id, product_id, quantity, sale_price, date):
        sale = Sale(transaction_id, product_id, quantity, sale_price, date) # This line for Create a Sale object
        self.sales.append(sale)  # Append the sale record to the sales list
        
# return product using transation id and a reson for" why return this product "
    def record_return(self, transaction_id, product_id, quantity, reason, date):
        return_record = Return(transaction_id, product_id, quantity, reason, date)# This line for Create a Return object
        self.returns.append(return_record) # Append the return record to the returns list
