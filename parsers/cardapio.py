from xml.dom.minidom import parse

dom = parse("parsers/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName("prato")

for prato in pratos:
    id_prato = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f"{id_prato} - {nome}")

id_desejado = input("Digite o id do prato para saber mais: ")

prato_selecionado = None
for prato in pratos:
    if prato.getAttribute("id") == id_desejado:
        prato_selecionado = prato
        break

if prato_selecionado:
    nome = prato_selecionado.getElementsByTagName("nome")[0].firstChild.nodeValue
    descricao = prato_selecionado.getElementsByTagName("descricao")[0].firstChild.nodeValue
    ingredientes = prato_selecionado.getElementsByTagName("ingredientes")[0].getElementsByTagName("ingrediente")
    preco = prato_selecionado.getElementsByTagName("preco")[0].firstChild.nodeValue
    calorias = prato_selecionado.getElementsByTagName("calorias")[0].firstChild.nodeValue
    tempo = prato_selecionado.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue

    print(f"\nNome: {nome}")
    print(f"Descrição: {descricao}")
    print("Ingredientes:")
    for ingrediente in ingredientes:
        print(f"    {ingrediente.firstChild.nodeValue}")
    print(f"Preço: {preco}")
    print(f"Calorias: {calorias}kcal")
    print(f"Tempo de preparo: {tempo}.")
else:
    print("ID de prato não encontrado.")
