salario = float(input("Informe o salário: ")) #Float usado para números decimais

if salario <= 3000:
    print("Programador junior")
#elif em outras linguagens é o else e if, porem no Python
elif salario> 3000 and salario<= 6000:
    print("Pormador pleno")
elif salario> 6000 and salario<= 15000:
    print("Pormador pleno")
else:
    print("Gerente de projetos")