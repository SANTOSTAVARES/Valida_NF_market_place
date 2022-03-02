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

nerd = third_party_invoice('nota_nerdstore.xml')
print(nerd.invoice_number())
