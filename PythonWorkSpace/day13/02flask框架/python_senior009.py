"""
--------------------------------
@Time    :  2022/2/22 - 14:16
@Author  :  Lee
@File    :  python_senior009
--------------------------------
"""

"""
flask框架介绍: 该框架为后端服务框架,能够部署服务,这样我们的接口/代码就能够使用http协议来调用
"""

# 第一步: 通过pip install 导入该库
import flask

# 第二步: 创建app对象,把当前的python文件当成一个服务,__name__代表当前文件
app = flask.Flask(__name__)


# 第三步:我们将接口发布成服务,route是路由的意思
@app.route('/index', methods=['post', 'get'])
def index():
    return 'tester24班的第一个接口服务'


@app.route('/home', methods=['post', 'get'])
def home():
    return '欢迎回家,今天幸苦了~'


if __name__ == '__main__':
    app.run(debug=True)  # 启动服务,使用debug模式启动服务,debug是可调式模式
