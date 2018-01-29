# 导入相关库文件
import requests
import re
import time


# 访问头文件
_headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
            }

# 新建txt文档，追加模式
f = open("/Users/zhangzheng/Documents/GitHub/Doupoxs_re/Doupo.txt", "a+")


def get_info(url):

    res = requests.get(url, headers=_headers)

    # 网址请求成功进入
    if res.status_code == 200:

        contents = re.findall("<p>(.*?)</p>", res.content.decode("utf-8"), re.S)

        for content in contents:

            print(content)

            # 写入文件
            f.write(content+"\n")

    else:
        pass


if __name__ == "__main__":

    # 遍历网址
    urls = ["http://www.doupoxs.com/doupocangqiong/{}.html".format(str(i))
            for i in range(2, 100)]

    # print(urls)

    for url in urls:

        get_info(url)

        # print(url)

        # 睡眠一秒
        time.sleep(1)


f.close()
