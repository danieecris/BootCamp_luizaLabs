saldo = 1000
saque = 10000

status = "sucesso" if saque <= saldo else "falha"

print(f"O status do saque foi: {status}")