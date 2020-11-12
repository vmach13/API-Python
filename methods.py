from DB import *

def customerListCpfSearch(searchCPF):
  i=0
  while i<len(customerList):
    if customerList[i].cpf == searchCPF:
      return True
    else:
      i+=1
  return False

def cpfSearch(searchCPF):
  if customerListCpfSearch(searchCPF) == False:
    return False
    #return 'Cliente não encontrado'
  else:
    #print(customerList[index].name + ': ' + customerList[index].cpf)
    return True

def companyListSearch(searchCompanyCode):
  i=0
  while i<len(companyList):
    if companyList[i].companyCode == searchCompanyCode:
      return True
    else:
      i+=1
  return False

def companyCodeSearch(searchCompanyCode):
  if companyListSearch(searchCompanyCode) == False:
    return False
    #return 'Sede não encontrada'
  else:
    #print(companyList[index].companyName + ': ' + companyList[index].companyCode)
    return True

def productListSearch(searchProductCode):
  i=0
  while i<len(customerList):
    if productList[i].productCode == searchProductCode:
      return True
    else:
      i+=1
  return False

def productCodeSearch(searchProductCode):
  if productListSearch(searchProductCode) == False:
    return False
    #return 'Produto não encontrado'
  else:
    return True
    #print(productList[index].productName + ': ' + productList[index].productCode)


def requestHandler(requestCPF, requestProductCode, requestCompanyCode):
  if cpfSearch(requestCPF) == False:
    return "Cliente não encontrado"
  elif productCodeSearch(requestProductCode) == False:
    return "Produto não encontrado"
  elif companyCodeSearch(requestCompanyCode) == False:
    return "Sede não encontrada"
  else:
    return "This was triumph. I'm making a note here: HUGE SUCCESS."

