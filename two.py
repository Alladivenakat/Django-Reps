




with open('abc.txt','r') as fr,open('write.txt','w') as fw:
    data=fr.readlines()
    fw.writelines(data)
    fw.write("Roll no,Name,Sub1,sub2,sub3,Total Marks"+"\n")

  
