curso = "python_curse"
curso2 = "     python      "

print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso2.strip())
print(curso2.lstrip())
print(curso2.rstrip())

print(curso.center(40, "#"))
print(".".join(curso))


for letra in curso:
    print(letra, end="!")