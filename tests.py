from methods import *

testCustomer = ['111.111.111-11','222.222.222-22','333.333.333-33','444.444.444-44','555.555.555-55','666.666.666-66','000.000.000-00']
testProduct = ['1001','1002','1003','1004','1005','1006','1000']
testCompany = ['90001','90002','90003','90004','90005','90006','90000']
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


#teste das requisicoes