import os
path = r"C:\Users\12485\Desktop\大创模型搭建\模型训练\data\F"
filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
count=0
for file in filelist:
    print(file)
for file in filelist:   #遍历所有文件
    Olddir=os.path.join(path,file)   #原来的文件路径
    if os.path.isdir(Olddir):   #如果是文件夹则跳过
        continue
    filename=os.path.splitext(file)[0]   #文件名
    filetype=os.path.splitext(file)[1]   #文件扩展名
    Newdir=os.path.join(path,str('F')+str('.')+str(count).zfill(4)+filetype)  #用字符串函数zfill 以0补全所需位数
    os.rename(Olddir,Newdir)#重命名
    count+=1