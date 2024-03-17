import schedule
from flask import Flask, render_template
from parse import parse_data
from parse import extracted_data

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('base.html', repositories=extracted_data)

if __name__ == "main":
    parse_data()
    # 每个一个小时调用一次 parse，并获取返回值，保存到 items 全局变量
    schedule.every(1).hours.do(parse_data)
    app.run(host='0.0.0.0', port=3030, debug=True) #threaded=True)
