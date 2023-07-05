# 计算哈希函数
import hashlib

# hellokitty 123456

def main():
    digester = hashlib.md5()
    # md5 / sha1 / sha256
    with open('新建文本文档.txt','rb') as file_stream:
        file_iter = iter(lambda: file_stream.read(1024),b'')
        for data in file_iter:
            digester.update(data)
    print(digester.hexdigest())


if __name__ == '__main__':
    main()