from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from auth import Auth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class AuthResourse(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = Auth()
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")
    
        @self.post("/register")
        def register(form_data: OAuth2PasswordRequestForm = Depends()):
            return self.auth.signup(form_data.username, form_data.password, form_data.username)
        
        @self.get("/register/{username}/{code}")
        def confirm(username: str, code: str):
            return self.auth.confirm(username, code)
        
        @self.post("/token")
        def token(form_data: OAuth2PasswordRequestForm = Depends()):
            return self.auth.token(form_data.username, form_data.password)

        @self.get("/user_info")
        def user_info(request: Request):
            access_token = request.headers["Authorization"].split(" ")[1]
            return self.auth.user(access_token)
        
        @self.get("/user_info/{access_token}")
        def user_info(access_token: str):
            return self.auth.user(access_token)