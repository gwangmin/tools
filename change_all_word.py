import os

start_path = '.'
word = {'before':'after'}

for path,dirs,files in os.walk(start_path):
    for fname in files:
        con = None
        with open(fname,'r') as f:
            con = f.read()
        for before in word.keys():
            con = con.replace(before,word[before])
        with open(fname,'w') as f:
            f.write(con)
