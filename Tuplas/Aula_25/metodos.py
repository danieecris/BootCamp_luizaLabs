contatos = {
    "daniel.cristian@gmail.com": {
        "nome": "Daniel", 
        "idade": 24, 
        "cidade": "São Paulo"
        }
    }

copias = contatos.copy()
copias["daniel.cristian@gmail.com"] = {"nome": "Dani"}

print(contatos["daniel.cristian@gmail.com"])
print(copias["daniel.cristian@gmail.com"])
print(contatos.get("telefone"))

contatos.update({"daniel.cristian@gmail.com":{"idade": 25}})
print(contatos)
