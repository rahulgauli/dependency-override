from fastapi import FastAPI, Depends
from settings.config import APISettings, init_settings

app = FastAPI()


@app.get("/")
def test(s = Depends(init_settings)):
    return{"msg":s.dict()}

@app.get("/hello")
def hello(s = Depends(init_settings)):
    print(s)
    return{"msg":"rhansa"}
