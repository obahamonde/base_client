from boto3 import Session

class CloudService(Session):
    @property
    def storage(self):
        return self.client("s3")
    
    @property
    def database(self):
        return self.resource("dynamodb")
    
    @property
    def email(self):
        return self.client("ses")
    
    @property
    def auth(self):
        return self.client("cognito-idp")