from urllib.request import urlopen

def get_url():
    url = "http://www.baidu.com/index.html"
    def get():
        return urlopen(url).read()
    return get

baidu_url = get_url()
print(baidu_url())