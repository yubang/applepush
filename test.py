# coding:UTF-8

from applepush import ApplePush

apns = ApplePush('证书路径', 'bundle ID')
print apns.single_push('苹果设备token', "推送内容")
apns.doc()