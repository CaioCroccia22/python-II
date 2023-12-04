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
