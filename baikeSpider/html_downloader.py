import urllib.request

# python3.X 版本是不需要安装 urllib2 包的， urllib 和 urllib2 包集合成一起
# 所以如何使用： urllib2.urlopen()?
# import urllib.request
# resp = urllib.request.urlopen("http://www.baidu.com")


class HtmlDownloader(object):

    @staticmethod
    def download(url):

        if url is None:
            return None

        try:
            resp = urllib.request.urlopen(url, timeout=10)
            # 声明 download 的时候不要用 response = urllib.request.urlopen(url);
            # 因为 response 已经被 python 占用， 可以改为 resp = urllib.request.urlopen(url);
            # 这样就不会出现 response 没有 getcode 用法的问题了
            if resp.getcode() != 200:
                return None
            return resp.read()

        except Exception as e:
            print(str(e))




