
import PIL.Image as Image
import os
import sys


# a = os.listdir('allmaps')
# print(len(a))


def pastepic(year):
    mw = 450  # 图片大小+图片间隔
    ms = 8
    msize = mw * ms

    toImage = Image.new('RGBA', (8*450, 4*450))

    for x in range(0, 4):  # 先试一下 拼一个5*5 的图片
        for y in range(0, 8):

            # 之前保存的图片是顺序命名的，x_1.jpg, x_2.jpg ...
            fname = "allmaps/"+year+"/"+str(y)+str(x)+".png"
            fromImage = Image.open(fname)
            # #fromImage =fromImage.resize((mw, mw), Image.ANTIALIAS)   # 先拼的图片不多，不用缩小

            toImage.paste(fromImage, ((y) * mw, (x) * mw))

    toImage.save("allOKmaps/"+year+"map.png")


if __name__ == '__main__':
    allyears = os.listdir('allmaps')
    for year in allyears:
        pastepic(str(year))
        print(year)
