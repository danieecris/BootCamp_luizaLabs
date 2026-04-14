pessoa = {
           "danielolicristian12@gmail.com":{ 
            "nome":"Daniel",
            "idade": 24, 
            "cidade": "São Paulo"
        },
            "emerson.cardoso@gmail.com": {      
            "nome":"Emerson",
            "idade": 24, 
            "cidade": "São Paulo"
            }
}


print(pessoa["emerson.cardoso@gmail.com"]["nome"])
print(pessoa.keys())