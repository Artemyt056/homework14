import library


def main():
    recipients = ['artemyt056@ukr.net']
    mail_body = 'My great email'
    mail_subject = "For homework 14"

    library.send_email(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject

    )


if __name__ == '__main__':
    main()
