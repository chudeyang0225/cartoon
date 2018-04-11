list = [1,2,3,4,5,6,7]
print (len(list))
with open ('log.txt','w') as w:
    w.write('346')
try:
    with open('log.txt') as r:
        lastlen = r.read()
        print(lastlen)
except:
    lastlen = 0
    print(lastlen)