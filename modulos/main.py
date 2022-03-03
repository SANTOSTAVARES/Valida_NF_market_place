from xml.dom import minidom
import xml.etree.ElementTree as ET

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
 
nerd = third_party_invoice('DFE35191142274696002561550010040410901297528776.xml')
print(nerd.invoice_number())
print(nerd.cnpj())
print(nerd.products())