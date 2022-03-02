#C:\Users\gst_9\Documents\estudando_git\xml
    root = ET.parse("nota_nerdstore.xml").getroot()
    NFe = {'ns': "http://www.portalfiscal.inf.br/nfe" }

    numero_NF = root.find('ns:NFe/ns:infNFe/ns:ide/ns:nNF', NFe).text
    chave_NF = root.find('ns:NFe/ns:infNFe', NFe)
    print(numero_NF)

    arquivo = open("nota_nerdstore.xml")
    conteudo_NF = minidom.parse(arquivo)
    numero_NF2 = conteudo_NF.getElementsByTagName('nNF')
    print(numero_NF2[0].firstChild.data)
    print(chave_NF.attrib['Id'])
    chave_NF2 = root.find('ns:NFe/ns:infNFe', NFe).attrib
    print(chave_NF2)

    itens = conteudo_NF.getElementsByTagName('det')
    nome_produto = conteudo_NF.getElementsByTagName('xProd')

    for i in itens:
        print(i.attributes['nItem'].value)

    for i in nome_produto:
        print(i.firstChild.data)

from xml.dom import minidom
import xml.etree.ElementTree as ET

class third_party_invoice:

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        invoice_file = open(self.file_name)
        global invoice_content
        global invoice_tag
        invoice_tag = invoice_content.getElementsByTagName(f'{xml_tag}')
        invoice_content = minidom.parse(invoice_file)
        
    def invoice_number(self):
        xml_tag = 'nNF'
        invoice_tag = invoice_content.getElementsByTagName(f'{xml_tag}')
        return invoice_tag[0].firstChild.data
    
    def cnpj(self):
        xml_tag = 'cnpj'
        invoice_tag = invoice_content.getElementsByTagName(f'{xml_tag}')
        return invoice_tag[0].firstChild.data
#Testeeeeeeeeeeeeee
#Testeeeeeeeeeeeeee
nerd = third_party_invoice('nota_nerdstore.xml')
print(nerd.invoice_number())