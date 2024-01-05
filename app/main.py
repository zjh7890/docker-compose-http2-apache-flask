from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.route("/")
def hello():
    delay_ns = request.args.get('delay', default=0, type=int)

#    delay_ns = int(request.GET['delay'])
    time_begin = time.time_ns()
    while True:
        duration = time.time_ns() - time_begin
        if duration > delay_ns:
            break
    time.sleep(delay_ns/1000000000)  #########################################################
    time_end = time.time_ns()
    astr = "%dxxx%d" % (time_begin, time_end)
    aastr = ":%d" % (time_begin)
    return astr

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3030, debug=True) #threaded=True)