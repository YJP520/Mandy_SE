"""
@Project : spider
@Time : 2022/11/20
@Author : YU.J.P
@Version: 1.0
@CopyRight: YU.J.P
"""

import requests


# 抓取百度的搜索结果，放到自己的页面上
def get_result(keyword):

    header = {
        # 浏览器的信息 反爬
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 '
    }

    res = requests.get('https://www.baidu.com/s?wd={}'.format(keyword), headers=header)
    # res = requests.get('https://www.baidu.com/s?wd={}'.format(keyword))
    # 返回百度搜索的源码
    res.encoding = "utf-8"
    result = res.text
    # print(result)
    return result


# MAIN
if __name__ == '__main__':
    get_result('小姐姐')
    pass