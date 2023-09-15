'''
    python 文件io
        新建test.txt 写入内容
        python文件IO分为3步：
            1.打开文件  --- open()
            2.对数据进行IO操作
                读
                    read(): 读取文件
                    seek()：指针归零
                    readline()：按行读取
                写

            3.关闭文件
'''

# fd = open("C:\\Users\\yanfa\\PycharmProjects\\pythonProject1\\day3\\test.txt", "rb")
# # buf = fd.readline()
# # fd.close()
#
# fd = open("C:\\Users\\yanfa\\PycharmProjects\\pythonProject1\\day3\\test1.txt", "wb")
# fd.writelines([b"bone\r\n", b"two\r\n", b"three\r\n"])
# fd.close()


# 实现将一个文件的内容拷贝到另一个文件中

# af = open("C:\\Users\\yanfa\\PycharmProjects\\pythonProject1\\day3\\testone.txt", "rb")
# df = open("C:\\Users\\yanfa\\PycharmProjects\\pythonProject1\\day3\\testtwo.txt", "wb")
#
# data = af.read()
# df.write(data)
#
# af.close()
# df.close()

# 实现文件（软件）拷贝
sf = open("C:\\Windows\\System32\\cmd.exe", "rb")
df = open("C:\\Users\\yanfa\\PycharmProjects\\pythonProject1\\day3\\dmc.exe", "wb")

while True:
    data = sf.read(4096)
    if data == b"":
        break
    df.write(data)

sf.close()
df.close()

