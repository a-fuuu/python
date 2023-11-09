import requests

# Webhook URL
webhook_url = "Webhook_url"

a = ['김치', '피자', '탕수육']
al = ', '.join(a)
version = '1.4.11'
# 메시지
message = f"추가된 Tag : {al} | 버전 : {version} | modelmapping git pull을 통해 최신 tag library를 받으세요"
# print(message)
# Webhook에 메시지를 보냅니다.
requests.post(webhook_url, json={"text": message})