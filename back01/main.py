nome = input("Nome:")
cpf = input("CPF:")
email = input("Email:")

arquivo = open("Clientes.txt", "a")
arquivo.write(f"nome: {nome} \n")
arquivo.write(f"CPF: {cpf} \n")
arquivo.write(f"Email: {email} \n")
arquivo.close()





