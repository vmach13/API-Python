from methods import *

testCustomer = ['111.111.111-11','222.222.222-22','333.333.333-33','444.444.444-44','555.555.555-55','666.666.666-66','000.000.000-00']
testProduct = ['1001','1002','1003','1004','1005','1006','1000']
testCompany = ['0001','0002','0003','0004','0005','0006','0000']
testSize = len(testCustomer)-1



def TESTE_CUSTOMERS():
  print("Testando lista de customers")
  i=0
  while i<testSize:
    a = requestHandler(testCustomer[i],testProduct[0],testCompany[0])
    print("CPF: "+testCustomer[i]+"\ Produto: "+testProduct[0]+"\ Companhia: "+testCompany[0]+"\ Resultado: "+a)
    i+=1
  print("\n\n")

def TESTE_PRODUCTS():
  print("Testando lista de products")
  i=0
  while i<testSize:
    a = requestHandler(testCustomer[0],testProduct[i],testCompany[0])
    print("CPF: "+testCustomer[0]+"\ Produto: "+testProduct[i]+"\ Companhia: "+testCompany[0]+"\ Resultado: "+a)
    i+=1
  print("\n\n")

def TESTE_COMPANIES():
  print("Testando lista de companies")
  i=0
  while i<testSize:
    a = requestHandler(testCustomer[0],testProduct[0],testCompany[i])
    print("CPF: "+testCustomer[0]+"\ Produto: "+testProduct[0]+"\ Companhia: "+testCompany[i]+"\ Resultado: "+a)
    i+=1
  print("\n\n")

def TESTE_ERRORS():
  print("Testando casos não encontrados")
  a = requestHandler(testCustomer[-1],testProduct[0],testCompany[0])
  print("Erro CustomerNotFound: CPF= "+testCustomer[-1]+" Resultado: "+ a )
  
  a = requestHandler(testCustomer[0],testProduct[-1],testCompany[0])
  print("Erro ProductNotFound: productCode= "+testProduct[-1]+" Resultado: "+ a )
  
  a = requestHandler(testCustomer[0],testProduct[0],testCompany[-1])
  print("Erro CompanyrNotFound: companyCode= "+testCompany[-1]+" Resultado: "+ a )
  

def RUN_ALL_TESTS():
  TESTE_CUSTOMERS()
  TESTE_PRODUCTS()
  TESTE_COMPANIES()
  TESTE_ERRORS()
  print("\nTodos testes executados")


def STILL_ALIVE():
  firstverse=["This was a triumph.","I'm making a note here: HUGE SUCCESS.","It's hard to overstate my satisfaction.","Aperture Science","We do what we must","Because we can.","For the good of all of us.","Except the ones who are dead.","\n"]
  secondverse=["But there's no sense crying over every mistake","You just keep on trying","Till you run out of cake.","And the Science gets done.","And you make a neat gun.","For the people who are","Still alive.","\n"]
  thirdverse=["I'm not even angry.","I'm being so sincere right now.","Even though you broke my heart.","And killed me.","And tore me to pieces.","And threw every piece into a fire.","As they burned it hurt because","I was so happy for you!","Now these points of data","Make a beautiful line.","And we're out of beta.","We're releasing on time.","So I'm GLaD. I got burned.","Think of all the things we learned","For the people who are","Still alive.","\n"]
  fourthverse=["Go ahead and leave me.","I think I prefer to stay inside.","Maybe you'll find someone else","To help you.","Maybe Black Mesa...","THAT WAS A JOKE, HA HA, FAT CHANCE.","Anyway this cake is great","It's so delicious and moist","Look at me still talking when there's Science to do","When I look out there","It makes me GLaD I'm not you","I've experiments to run","There is research to be done","On the people who are","Still alive.","\n"]
  fifthverse=["And believe me I am still alive","I'm doing science and I'm still alive","I feel FANTASTIC and I'm still alive","While you're dying I'll be still alive","And when you're dead I will be still alive","Still alive","Still alive.","\n"]
  print("\n\n")
  for x in firstverse:
    print(x)
  for x in secondverse:
    print(x)
  for x in thirdverse:
    print(x)
  for x in fourthverse:
    print(x)
  for x in fifthverse:
    print(x)