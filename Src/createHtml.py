"""
@Project : Auto Write Html
@Time : 2022/11/24
@Author : YU.J.P
@Version: 1.0
@CopyRight: YU.J.P
"""

########################################################################################################################


html1 = "<!DOCTYPE html>\n"
html2 = '<html lang="en" dir="ltr">\n<head>\n'
html3 = '\t<meta charset="utf-8">\n'
html4 = "\t<title>(づ￣3￣)づ╭❤～Mandy</title>\n"

css1 = '\t<style type="text/css">\n'
css2 = '\t\t* {\n\t\t\tbox-sizing: border-box;\n\t\t}\n\n'
css3 = '\t\tbody {\n\t\t\tbackground: -webkit-linear-gradient(to right, #C1FFC1, #AEEEEE);\n' \
       '\t\t\tbackground: linear-gradient(to right, #C1FFC1, #AEEEEE);\n\t\t}\n\n'
css4 = '\t\t.MandySearch {\n\t\t\twidth: 90%;\n\t\t\tmargin: 0 auto;\n\t\t\theight: 8rem;\n' \
       '\t\t\tdisplay: flex;\n\t\t\talign-items: center;\n\t\t}\n\n'
css5 = '\t\t.MandySearch form {\n\t\t\twidth: 70%;\n\t\t\tdisplay: flex;\n\t\t\tjustify-content: center;\n\t\t}\n\n'

css6 = '\t\t.MandySearch a {\n\t\t\tfont: "微软雅黑";\n\t\t\tfont-weight: bolder;\n\t\t\tfont-size: 30px;\n' \
       '\t\t\tcolor: #3B3B3B;\n\t\t}\n\n'
css7 = '\t\t.MandySearch a:hover {\n\t\t\ttext-decoration: none;\n\t\t\tcolor: #FF8C00\n\t\t}\n\n'
css8 = '\t\t.MandySearch input {\n\t\t\tborder: none;\n\t\t\toutline: none;\n\t\t\theight: 42px;\n\t\t\twidth: 75%;' \
       '\n\t\t\tpadding-left: 13px;\n\t\t\tborder: 2px solid #FFA07A;\n\t\t\tborder-radius: 19px;' \
       '\n\t\t\tbackground: transparent;\n\t\t\tfont-size: 18px;\n\t\t}\n\n'
css9 = '\t\t.MandySearch button {\n\t\t\tborder: none;\n\t\t\toutline: none;\n\t\t\tfont-size: 18px;\n' \
       '\t\t\tcolor: #F9F0DA;\n\t\t\t\n\t\t\theight: 42px;\n\t\t\ttwidth: 42px;\n\t\t\tcursor: pointer;\n' \
       '\t\t\tbackground: #EE6A50;\n\t\t\tborder-radius: 0 19px 19px 0;\n' \
       '\t\t\twidth: 60px;\n\t\t\tmargin-left: -3rem;\n\t\t}\n\n'
css10 = '\t\t.MandySearch button:hover {\n\t\t\tbackground-color: #CD3700;\n\t\t}\n\n'
css11 = '\t\t.MandySearch button:before {\n\t\t\tfont-size: 18px;\n\t\t\tcolor: #F9F0DA;\n\t\t}\n\n'
css12 = '\t\t.main {\n\t\t\twidth: 90%;\n\t\t\tmargin:0 auto;\n\t\t}\n\n'
css13 = '\t\t.item {\n\t\t\twidth: 70%;\n\t\t\tpadding: 1.5rem 0;\n\t\t\tborder-bottom: 1px solid blue;\n\t\t}\n\n'
css14 = '\t\t.item cite {\n\t\t\tcolor: #006d21;\n\t\t\tfont-style: normal;\n\t\t}\n\n'
css15 = '\t\ta {\n\t\t\ttext-decoration: none;\n\t\t\tfont-size: 1.5rem;\n\t\t\tcolor: #454545;\n\t\t}\n\n'
css16 = '\t\ta:hover {\n\t\t\ttext-decoration: underline;\n\t\t\tcolor: #8A2BE2;\n\t\t}\n\n'
css17 = '\t\tp {\n\t\t\tcolor: #777;\n\t\t}\n\n'
css18 = '\t</style>\n</head>\n<body>\n'

html5 = '\t<div class="MandySearch">\n\t\t<a href="/s">Mandy</a>\n' \
        '\t\t<form action="/s" method="get">\n\t\t\t<input value="'
html6 = '" name="wd" type="text">\n\t\t\t<button type="submit">GO</button>\n\t\t</form>\n\t</div>\n\n'

js1 = '\t<script>\n\t\tvar keyword = "'
js2 = '"\n\t\tvar doc = document.querySelectorAll("p")\n\t\tvar doc2 = document.querySelectorAll("a")\n'
js3 = '\t\tfor(let i = 0; i < doc.length; i++) {\n'
js4 = '\t\t\tdoc[i].innerHTML = doc[i].innerText.split(keyword).join(`<span style="color: red;">${keyword}</span>`)\n'
js5 = '\t\t\tdoc2[i].innerHTML = doc2[i].innerText.split(keyword).join(`<span style="color: red;">${keyword}</span>`)\n'
js6 = '\t\t}\n\t</script>\n'


########################################################################################################################


def write_text(path, keyword, title, link, text, quantity):
    # html头部 css 样式 搜索框
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html1 + html2 + html3 + html4 + css1 + css2 + css3 + css4 + css5 + css6 +
                css7 + css8 + css9 + css10 + css11 + css12 + css13 + css14 + css15 + css16 +
                css17 + css18 + html5 + keyword + html6)
        f.close()
    # 返回的内容 html
    for index in range(quantity):
        s1 = '\t<div class="main">\n'
        s2 = '\t\t<div class="item">\n'
        s3 = '\t\t\t<a href="' + link[index]  # 插入网页链接
        s4 = '" target="_blank">\n\t\t\t' + title[index]  # 中间插入标题
        s5 = '\n\t\t\t</a><br>\n\t\t\t<cite>\n\t\t\t\t' + link[index]  # 插入网页链接
        s6 = '\n\t\t\t</cite>\n\t\t\t<p>\n\t\t\t\t' + text[index]  # 中间插入内容
        s7 = "\n\t\t\t</p>\n\t\t</div>\n\t</div>\n"

        with open(path, 'a', encoding='utf-8') as f:
            f.write(s1 + s2 + s3 + s4 + s5 + s6 + s7)
            f.close()
    # js + 尾部
    with open(path, 'a', encoding='utf-8') as f:
        # js
        f.write(js1 + keyword + js2 + js3 + js4 + js5 + js6)
        # 尾巴
        f.write('</body>\n</html>')
        f.close()


########################################################################################################################


# MIAN
if __name__ == "__main__":
    write_text("../Src/templates/result2.html", 'keyword', ['1', '2', '3', '4', '5'],
               ['text1', 'text2', 'text3', 'text4', 'text5'], 5)
