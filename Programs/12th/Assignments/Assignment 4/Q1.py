fh1=open('Our Generation.txt','r')
fh2=open('reversePoem.txt','w+')
lines=fh1.readlines()
lines.reverse()
fh2.writelines(lines)
fh1.close()
fh2.seek(0)
print(fh2.read())
fh2.close()
