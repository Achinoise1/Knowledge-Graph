from flask import Flask

app = Flask(__name__)

# 少了个@符号就变成NotFound了？
# 通过路由绑定视图函数
# 视图函数得有返回值
@app.route('/')
def hello():
    return "Hello"

@app.route('/')
def hello1():
    return "Hell"

# 是否直接用当前模块运行
if __name__ == '__main__':
    print(app.url_map)
    # 默认端口为5000    http://127.0.0.1:5000 
    app.run()
    
    
# object.url_map 查看哪些路由(地址)可以直接访问
# 也就是说每当我绑定一个，就可以访问多一个路径？
