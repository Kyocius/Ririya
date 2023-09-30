## Ririya

> 北邮人技术考核 Task 3: Simple TODO

尝试仅使用 Socket 实现的简单 Http 服务器。

### 完成情况

太菜了，从 Flask 抄了路由但又没能实现像 Flask 那样的 `url/<varrible index>`，所以没办法实现动态生成和动态查询，只能硬写死在各个 id 的路由里。

- 实现：添加 TODO 项
- 实现：根据 `id` 查看具体列表
- 实现：删除某项
- 未实现：修改某项（怪，在改了）

### 使用方法
```
python3 run.py
```
### 文件结构
- app：
  - scaffold.py: `App` 主类， `request` 和 `response` 类
  - server.py: TCP 监听服务
- run.py: 运行脚本

