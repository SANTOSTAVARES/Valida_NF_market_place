from xml.dom import minidom
import xml.etree.ElementTree as ET

class NFe_parceiro:

    def __init__(self, nome_arquivo) -> None:
        self.nome_arquivo = nome_arquivo
    
    arquivo = open(f'{self.nome_arquivo}')
    conteudo_NF = minidom.parse(arquivo)

    def cnpj(self):
        return conteudo_NF.getElementsByTagName('CNPJ')

nerd = NFe_parceiro('nota_nerdstore.xml')
