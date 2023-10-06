
def linearSearchProduct(productList,targetProduct):
  indicies= []
  for index,product in 
enumerate(productList):
  if product == targetProduct:
    indicies.append(index)
  return indicies
products=["shoes","boot","loafer","shoes",]
taget="shoes"
result=linearsearchProduct(products,target)
print(result)