
一、程序要求：
spider -> rabbitmq -> parser -> mongodb


二、说明：
1、这里写了两个project，一个是后端app，一个是spider（这个可以放在前一个里作为一个utils）。

spider说明：
1、只获取了https://www.weixinqun.com/group的一个页面，后续可下载所有页面。
2、没有用并发，后续优化可用多线程或者携程。


优化：
1、并发爬取页面
2、可设置多个消费队列，用多线程的方式分别完成html的消费，img下载的消费，使得parse和img下载进行解耦。
3、使用多线程的方式，对多个rabbitmq或queue进行消费
4、待定。




三、文件夹
卷 文档 的文件夹 PATH 列表
卷序列号为 000F-3273
D:.
│  README.md
│  
├─weixinqunBackend
│  │  db.sqlite3
│  │  manage.py
│  │  test.py
│  │  
│  ├─api  # 提供api给spider进行数据存储，以及提供后台页面数据。使用了restfulframework
│  │  │  admin.py
│  │  │  apps.py
│  │  │  models.py
│  │  │  serializer.py
│  │  │  tests.py
│  │  │  urls.py
│  │  │  views.py
│  │  │  __init__.py
│  │  │  
│  ├─static
	略   
│  │  ├─imgs
│  │  │      0f00110b7a94d702c33709e8fc0cd0e4.jpeg
│  │  │      116f948370dfc8d18aa234f56b6855d8.png
│  │  │      1bf10e5c934fe2ae66008119e5bd4068.jpeg
│  │  │      
│  ├─weixinqunBackend
│  │  │  settings.py
│  │  │  urls.py
│  │  │  wsgi.py
│  │  │  __init__.py
│  │  │  
│  └─wxqInfo  # 后台处理app
│      │  admin.py
│      │  apps.py
│      │  models.py
│      │  tests.py
│      │  urls.py
│      │  views.py
│      │  __init__.py
│      │  
│      ├─templates
│      │  │  list.html  # 群list的页面
│      │  │  
│      │  └─layout
│      │          layout.html        





──weixinqunSpider  # 爬虫app
    ├─bin
    │      run.py    # 程序入口
    │      
    ├─conf
    │  │  settings.py  # 配置文件
    │  │  
    │  └─__pycache__
    │          settings.cpython-36.pyc
    │          
    ├─logs
    │      error.log  # 日志文件
    │      system.log
    │      
    └─src
        │  api.py  # 发送到django的API，存入数据库
        │  container.py  # 容器，实现了get和put两个方法，rabbitMQ使用这个即可
        │  logger.py  # 日志
        │  main.py  # 主逻辑
        │  parse_handler.py  # 网页数据提取
        │  spider.py  # 爬虫
        │  
        └─__pycache__
                api.cpython-36.pyc
                container.cpython-36.pyc
                logger.cpython-36.pyc
                main.cpython-36.pyc
                parse_handler.cpython-36.pyc
                spider.cpython-36.pyc
                
