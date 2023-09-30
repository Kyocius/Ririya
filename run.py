from app import (start, App)

app = App()

data = [{'task': 1}, {'task': 2}, {'task': 3}]


@app.route('/api/list')
def route_index():
    return app.response.send_json(data)


@app.route("/api/list/new")
def route_new():
    if app.request.method == "POST":
        data.append(app.request.data_json)
        return app.response.send_json({'id': len(data)})
    else:
        return app.response.bad_request()

# 没有实现 <varrible index> 所以只能将方法硬写死在不同 id 的路由下
@app.route("/api/list/1")
def route_1():
   render(1)

@app.route("/api/list/2")
def route_2():
    render(2)

@app.route("/api/list/3")
def route_3():
    render(3)

def render(i: int = 1):
    if app.request.method == "GET":
        return app.response.send_json(data[i-1])
    elif app.request.method == "DELETE":
        del data[i-1]
        return app.response.send_json({'code': 200})
    elif app.request.method == "POST":
        data[i-1] == app.request.data_json
        return app.response.send_json({'code': 200})
    else: 
        return app.response.not_implemented()

start(app, __name__)
