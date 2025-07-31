import requests
from getpass import getpass
from rich.console import Console
from rich.table import Table

api_url = "https://suap.ifrn.edu.br/api/"
user = input("Usuário SUAP: ")
password = getpass("Senha: ")

data = {"username": user, "password": password}
response = requests.post(api_url + "v2/autenticacao/token/", json=data)

if response.status_code != 200:
    print("❌ Erro ao autenticar.")
    print("Detalhes:", response.text)
    exit()

token = response.json()["access"]
headers = {"Authorization": f"Bearer {token}"}

ano = input("Digite o ano (ex: 2024): ")

response = requests.get(f"https://suap.ifrn.edu.br/api/edu/meu-boletim/{ano}/1/", headers=headers)

if response.status_code != 200:
    print("❌ Erro ao buscar boletim.")
    print("Detalhes:", response.text)
    exit()

boletim = response.json()

console = Console()
table = Table(title=f"Boletim {ano} - 1º período")

table.add_column("Disciplina", style="bold green")
table.add_column("1ª Unidade", style="blue")
table.add_column("2ª Unidade", style="blue")
table.add_column("3ª Unidade", style="blue")
table.add_column("4ª Unidade", style="blue")
table.add_column("Média Final", style="green")
table.add_column("Situação", style="red")
table.add_column("Faltas", style="white")

for materia in boletim:
    table.add_row(
        materia.get("disciplina", "—"),
        str(materia.get("nota_etapa_1", {}).get("nota", "—")),
        str(materia.get("nota_etapa_2", {}).get("nota", "—")),
        str(materia.get("nota_etapa_3", {}).get("nota", "—")),
        str(materia.get("nota_etapa_4", {}).get("nota", "—")),
        str(materia.get("media_final_disciplina", "—")),
        materia.get("situacao", "—"),
        str(materia.get("numero_faltas", "—")),
    )

console.print(table)
