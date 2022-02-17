liste = [1,2,3,4]
for i in liste:
    print(i)

print("")


matris = [[1,2,3],
          [4,5,6],
          [7,8,9]]

generator  = (x for x in matris)
for i in generator:
    print(i)
    
'''
fonksiyon eğer return  olarak generator döndürecek ise
bunu return yerine yield yazarız
'''

def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i
    
print(10*"#")
generator = createGenerator()
print(generator)

for i in generator:
    print(i)











