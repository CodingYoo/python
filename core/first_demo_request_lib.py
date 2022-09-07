import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=1)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.status_code
    except:
        return "请求失败！"


if __name__ == '__main__':
    url = "https://www.baidu.com"
    print(getHTMLText(url))
