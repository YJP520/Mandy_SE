

str1 = "<!DOCTYPE html>\n"
str2 = '<html lang="en" dir="ltr">\n<head>\n'
str3 = '\t<meta charset="utf-8">\n'
str4 = "\t<title>Mandy Search</title>\n"
str5 = '\t<style type="text/css">\n'
str6 = '\t\t* {\n\t\t\tbox-sizing: border-box;\n\t\t}\n\n'
str7 = '\t\tbody {\n\t\t\tbackground: -webkit-linear-gradient(to right, #00EE00, #00E5EE);' \
       '\n\t\t\tbackground: linear-gradient(to right, #00EE00, #00E5EE);\n\t\t}\n\n'
str8 = "\t\ta{\n\t\t\ttext-decoration: none;\n\t\t\tfont-size: 18px;\n\t\t\tcolor: #F9F0DA;\n\t\t}\n\n"
str9 = '\t</style>\n</head>\n<body>\n'

str10 = '</body>\n</html>'


def write_text(path, title, text, max, begin):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9)
        f.close()
    for index in range(max):
        s2 = '\t<div class="item">\n'
        s3 = '\t\t<a  href="/t'
        s4 = '" target="_blank">'
        s5 = '</a>\n\t\t<p>\n\t\t\t'
        s6 = "\n\t\t</p>\n\t</div>\n"
        with open(path, 'a', encoding='utf-8') as f:
            f.write(s2+s3+str(index+1)+"?t="+str(int(begin/5)+1)+s4+title[index+begin]+s5+text[index+begin]+s6)
            f.close()
    with open(path, 'a', encoding='utf-8') as f:
        f.write(str10)
        f.close()


write_text("../Src/templates/result2.html", ['1', '2', '3', '4', '5'], ['text1', 'text2', 'text3', 'text4', 'text5'], 5, 0)
