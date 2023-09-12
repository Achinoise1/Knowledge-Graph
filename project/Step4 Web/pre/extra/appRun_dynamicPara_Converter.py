from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class SelfConverter(BaseConverter):
    def __init__(self,map,regex):
        super(SelfConverter,self).__init__(map)
        self.regex = regex

app.url_map.converters["Emm"] = SelfConverter       #Emm就是我自己定义的类型

@app.route('/<Emm("\d{3}"):age>')
def Hell(age):
    return "WOW Fantastic %s"%age

'''@app.route('/<int:age>')
def Hell(age):
    return "WOW Fantastic %s"%age   #转成str'''

# 注意视图函数别重名

'''@app.route('/<float:age>')
def Hell1(age):
    return "WOW Fantastic %s"%age   #转成str

@app.route('/<path:age>')            #没有str，但是path(好像还有string) 不特意注明的情况下，就是path类型
def Hell2(age):
    return "WOW Fantastic %s"%age   #转成str'''

if __name__ == '__main__':
    #default
    #app.run(host = "127.0.0.1",port = 5000,debug = False)
    app.run(host = "127.0.0.1",port = 5002,debug = True)