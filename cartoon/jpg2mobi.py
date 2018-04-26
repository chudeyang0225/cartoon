import os



mangapath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/cartoon/manga'
print(mangapath)
folders = os.listdir(mangapath)
print(folders)
os.chdir(mangapath)
print(os.getcwd())
for folder in folders:
    print(folder)
    os.system('kcc-c2e -p KV -u -s -r 1 %s/'%folder)