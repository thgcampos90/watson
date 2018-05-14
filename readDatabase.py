import pandas

#print(pandas.read_excel('settings.xls'))

D = pandas.read_excel('settings.xls')

workspace = None
password  = None 
path   = None

#for i in range(0,2):
#    print(D["workspace"][i])
#    print(D["password"][i])
#    print(D["path"][i])

#print (len(D))

for i in range(0,len(D)): 
    workspace = D['workspace'][i]
    password  = D['password'][i]
    path = D['path'][i] + '/' + workspace + '.json' 
    F = open(path,'w')
    F.write(workspace)
    F.close()    

