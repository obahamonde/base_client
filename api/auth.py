from services import CloudService
from typing import List, Dict, Optional, Any, Union, Tuple, Callable
from dotenv import load_dotenv
from os import getenv
from hashlib import sha256

load_dotenv()

USER_POOL_ID = getenv("USER_POOL_ID")
APP_CLIENT_ID = getenv("APP_CLIENT_ID")

class Auth:
    def __init__(self):
        self.auth = CloudService().auth
    
    def signup(self,  username: str, password: str, email: str):
        """Register Endpoint"""
        try:
            self.auth.sign_up(
                ClientId=APP_CLIENT_ID,
                Username=username,
                Password=sha256(password.encode()).hexdigest()+sha256(password.encode()).hexdigest().upper()+"#",
                UserAttributes=[
                    {
                        "Name": "email",
                        "Value": email
                    }
                ]
            )
            return {"message": "Verification code sent to email"}
        except Exception as e:
            return {"message": str(e)}

    def confirm(self, username: str, code: str):
        """Authorize Endpoint"""
        try:
            self.auth.confirm_sign_up(
                ClientId=APP_CLIENT_ID,
                Username=username,
                ConfirmationCode=code
            )
            return {"message": "User confirmed"}
        except Exception as e:
            return {"message": str(e)}
        
    def token(self, username: str, password: str):
        """Token Endpoint"""
        try:
            response = self.auth.initiate_auth(
                ClientId=APP_CLIENT_ID,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": username,
                    "PASSWORD": sha256(password.encode()).hexdigest()+sha256(password.encode()).hexdigest().upper()+"#"
                }
            )
            return response["AuthenticationResult"]
        except Exception as e:
            return {"message": str(e)}
        
    def user(self, token:str):
        """User Info"""
        try:
            response = self.auth.get_user(
                AccessToken=token
            )
            return {i["Name"]: i["Value"] for i in response["UserAttributes"]}
        except Exception as e:
            return {"message": str(e)}