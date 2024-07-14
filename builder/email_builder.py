from email_message import EmailMessage


class EmailBuilder():
    def __init__(self) -> None:
        self._email_message = EmailMessage()
        
    def add_from(self, from_: str):
        self._email_message.set_from(from_)
        return self
    def add_to(self, to: str):
        self._email_message.set_to(to)
        return self
    def build(self):
        return self._email_message