#
# Crawler Edited by Pycharm.
# Time : 2022/11/21
# Author : YU.J.P
#

"""
    版本: V1.2
    基本功能:
    根据提取的链接，采用广度优先方式抓取至少1000个网页，并提取上述指定的信息；
"""
import codecs
import json
import urllib.request
import BitVector as BitVector
from bs4 import BeautifulSoup
import re
from Plug_in.Colors import Color

########################################################################################################################


class SimpleHash:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    # 生成hash值
    def hash(self, value):
        result = 0
        for i in range(len(value)):
            # 加权求和
            result += self.seed * result + ord(value[i])
        # 位运算保证最后的值在0到self.cap之间
        return (self.cap - 1) & result

########################################################################################################################


# 布隆过滤器
class BloomFilter:
    def __init__(self, BIT_SIZE=1 << 25):
        self.BIT_SIZE = 1 << 25
        # 哈希种子 素数
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.bitset = BitVector.BitVector(size=self.BIT_SIZE)
        self.hashFunc = []
        # 生成对应大小的哈希表
        for i in range(len(self.seeds)):
            self.hashFunc.append(SimpleHash(self.BIT_SIZE, self.seeds[i]))

    # 将元素值加入过滤器中
    def insert(self, value):
        # 计算每一个哈希表
        for f in self.hashFunc:
            loc = f.hash(value)
            # print(loc)
            self.bitset[loc] = 1

    # 是否已经在过滤器中
    def is_contain(self, value):
        if value is None:
            return False
        result = True
        # 判断每个哈希值是否都已经出现
        for f in self.hashFunc:
            loc = f.hash(value)
            result &= self.bitset[loc]
        return result

########################################################################################################################


# 正则表达式处理网页
class Remove:

    @classmethod
    def extract_title(cls, content):
        """
        提取网页 标题
        :param content: html文本
        :return: 返回html文本的标题
        """
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find('title')
        return title.text

    @classmethod
    def remove_empty_line(cls, content):
        """
        去除空行
        :param content: 需要处理的文本
        :return: 处理空行、空格好的文本
        """
        r = re.compile(r'''^\s+$''', re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r'''\n+''', re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r'''\t+''', re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r'''\r+''', re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r''' +''', re.M | re.S)
        content = r.sub('', content)
        return content

    @classmethod
    def remove_js_css(cls, content):
        """
        去除script,style,meta，注释等脚本
        :param content: 需要处理的文本
        :return: 移除script,style,meta，注释等脚本脚本后的文本
        """
        r = re.compile(r'''<script.*?</script>''', re.I | re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r'''<style.*?</style>''', re.I | re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r'''<!--.*?-->''', re.I | re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r'''<meta.*?>''', re.I | re.M | re.S)
        content = r.sub('', content)
        r = re.compile(r'''<ins.*?</ins>''', re.I | re.M | re.S)
        content = r.sub('', content)
        return content

    @classmethod
    def remove_any_tag(cls, content):
        """
        移除js,css脚本
        :param content: 需要处理的文本
        :return: 移除js,css脚本后的文本
        """
        content = re.sub(r'''<[^>]+>''', '', content)
        return content.strip()

########################################################################################################################


# 利用正则表达式，将网页中的标题、正文、超链接、图片等元素分别提取出来，并能存放到指定的文件中；图片单独存储
class BFSCrawler:

    def __init__(self, htmlPath, childPath, imagePath):
        self.htmlPath = htmlPath  # 内容地址
        self.childPath = childPath  # 子链接地址
        self.imagePath = imagePath  # 图片地址
        self.urlCount = 0  # 网址计数器
        self.imgCount = 0  # 图片计数器

    def BFS_getImages(self, content):
        """
        爬取图片
        :param content: 爬取网页内容
        :param path: 本地图片存储位置
        :return: None
        """
        Img = re.compile(r'Src="(.+?\.jpg)"')  # 正则表达式匹配图片
        imageList = re.findall(Img, content)  # 结合re正则表达式和BeautifulSoup, 仅返回超链接
        if imageList is not None:
            newList = []
            for index in imageList:
                # 应该有更好的网链处理
                if index != '' and 'https' in index:
                    newList.append(index)
            # print(newList)  # 奇怪的方法解决了BUG

            print(Color.red + "# Begin Download Image DATA...")
            for imageUrl in newList:
                # 打开网址，下载图片保存到本地
                urllib.request.urlretrieve(imageUrl, '{}{}.jpg'.format(self.imagePath, self.imgCount))
                self.imgCount += 1  # 计数器
            print(Color.green + "# Download Image DATA Successfully...")
        else:
            print(Color.red + "# ERROR ! No Useful URL...")

    def BFS_extract_a_label(self, content):
        """
        提取网页子网页,并写入文件
        :param content: 需要处理的文本
        :return: None
        """
        soup = BeautifulSoup(content, 'html.parser')
        childLink = soup.find_all('a')
        # return alink

        # 写入文件 按编号写入
        childList = []
        file_ob = open(self.childPath + 'childUrl' + str(self.urlCount) + '.txt', 'w', encoding='utf-8')
        for link in childLink:
            child = link.get('href')
            key = link.string
            if key is not None and child is not None:
                file_ob.write(key + ':' + child + '\n')
                childList.append(child)  # 子网址列表
        file_ob.close()
        print(Color.yellow + "# childLink " + str(self.urlCount) + " Writing Successfully...")
        return childList  # 返回子网址

    def BFS_cuteCrawler(self, url):
        """
        爬虫程序 - 将网页中的标题、正文、超链接、图片等元素分别提取出来，并能存放到指定的文件中；图片单独存储。
        :param url: 网页网址
        :return: None
        """
        dic = {}  # 字典
        id = self.urlCount  # 编号记录
        # 获取网页内容
        try:
            # 无法访问 这一句报错
            page = urllib.request.urlopen(url)
            # 接下来都是正常访问的情况
            self.urlCount += 1  # 网址编号++
            content = page.read().decode('UTF-8')
            # 获取编号
            dic['id'] = id
            # 获取网址
            dic['url'] = url
            # 获取标题
            dic['title'] = Remove.extract_title(content)
            # 获取图片 存储位置 : Image
            self.BFS_getImages(content)
            # 获取html正文
            html = Remove.remove_empty_line(Remove.remove_js_css(content))
            html = Remove.remove_any_tag(html)
            html = Remove.remove_empty_line(html)
            dic['html'] = html  # 加入字典
            # print(Color.carmine, dic['html'])

            # 写入文件 'html<num>.txt'
            # file_ob = open(self.htmlPath + 'html' + str(id) + '.txt', 'w', encoding='utf-8')
            # # file_ob.write(json.dumps(dic, ensure_ascii=False))
            # file_ob.write(str(dic))
            # file_ob.close()

            with codecs.open(self.htmlPath + 'html' + str(id) + '.txt', 'w', encoding='utf-8') as f:
                json.dump(dic, f)

            print(Color.green + "# HTML DATA Writing Successfully...")
            # 获取子网页
            childList = self.BFS_extract_a_label(content)
            return childList
        except Exception as e:
            print(Color.red + '# 无法访问此网址...', e.args)
            return []  # 无法访问返回空

    def BFS_GetInfo(self, ceedUrl, quantity):
        """
        :param ceedUrl: 种子网站
        :param quantity: 爬取数量
        :return: None
        """
        # 布隆过滤器
        bf = BloomFilter(quantity + 10)
        # 列表作队列 尾部为队首 pop():弹出最后一个,insert(0,''):开始插入一个
        urlQueue = [ceedUrl]  # 先进先出
        # 队列不为空 爬爬爬~
        hadCount = 0
        while urlQueue:
            url = urlQueue.pop()
            print(Color.blue + '# 正在爬取：' + url)
            bf.insert(url)  # 计入过滤器
            childList = self.BFS_cuteCrawler(url)
            print(Color.carmine + '# 已爬取网站数:', self.urlCount, ' 图片数:', self.imgCount)
            # 退出循环
            if self.urlCount >= quantity:
                break
            # 筛选网址
            # print(childList)
            newChildList = []
            for index in childList:
                if index != '' and 'https' in index:
                    newChildList.append(index)
            # 子网址加入队列
            if newChildList is not None:
                for index in newChildList:
                    # index 需要查重！！！
                    if bf.is_contain(index) == 0:  # 不包含
                        urlQueue.insert(0, index)
                        hadCount += 1

########################################################################################################################


# 运行
if __name__ == '__main__':
    # url = 'https://www.keaitupian.cn/meinv/'
    url = 'http://www.sina.com.cn'  # 新浪
    # url = 'http://tieba.baidu.com/'
    quantity = 1000  # 广度爬1000

    htmlPath = "Data_bfs/Html/"
    childPath = "Data_bfs/Child/"
    imagePath = "Data_bfs/Image/"
    cute = BFSCrawler(htmlPath, childPath, imagePath)
    cute.BFS_GetInfo(url, quantity)  # 广度遍历
    pass
