from fastapi import FastAPI
from .params import PostTradParams

app = FastAPI()

@app.post('/trad')
def postTrad(params: PostTradParams):
    return {
        'word': params.word,
        'dictionnary': params.dictionnary,
        'trad': "... --- ..."
    }

@app.get("/")
def index():
    return {'msg': 'Hello World !'}

@app.get("/trad/{word}")
def getTrad(word: str):
    return {
        "word": word
    }
