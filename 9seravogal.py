letra=input("Digite uma letra: \n")#pede para usuario digitar uma letra, e armazena na variavel letra
vogais=["a","e","i","o","u"]#declara as vogais
if letra in vogais:#se letra for um dos itens de vogal então
    print("A letra ",letra," É uma vogal")
else:
    print("A letra", letra, "É uma consoante")