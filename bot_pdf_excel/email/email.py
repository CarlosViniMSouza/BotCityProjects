from botcity.plugins.email import BotEmailPlugin

"""
recipient = destinatario
topic = assunto
content = conteudo
"""

def send_email(recipient, topic, content):
    email = BotEmailPlugin()
    
    email.configure_imap("imap.gmail.com", 993)
    email.configure_smtp(host_address="smtp.gmail.com", port=587)

    email.login(email="botcityifam@gmail.com", password="licp pjdk zdet japu")

    to = [recipient]
    subject = topic
    body = content

    email.send_message(subject, body, to, use_html=True)
    email.disconnect()

# same as the function above
def send_email_attachment(recipient, topic, content, attachment):
    email = BotEmailPlugin()
    
    email.configure_imap("imap.gmail.com", 993)
    email.configure_smtp(host_address="smtp.gmail.com", port=587)

    email.login(email="botcityifam@gmail.com", password="licp pjdk zdet japu")

    to = [recipient]
    subject = topic
    body = content
    files = [attachment]

    email.send_message(subject, body, to, attachments=files, use_html=True)
    email.disconnect()
