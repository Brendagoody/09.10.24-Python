
saudacao = input("Olá, seja bem vind-!")
nome = input("Como você se chama ?")
idade = int(input("Muito prazer " + nome + ", eu me chamo Brenda! E me diga, quantos anos você tem ?"))

if idade <=17: 
    print("É muito legal ter você aqui conosco," + nome + ",mas você precisará comparecer com um responsável por ter " + idade "anos, combinado ?") 
else: 
    resposta = input("Legal, e como você ficou sabendo da nossa feira cultural ?")

    resposta = input("Legal ? (sim ou não)")



if resposta.lower() == "sim":
 print("Legal !")

else: 
 print("Ah, tudo bem. Nos vemos na próxima !")
