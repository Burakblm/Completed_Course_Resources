import os

print(os.name)
currentDir = os.getcwd() # hangi klasörün içinde olduğumuzu verir
print(currentDir)

# new folder(yeni dosya)
folder_name = "new_folder"
os.mkdir(folder_name)

# klasör ismini değiştirme
new_folder_name = "new_folder_2"
os.rename(folder_name,new_folder_name)

# dosya içinde gimek
os.chdir(currentDir+"\\"+new_folder_name)# dosyaların içine girmek için kullanılır
print(os.getcwd())

os.chdir(currentDir)# dosyaların içine girmek için kullanılır
print(os.getcwd())

# dizinin içindeki dosyaları listelemek
files = os.listdir()
print(files)

# dizinde py uzantılı dosyaları listelemek
for i in files:
    if i.endswith(".py"):
        print(i)
        

# klasörü silmek
os.rmdir("new_folder_2")

for i in os.walk(currentDir):
    print(i)

# dizinde dosyanın var olup olmadığını kontrol etmek
# var ise True yok ise False döndürecek
os.path.exists("denemeler.py")
