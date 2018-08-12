from django.core.cache import cache
from django.core.mail import send_mail
import uuid
import hashlib

def get_token():
    uuid_str = str(uuid.uuid4()).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

def send_active_email(email):
    token = get_token()
    cache.set(token, email, 60*10)
    from_email = "1187757450@qq.com"
    to = [email]
    subject = "爱鲜蜂会员激活邮件"
    confirm_url = "http://47.105.102.200:12348/axf/active/" + token
    content = "将以下激活连接复制到浏览器" + confirm_url
    send_mail(subject, content, from_email, to)