import xml.etree.ElementTree as ET
import json

def parse_imobiliaria(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    imoveis = []

    for imovel in root.findall('imovel'):
        data = {}

        data['descricao'] = imovel.findtext('descricao')

        proprietario = imovel.find('proprietario')
        prop_data = {
            'nome': proprietario.findtext('nome'),
            'telefones': [t.text for t in proprietario.findall('telefone')],
            'email': proprietario.findtext('email')
        }
        data['proprietario'] = prop_data

        # Endereço
        endereco = imovel.find('endereco')
        end_data = {
            'rua': endereco.findtext('rua'),
            'bairro': endereco.findtext('bairro'),
            'cidade': endereco.findtext('cidade'),
            'numero': endereco.findtext('numero')
        }
        data['endereco'] = end_data

        # Características
        caracteristicas = imovel.find('caracteristicas')
        caract_data = {
            'tamanho': caracteristicas.findtext('tamanho'),
            'numQuartos': int(caracteristicas.findtext('numQuartos')),
            'numBanheiros': int(caracteristicas.findtext('numBanheiros'))
        }
        data['caracteristicas'] = caract_data

        # Valor
        data['valor'] = int(imovel.findtext('valor'))

        imoveis.append(data)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(imoveis, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    parse_imobiliaria('imobiliaria.xml', 'imobiliaria.json')
