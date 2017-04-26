fileList = []

for fname in fileList:    
    with open(fname,'r') as f:
        con = f.read()
    
    con = con.replace('/n','\r\n')
    
    with open(fname,'w') as f:
        f.write(con)
