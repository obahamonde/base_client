from fastapi import *
from fastapi.responses import *
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.security import *

from typing import *
from pydantic import *
from datetime import datetime
from uuid import UUID, uuid4

from prisma import Prisma
from prisma.models import User, Todo, Phase, Board
from jwt import encode, decode

from boto3 import Session

from hashlib import sha256

class JWTEncoder:
    def __init__(self, secret: str):
        self.secret = secret
        
    def encode(self, payload: dict) -> str:
        return encode(payload, self.secret, algorithm="HS256")
    
    def decode(self, token: str) -> dict:
        return decode(token, self.secret, algorithms=["HS256"])

    def verify(self, token: str) -> bool:
        try:
            self.decode(token)
            return True
        except:
            return False
        
class UserIn(BaseModel):
    email: str
    password: str
    picture: str
    
    @property
    def hashed_password(self) -> str:
        return sha256(self.password.encode()).hexdigest()
    
    
    
class Auth(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = "/oauth2"
        self.oauth = OAuth2PasswordBearer(tokenUrl="api/oauth2/login")

        @self.post("/authorize")
        async def signup(user: UserIn):
            user = await User.prisma().create(data=user.dict())
            return {"message": "User created successfully"}
        
        @self.post("/token")
        async def login(form: OAuth2PasswordRequestForm = Depends()):
            user = await User.prisma().find_unique(where={"email": form.username})
            if user and user.hashed_password == sha256(form.password.encode()).hexdigest():
                encoder = JWTEncoder(form.username)
                token = encoder.encode(user.dict())
                return token
            else:
                raise HTTPException(status_code=401, detail="Invalid credentials")
            
        @self.get("/user_info")
        async def me(token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                return encoder.decode(token)
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
class BoardIn(BaseModel):
    name: str
    description: str
    owner: str

class PhaseIn(BaseModel):
    name: str
    description: str
    board: str
    
class TodoIn(BaseModel):
    name: str
    description: str
    phase: str
    
class BoardAPI(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = "/board"
        self.oauth = OAuth2PasswordBearer(tokenUrl="api/oauth2/login")
    
        @self.post("/create")
        async def create_board(board: BoardIn, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                board = await Board.prisma().create(data=board.dict())
                return board
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.get("/get")
        async def get_board(board_id: str, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                board = await Board.prisma().find_unique(where={"id": board_id})
                return board
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.get("/get_all")
        async def get_all_boards(token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                boards = await Board.prisma().find_many()
                return boards
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.post("/update")
        async def update_board(board: BoardIn, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                board = await Board.prisma().update(data=board.dict())
                return board
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.post("/delete")
        async def delete_board(board_id: str, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                board = await Board.prisma().delete(where={"id": board_id})
                return board
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
class PhaseAPI(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = "/phase"
        self.oauth = OAuth2PasswordBearer(tokenUrl="api/oauth2/login")
        
        @self.post("/create")
        async def create_phase(phase: PhaseIn, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                phase = await Phase.prisma().create(data=phase.dict())
                return phase
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.get("/get")
        async def get_phase(phase_id: str, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                phase = await Phase.prisma().find_unique(where={"id": phase_id})
                return phase
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.get("/get_all")
        async def get_all_phases(token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                phases = await Phase.prisma().find_many()
                return phases
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.post("/update")
        async def update_phase(phase: PhaseIn, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                phase = await Phase.prisma().update(data=phase.dict())
                return phase
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.post("/delete")
        async def delete_phase(phase_id: str, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                phase = await Phase.prisma().delete(where={"id": phase_id})
                return phase
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
class TodoAPI(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = "/todo"
        self.oauth = OAuth2PasswordBearer(tokenUrl="api/oauth2/login")
        
        @self.post("/create")
        async def create_todo(todo: TodoIn, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                todo = await Todo.prisma().create(data=todo.dict())
                return todo
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.get("/get")
        async def get_todo(todo_id: str, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                todo = await Todo.prisma().find_unique(where={"id": todo_id})
                return todo
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.get("/get_all")
        async def get_all_todos(token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                todos = await Todo.prisma().find_many()
                return todos
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.post("/update")
        async def update_todo(todo: TodoIn, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                todo = await Todo.prisma().update(data=todo.dict())
                return todo
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
            
        @self.post("/delete")
        async def delete_todo(todo_id: str, token: str = Depends(self.oauth)):
            encoder = JWTEncoder(token)
            if encoder.verify(token):
                todo = await Todo.prisma().delete(where={"id": todo_id})
                return todo
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
    
class App(FastAPI):
    def __init__(self):
        super().__init__()
        self.include_router(Auth())
        self.include_router(BoardAPI())
        self.include_router(PhaseAPI())
        self.include_router(TodoAPI())
        
        @self.get("/api")
        async def root():
            return "Todo App"
        
    
app = App()