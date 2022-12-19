from fastapi import FastAPI
from resources import AuthResourse

class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Base Template"
        self.description = "This is a boilerplate for a FastAPI project."
        self.version = "0.1.0"
        
        @self.get("/api")
        def api():
            return self.title

        self.include_router(AuthResourse(), prefix="/api", tags=["auth"])
        

app = App()