# invoice.py
from fpdf import FPDF

class Invoice:
    def __init__(self, sale):
        self.sale = sale

    def generate_invoice(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Invoice for Sale ID: {self.sale.transaction_id}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Product ID: {self.sale.product_id}", ln=True)
        pdf.cell(200, 10, txt=f"Quantity Sold: {self.sale.quantity}", ln=True)
        pdf.cell(200, 10, txt=f"Sale Price: {self.sale.sale_price}", ln=True)
        pdf.cell(200, 10, txt=f"Date: {self.sale.date}", ln=True)
        pdf.output(f"Invoice_{self.sale.transaction_id}.pdf")
