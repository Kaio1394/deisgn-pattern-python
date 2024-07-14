from email_builder import EmailBuilder
from email_message import EmailMessage


email_msg = (
    EmailBuilder()
        .add_to("from@hotmail.com")
        .add_from("to@hotmail.com")
        .build()
    )
email_msg.send()