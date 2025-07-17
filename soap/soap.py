import requests
from xml.dom.minidom import parseString

URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

def send_soap_request(action, body):
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": action
    }

    response = requests.post(URL, data=body, headers=headers)
    return parseString(response.text)

def get_currency(country_code):
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_code}</sCountryISOCode>
        </CountryCurrency>
      </soap:Body>
    </soap:Envelope>"""

    dom = send_soap_request("http://www.oorsprong.org/websamples.countryinfo/CountryCurrency", body)
    currency = dom.getElementsByTagName("m:sName")[0].firstChild.nodeValue
    print(f"Moeda: {currency}")

def get_capital(country_code):
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_code}</sCountryISOCode>
        </CapitalCity>
      </soap:Body>
    </soap:Envelope>"""

    dom = send_soap_request("http://www.oorsprong.org/websamples.countryinfo/CapitalCity", body)
    capital = dom.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue
    print(f"Capital: {capital}")

def get_flag(country_code):
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryFlag xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_code}</sCountryISOCode>
        </CountryFlag>
      </soap:Body>
    </soap:Envelope>"""

    dom = send_soap_request("http://www.oorsprong.org/websamples.countryinfo/CountryFlag", body)
    flag_url = dom.getElementsByTagName("m:CountryFlagResult")[0].firstChild.nodeValue
    print(f"URL da Bandeira: {flag_url}")

def menu():
    print("===== Menu =====")
    print("1 - Ver moeda do país")
    print("2 - Ver capital do país")
    print("3 - Ver bandeira do país")
    opcao = input("Escolha uma opção (1-3): ")

    country_code = input("Digite o código ISO do país (ex: BR, US, FR...): ").upper()

    if opcao == "1":
        get_currency(country_code)
    elif opcao == "2":
        get_capital(country_code)
    elif opcao == "3":
        get_flag(country_code)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
