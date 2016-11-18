# coding:UTF-8


"""
基于HTTP2的苹果推送
@author: yubang
创建于2016年11月18日
"""

from hyper import HTTPConnection, tls
import re
import json


class ApplePush:
    def __init__(self, cert, apns_topic):
        self.cert = cert
        self.headers = {"apns-topic": apns_topic}
        self.api_url = 'api.development.push.apple.com:443'
        self.api_path = '/3/device/%s'

    def get_api_path(self, token):
        """
        获取请求的API路径
        :param token:
        :return:
        """
        return self.api_path % token

    @staticmethod
    def make_response(r):
        """
        封装返回对象
        :param r:
        :return:
        """
        data = r.read()
        try:
            data = json.loads(data)
        except ValueError:
            data = {}
        status = r.status

        return {
            "data": data,
            "status": status,
            "error_msg": data.get('reason', '未知错误') if data else None,
            "headers": dict(r.headers)
        }

    @staticmethod
    def handle_token(token):
        """
        处理token
        :param token: 苹果设备token
        :return:
        """
        if re.match(r'<.*?>', token):
            token = token[1:-1]
        return token.replace(" ", '')

    def single_push(self, token, alert, badge=1):
        """
            发送单个设备
            :param token:设备
            :param alert:弹出的消息
            :param badge:红点数字
            :return:
            """
        token = self.handle_token(token)
        payload = {
            'aps': {
                'alert': alert,
                'sound': 'default',
                'badge': badge,
            }
        }
        conn = HTTPConnection(self.api_url, ssl_context=tls.init_context(cert=self.cert))
        conn.request('POST', self.get_api_path(token), body=json.dumps(payload), headers=self.headers)
        resp = conn.get_response()
        return self.make_response(resp)


