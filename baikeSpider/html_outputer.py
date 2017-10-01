
class Htmloutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<html>\n")
        fout.write("<head>\n")
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"> \n')

        fout.write("</head>\n")

        fout.write("<body>\n")
        fout.write("<table border='1'>\n")

        for data in self.datas:
            fout.write("<tr>\n")
            fout.write("<td>%s</td>\n" % data['url'])
            fout.write("<td>%s</td>\n" % data['title'])
            fout.write("<td>%s</td>\n" % data['summary'])

        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")

