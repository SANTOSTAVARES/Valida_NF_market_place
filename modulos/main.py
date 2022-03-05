from xml.dom import minidom
import xml.etree.ElementTree as ET
from data import not_checked_invoices
import time

class third_party_invoice:

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        invoice_file = open(self.file_name)
        global invoice_content
        invoice_content = minidom.parse(invoice_file)
                
    def invoice_number(self):
        xml_tag = 'nNF'
        invoice_tag = invoice_content.getElementsByTagName(f'{xml_tag}')
        return invoice_tag[0].firstChild.data
    
    def cnpj(self):
        xml_tag = 'CNPJ'
        invoice_tag = invoice_content.getElementsByTagName(f'{xml_tag}')
        return invoice_tag[0].firstChild.data

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

    while True:    
        counter = 0
        if len(not_checked_invoices()) > 0:
            for i in range(len(not_checked_invoices())):
                first_in_line = not_checked_invoices()[counter][0]
                analyze_invoice = third_party_invoice(f'{first_in_line}.xml')
                print(analyze_invoice.products())
                counter += 1
        else:
            print("There isn't any invoice to check.")
            time.sleep(20)
            print("It's going to be checked, if there is invoice in line.")
