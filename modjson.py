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
