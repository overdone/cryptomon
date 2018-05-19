import smtplib

from cryptomon.ext_api.etherscan import EtherScan


def send_mail(mail_server, mail_user, mail_pass,
              from_addr, to_addr, subject, body_text):
    body = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP(mail_server)
    server.ehlo()
    server.starttls()
    server.login(mail_user, mail_pass)
    server.sendmail(from_addr, [to_addr], body)
    server.quit()


def last_price_alarm(**kwargs):
    msg = ''
    api = EtherScan(
        kwargs['ether_scan_api_root'],
        kwargs['ether_scan_api_key'],
    )

    price = float(api.get_last_price())

    if price <= kwargs['check_threshold_min']:
        msg = 'Minimum threshold({min}) exceeded. Current price is: {current}'.format(
            min=kwargs['check_threshold_min'],
            current=price
        )

    if price >= kwargs['check_threshold_max']:
        msg = 'Maximum threshold({max}) exceeded. Current price is: {current}'.format(
            max=kwargs['check_threshold_max'],
            current=price
        )

    if msg != '':
        send_mail(kwargs['mail_server'],
                  kwargs['mail_user'],
                  kwargs['mail_pass'],
                  kwargs['mail_from'],
                  kwargs['mail_to'],
                  'Threshold exceeded',
                  msg)



