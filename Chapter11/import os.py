import os
def read_file(fileIn):
    line=None
if os.path.isfile(fileIn):
    data=open(fileIn,"r")
while line !="":
    line=data.readline()
print(line)