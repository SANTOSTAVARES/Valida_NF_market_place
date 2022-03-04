from xml.dom import minidom
import xml.etree.ElementTree as ET
from data import not_checked_invoices

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
            products_list[counter][1] = x.firstChild.data
            counter += 1

        return products_list


#print(nerd.invoice_number())
#print(nerd.cnpj())
#print(nerd.products())

counter = 0
first_in_line = not_checked_invoices()[counter][0]
print(first_in_line)
analyze_invoice = third_party_invoice(f'{first_in_line}.xml')
print(analyze_invoice.products())