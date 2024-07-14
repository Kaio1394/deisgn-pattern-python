class EmailMessage:
    def __init__(self) -> None:
        self._from_ = ""
        self._to = ""
        self._cc = ""
        self._bcc = ""
        self._subject = ""
        self._body = ""
        self._attachments = ""
        
    def get_cc(self):
        return self._cc
    def get_to(self):
        return self._to
    def get_from(self):
        return self._from_
    def get_bcc(self):
        return self._bcc   
    def get_subject(self):
        return self._subject   
    def get_body(self):
        return self._body    
    def get_attachments(self):
        return self._attachments
    
    def set_attachments(self, value):
        self._attachments = value        
    def set_to(self, value):
        self._to = value        
    def set_body(self, value):
        self._body = value    
    def set_subject(self, value):
        self._subject = value   
    def set_cc(self, value):
        self._cc = value        
    def set_from(self, value):
        self._from_ = value
    def set_bcc(self, value):
        self._bcc = value
    def send(self):
        print(f"Email succesfully sent:")
        print(f"-----------------------")
        print(f"FROM: {self._from_}")
        print(f"TO: {self._to}")
        print(f"CC: {self._cc}")
        print(f"BCC: {self._bcc}")
        print(f"SUBJECT: {self._subject}")
        print(f"ATTACHMENTS: {self._attachments}")
        
    # def set_from(self, address_from: str):
    #     self._from = address_from
    # def set_to(self, address_to: str):
    #     self._to = address_to
    # def set_body(self, body: str):
    #     self._body = body
    # def get_to(self):
    #     return self._to
    # def get_cc(self):
    #     return self._cc
    # def get_bcc(self):
    #     return self._bcc
    # def get_attachments(self):
    #     return self._attachments
    
    