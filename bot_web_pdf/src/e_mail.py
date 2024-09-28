from botcity.plugins.email import BotEmailPlugin

def send_email_attachment(recipient, topic, content, attachment):
    # recipient = destinatario | topic = assunto
    # content = conteudo | attachment = anexo 

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

def send_email(recipient, topic, content):
    # recipient = destinatario | topic = assunto | content = conteudo

    email = BotEmailPlugin()
    
    email.configure_imap("imap.gmail.com", 993)
    email.configure_smtp(host_address="smtp.gmail.com", port=587)

    email.login(email="botcityifam@gmail.com", password="licp pjdk zdet japu")

    to = [recipient]
    subject = topic
    body = content

    email.send_message(subject, body, to, use_html=True)
    email.disconnect()