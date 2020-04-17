from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailClient:

    def send_email(self, api_key, from_email, to_email, subject, body):
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=body)
        sendgrid_client = SendGridAPIClient(api_key=api_key)
        sendgrid_client.send(message)
