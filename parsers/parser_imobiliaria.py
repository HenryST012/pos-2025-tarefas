import json

def carregar_imoveis(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def exibir_menu(imoveis):
    print("\n==== Lista de Imóveis Disponíveis ====")
    for i, imovel in enumerate(imoveis):
        print(f"[{i}] {imovel['descricao']}")
    print("[s] Sair")

def exibir_detalhes(imovel):
    print("\n=== Detalhes do Imóvel ===")
    print(f"Descrição: {imovel['descricao']}")
    print(f"Valor: R$ {imovel['valor']:,.2f}")

    print("\n-- Proprietário --")
    print(f"Nome: {imovel['proprietario']['nome']}")
    if imovel['proprietario'].get('telefones'):
        print("Telefones:", ", ".join(imovel['proprietario']['telefones']))
    if imovel['proprietario'].get('email'):
        print("Email:", imovel['proprietario']['email'])

    print("\n-- Endereço --")
    endereco = imovel['endereco']
    print(f"{endereco.get('rua', '')}, Nº {endereco.get('numero', 's/n')}")
    print(f"Bairro: {endereco.get('bairro', '')}")
    print(f"Cidade: {endereco.get('cidade', '')}")

    print("\n-- Características --")
    caract = imovel['caracteristicas']
    print(f"Tamanho: {caract['tamanho']}")
    print(f"Quartos: {caract['numQuartos']}")
    print(f"Banheiros: {caract['numBanheiros']}")
    print("=" * 40)

def menu_interativo():
    imoveis = carregar_imoveis('imobiliaria.json')

    while True:
        exibir_menu(imoveis)
        escolha = input("\nDigite o ID do imóvel para ver detalhes (ou 's' para sair): ")

        if escolha.lower() == 's':
            print("Encerrando programa. Até logo!")
            break
        elif escolha.isdigit():
            id_imovel = int(escolha)
            if 0 <= id_imovel < len(imoveis):
                exibir_detalhes(imoveis[id_imovel])
            else:
                print("ID inválido. Tente novamente.")
        else:
            print("Entrada inválida. Digite um número ou 's'.")

if __name__ == '__main__':
    menu_interativo()
