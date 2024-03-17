import requests


def get_page():
    url = 'https://github.com/trending'

    headers = {
        'authority': 'github.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache'
    }

    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打印获取到的页面内容
        # print(response.text)
        return response.text
    else:
        print("请求失败，状态码：", response.status_code)
        return ""
