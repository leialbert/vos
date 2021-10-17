# 黑名单管理系统开发记录

## 开发环境
    Python 3.8.5
    Flask 1.1.2
    Werkzeug 1.0.1
    mongodb 4.4.5
```python
pip install flask
pip install pymongo
pip install gunicorn
```
## 正式运行操作
1. 购买阿里云ECS，得到账号密码
2. 配置python3并安装相关扩展包
3. 给MongoDB创建数据库blacklist
4. 给数据库创建Collection，名字为phones
5. 导入去重后的数据字段为phone
6. 给phone创建索引
```
db.getCollection('phones').ensureIndex({phone:1},{background:true})
```

做好上述步骤后，直接使用gunicorn运行程序。
```
gunicorn run:app
```

## 常用命令记录
- 启动

## 正常运行
- 万次请求毫秒级响应
- 完美适配VoS外部黑名单系统
