# applepush
*一个基于python2和http2的苹果推送SDK*

### 安装

```
pip install applepush
```

### 使用

```

# coding:UTF-8

from applepush import ApplePush

apns = ApplePush('证书路径', 'bundle ID')
print apns.single_push('苹果设备token', "推送内容")

```

### 函数返回值

```

{
    'status': 成功为200，错误为其它,
    'headers': {
      'apns-id': 苹果推送返回的UUID,
    },
    'data': 苹果接口返回的字符串,
    'error_msg': 错误原因，如果推送成功为None
}

status请参考：https://developer.apple.com/library/prerelease/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html#//apple_ref/doc/uid/TP40008194-CH11-SW15

```

### 打印帮助文档
```

from applepush import ApplePush

apns = ApplePush('证书路径', 'bundle ID')
apns.doc()

```