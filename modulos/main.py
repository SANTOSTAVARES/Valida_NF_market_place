from xml.dom import minidom
import xml.etree.ElementTree as ET
from data import not_checked_invoices
import sqlite3
from contextlib import closing

class third_party_invoice:
    """Get data from xml file to access information by this object.
    The parameter must be the file without .xml"""

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        invoice_file = open(f"../NFe/{self.file_name}")
        global invoice_content
        invoice_content = minidom.parse(invoice_file)

    #This fuction returns the invoice number.            
    def invoice_number(self):
        xml_tag = 'nNF'
        invoice_tag = invoice_content.getElementsByTagName(f'{xml_tag}')
        return invoice_tag[0].firstChild.data
    
    #This function returns the sales company CNPJ.
    def cnpj(self):
        xml_tag = 'CNPJ'
        invoice_tag = invoice_content.getElementsByTagName(f'{xml_tag}')
        return invoice_tag[0].firstChild.data

    #This function  returns the product name and prince in Python list.
    def products(self):
        products_list = []
        items_list = invoice_content.getElementsByTagName('det')
        product_name = invoice_content.getElementsByTagName('xProd')
        unitary_value = invoice_content.getElementsByTagName('vUnCom')    
        
        for x in items_list:
            products_list.append(['', ''])
        
        counter =  0
        for x in product_name:
            products_list[counter][0] = x.firstChild.data
            counter += 1
        
        counter =  0
        for x in unitary_value:
            products_list[counter][1] = x.firstChild.data[:-8]
            counter += 1

        return products_list

def search_invoice():
    """Search in database, if there is invoice to be analyzed.
    This function reads only the first invoice has to be analyzed. It was not implemented loop in this function.
    In the end of this function, It prints the analysis."""

    
    if len(not_checked_invoices()) > 0: #Check if there is invoice in line in database to be checked.
        first_in_line = not_checked_invoices()[0][0]
        analyze_invoice = third_party_invoice(f'{first_in_line}.xml')
        main_report = analyze_invoice.products()
                                    
        to_be_checked = []
        with sqlite3.connect("sold_products.db") as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("select * from sold_products where id_NFe=:chave", {"chave": first_in_line})
                while True:
                    query_result = cursor.fetchone()
                    if query_result is None:
                        break
                    iterable_result = [query_result[1], query_result[2]]
                    to_be_checked.append(iterable_result) 
        
        for i in main_report:
            i.append('')
        for x in main_report:
            for y in to_be_checked:
                if x[0] == y[0]:
                    x[2] = 'REGULAR'
        for i in main_report:
            if i[2] == '':
                i[2] = 'IRREGULAR'
        print(main_report)            
    else:
        print("There isn't any invoice to check yet.")
