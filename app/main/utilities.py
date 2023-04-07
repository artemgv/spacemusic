import re
from django.template.loader import render_to_string
from django.core.signing import Signer
from django.conf import settings
from datetime import datetime
from os.path import splitext


signer = Signer()


# Функция, генерирующая имена сохраняемых в модели выгруженных файлов
def get_timestamp_path(instance, filename):
    return "%s%s" % (datetime.now().timestamp(), splitext(filename)[1])


# См. объявление сигнала в модуле apps.py и отправку этого сигнала из form.py
# Также вызывается из функции send_new_comment_notifications модуля admin.py
def send_activation_notification(user):
    if settings.ALLOWED_HOSTS:
        host = "http://" + settings.ALLOWED_HOSTS[0]
    else:
        host = "http://localhost:8000"
    context = {"user": user, "host": host, "sign": signer.sign(user.username)}
    subject = render_to_string("email/activation_letter_subject.txt", context)
    subject = re.sub(r"^\s+|\n|\r|\s+$", "", subject)
    body_text = render_to_string("email/activation_letter_body.txt", context)
    user.email_user(subject, body_text)
