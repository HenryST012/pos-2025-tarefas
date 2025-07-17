import zeep

# URL do WSDL
wsdl_url= "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# Criação do cliente Zeep
client = zeep.Client(wsdl=wsdl_url)

def converter_numero():
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = client.service.NumberToWords(ubiNum=numero)
        print(f"{numero} por extenso em inglês: {resultado}")
    except ValueError:
        print("Você precisa digitar um número inteiro válido.")

if __name__ == "__main__":
    converter_numero()
