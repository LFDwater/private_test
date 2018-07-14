import os
import sys
from PIL import Image
file_path = os.path.dirname((sys.argv[1])[:-6] + 'image/')
if not os.path.exists(file_path):
    os.makedirs(file_path)
lis = os.listdir(sys.argv[1])
for i in range(0,len(lis)):
    path = os.path.join(sys.argv[1],lis[i])
    #print(lis[i].split('_'))
    if os.path.isfile(path):
        os.chdir(file_path)
        im = Image.open(path)
        #n = 0
        while True:
            w = im.size[0]/2
            h = im.size[1]/2
            x = 0
            y = 0
            region = im.crop((x,y,x+w,y+h))
            region = region.resize((int(region.size[0])*2,int(region.size[1])*2))
            region.save(lis[i].split('_')[0] + '.jpg')
            print(path)
            x = w
            y = h
            region = im.crop((x,y,x+w,y+h))
            region = region.resize((int(region.size[0])*2,int(region.size[1])*2))
            region.save(lis[i].split('_')[1] + '.jpg')

            x = 0
            y =h
            region = im.crop((x,y,x+w,y+h))
            region = region.resize((int(region.size[0])*2,int(region.size[1])*2))
            region.save(lis[i].split('_')[2] + '.jpg')
     
            x = w
            y = 0
            region = im.crop((x,y,x+w,y+h))
            region = region.resize((int(region.size[0])*2,int(region.size[1])*2))
            region.save(lis[i].split('_')[3] + '.jpg')
          
            break
        #n = n + 4
print('finish')