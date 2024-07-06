from transaction import Sale, Return
class SalesReturnsTracking:
    def __init__(self):
        self.sales = []
        self.returns = []
        
# sale and create transaction id for sale sale record 
    def record_sale(self, transaction_id, product_id, quantity, sale_price, date):
        sale = Sale(transaction_id, product_id, quantity, sale_price, date)
        self.sales.append(sale)
        
# return product using transation id and a reson for" why return this product "
    def record_return(self, transaction_id, product_id, quantity, reason, date):
        return_record = Return(transaction_id, product_id, quantity, reason, date)
        self.returns.append(return_record)
