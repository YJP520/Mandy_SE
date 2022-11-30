"""
@Project : Flask Test
@Time : 2022/11/20
@Author : YU.J.P
@Version: 1.0
@CopyRight: YU.J.P
"""

from flask import Flask
from flask import render_template
from flask import request
from spider import get_result
from createHtml import write_text

# Running on http://127.0.0.1:5000
# 127.0.0.1 本机域名 未上线
# Flask(__name__).run()

app = Flask(__name__)


@app.route('/')  # http://127.9.9.1:5000/
def index():
    # 前端代码 flask后端
    # return ''  规定
    return render_template('index.html')


# http://127.9.9.1:5000/s?wd=python
@app.route("/s")
def s():
    keyword = request.args.get('wd')
    print(keyword)
    if keyword is None:
        return render_template('index.html')
    else:
        # return get_result(keyword)  # 搜索的结果 爬虫爬取的数据
        title = ['配图网-可爱图片_唯美图片_小清新图片大全',
                 '登录 ‹ 犀牛图片网',
                 '性感帅哥_让人心跳加速的性感帅哥写真图片照片大全-喃仁图',
                 '杨晨晨_清纯迷人的杨晨晨图片写真照作品大全-喃仁图',
                 '电视剧琉璃美人煞演员表-喃仁图']
        text = ['20款小公主发型扎法女生发型三十七种漂亮发型编法女生短发发型女生发型大全',
                '20款小公主发型扎法女生发型三十七种漂亮发型编法女生短发发型女生发型大全',
                '20款小公主发型扎法女生发型三十七种漂亮发型编法女生短发发型女生发型大全',
                '20款小公主发型扎法女生发型三十七种漂亮发型编法女生短发发型女生发型大全',
                '20款小公主发型扎法女生发型三十七种漂亮发型编法女生短发发型女生发型大全']
        write_text("templates/result2.html", title, text, 5, 0)
        return render_template('result2.html')


@app.route("/j")
def jump():
    keyword = request.args.get('wd')
    print(keyword)
    return render_template('index.html')


# 每次修改代码后，自动重启
# port 默认端口 5000
app.run(debug=True)
