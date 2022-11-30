"""
@Project : Selenium spider
@Time : 2022/11/24
@Author : YU.J.P
@Version: 1.0
@CopyRight: YU.J.P
"""

# 自动化爬取
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# 数据库
from link_database import insert_jd_link

########################################################################################################################


def get_goods(browser):
    """
    获取指定的信息
    :param browser:
    :return:
    """
    # 查找多节点 查找到所有的li标签
    goods = browser.find_elements(By.CLASS_NAME, 'gl-item')
    # 地址 名字 价格 评论
    for good in goods:
        # 地址
        link = good.find_element(By.TAG_NAME, value='a').get_attribute('href')
        # 名字 css选择器
        name = good.find_element(By.CSS_SELECTOR, value='.p-name em').text.replace('\n', '')
        # 价格
        price = good.find_element(By.CSS_SELECTOR, value='.p-price i').text
        # 评论
        comment = good.find_element(By.CSS_SELECTOR, value='.p-commit a').text
        # 字符串格式化
        # msg = '''
        #     商品 : %s
        #     链接 : %s
        #     价钱 : %s
        #     评论 : %s
        # ''' % (name, link, price, comment)
        # print(msg)
        insert_jd_link(link, name, price, comment)
    time.sleep(10)


def auto_spider(url, keyword):
    """
    自动化爬虫 - ChromeDriver
    :param url: 待爬取网址
    :param keyword: 关键词
    :return: None
    """
    browser = webdriver.Chrome()
    # 访问指定网页
    browser.get(url)
    # 隐式等待 确保内容结点完全加载出来
    browser.implicitly_wait(3)
    # 定位搜索框
    # 找到id属性为key的标签
    input_tag = browser.find_element(by='id', value='key')
    # 模拟键盘输入关键词
    input_tag.send_keys(keyword)
    # 模拟键盘输入enter键
    input_tag.send_keys(Keys.ENTER)
    # 数据抓取
    get_goods(browser)
    # 等待5秒钟
    time.sleep(30)

########################################################################################################################


# MIAN
if __name__ == "__main__":
    # auto_spider('https://www.jd.com', '口罩')
    auto_spider('https://www.jd.com', '酒精')
    auto_spider('https://www.jd.com', '防护服')
    auto_spider('https://www.jd.com', '消毒液')
    auto_spider('https://www.jd.com', '连花清瘟')
    auto_spider('https://www.jd.com', '医疗包')
    auto_spider('https://www.jd.com', '压缩饼干')
    auto_spider('https://www.jd.com', '牛奶')
    auto_spider('https://www.jd.com', '鸡蛋')
    auto_spider('https://www.jd.com', '饼干')
    auto_spider('https://www.jd.com', '面包')


    pass