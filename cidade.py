import requests
from datetime import date, datetime

def cidade(cursor):
    try:
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Conectando a API....")
        response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes')
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Conexão realizada com sucesso!")
        response.raise_for_status()
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Inserção na base de dados iniciada...")
        for item in response.json():
            try:
                cursor.execute("INSERT INTO CIDADE VALUES (?, ?, ?)",
                               item["id"],
                               item["mesorregiao"]["UF"]["id"],
                               item["nome"])
            except Exception as error:
                print(error)
        cursor.commit()
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Inserção concluída com sucesso!\n")

    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)