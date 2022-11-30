"""
@Project : Flask Web
@Time : 2022/11/24
@Author : YU.J.P
@Version: 1.0
@CopyRight: YU.J.P
"""

from flask import Flask
from flask import render_template
from flask import request
from createHtml import write_text
from Auto.link_database import search_index
from Core.abstract import TFIDF_Abstract
from Core.Plug_in.Colors import Color

########################################################################################################################
# Running on http://127.0.0.1:5000
# 127.0.0.1 本机域名 未上线
# Flask(__name__).run()

# Flask 框架
app = Flask(__name__)


########################################################################################################################

@app.route('/')  # http://127.9.9.1:5000/
def index():
    # 前端代码 flask后端
    # return ''  规定
    return render_template('index.html')


@app.route("/j")
def jump():
    # 重新加载初始页面
    return render_template('index.html')


# http://127.9.9.1:5000/s?wd=python
@app.route("/s")
def search():
    keyword = request.args.get('wd')
    # print(keyword)
    # 输入词是否为空
    if not keyword:
        # 重新加载当前页面
        return render_template('index.html')
    else:
        # return get_result(keyword)  # 搜索的结果 爬虫爬取的数据
        # 数据库获取信息
        data = search_index(keyword)
        titles, links, texts = [], [], []
        for link, name, price, comment in data:
            try:
                # 获取标题
                ob = TFIDF_Abstract(keyword, name, 20)
                title = ob.abstract + '...'
            except Exception as e:
                # 如果出错
                print(Color.red, e.args)
                title = name[0:20] + '...'
            titles.append(title)
            links.append(link)
            texts.append(name)

        # 返回结果是否为空
        if len(titles) == 0:
            return render_template('blank.html')
        else:
            write_text("templates/result.html", keyword, titles, links, texts, len(titles))
            return render_template('result.html')


########################################################################################################################

# 每次修改代码后，自动重启 port 默认端口 5000
app.run(debug=True)
