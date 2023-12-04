"""
Módulo JSON

Com esse modulo conseguimos ler dados json de forma externa
salva arquivo json em txt
e formatar visualização do json
O json hoje é um dos principais arquivos para comunicação entre aplicações


"""

import json

# 1 -Strings para dicionários

person = '{"name": "Caio", "languages":["Python", "Javascript"]}'
person_dicti = json.loads(person)
print(person_dicti)

# 2 - Convertendo dicionário para json
person_json = json.dumps(person_dicti)#dumps - serializa um objeto python para uma string json
print(person_json)
print(type(person_json))
print(type(person_dicti))

# 3 - Formatando Json
print(json.dumps(person_dicti,indent=4, sort_keys=True ))
#O parâmetro indent=4 é usado para especificar a indentação de 4 espaços na string JSON, tornando-a mais legível para os humanos.
#O parâmetro sort_keys=True indica que as chaves do dicionário devem ser ordenadas em ordem alfabética na string JSON resultante.
#Essa operação é útil ao exibir ou armazenar dados JSON de forma organizada e legível

# 4 - Salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dicti, json_file)

# 5 - Lendo um arquivo json externo
with open("iris.json", "r") as f:
    data = json.load(f)
    print(data)
