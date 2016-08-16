+ 可以使用如下代码获取flask的url mapping信息
```python
>>> from test02 import app
>>> app.url_map
Map([<Rule '/appname' (HEAD, OPTIONS, GET) -> user>,
 <Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>])
```
+ 我们可以看到有一个Rule是/static/<filename>, 这个是flask默认的static文件夹位置
