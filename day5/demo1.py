'''
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76

/admdfs/g30/M02/72/3D/CjIFU2UBbzaAHTr2AABMZSFj5ns385.jpg
//gw.alicdn.com/bao/uploaded/i3/2429532607/O1CN01PSWxB51V83OxpqjxZ_!!2429532607.jpg_300x300q90.jpg
http://img5.pcpop.com/ArticleImages/730x547/4/4069/004069584.jpg
'''


import urllib.request
import re


class GetHtml(object):
    def __init__(self, URL, HEAD):  #构造函数，初始化了url 和 head
        self.url = URL
        self.head = HEAD

    def get_index(self,):           #获取网页所有html信息
        self.request = urllib.request.Request(self.url)
        self.request.add_header("user-agent", self.head)
        self.response = urllib.request.urlopen(self.request)
        return self.response.read()

    def get_list(self):             #过滤出所有图片
        self.strimglist = []
        self.imglist = re.findall(b"/\w(33)png", self.get_index())
        print(self.imglist)
        for i in self.imglist:
            self.strimglist.append(self.url+str(i,encoding="utf8"))
            #print(self.strimglist)
            return self.strimglist

    def get_images(self):           #保存图片
        num = 0
        for self.url in self.get_list():
            num += 1
            with open(str(num)+".jpg", "wb") as f:
                f.write(self.get_index())

html = GetHtml("https://image.so.com/", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76")
print(html.get_index())
html.get_list()
try:
    html.get_images()
except TypeError:
    print("not find image")