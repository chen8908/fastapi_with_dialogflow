import uvicorn
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class qaInfo(BaseModel):
    answers: str


@app.get('/question/{question}')
async def result(question: str, query_string: Optional[str]=None):
    return {'question': question, 'query_string': query_string}

@app.post('/question/{question}')
async def result(question: str, qaInfo: qaInfo):
    return {'question': question, 'qaInfo': qaInfo}


class qamaker(str, Enum):
    locations = "地點"
    opentime = "營業時間"

@app.get('/enum')
async def result(qa: qamaker):
    if qa == qamaker.locations:
        return {'回答': '我們的門市地點為XXXX'}
    if qa == qamaker.opentime:
        return {'回答': '營業時間為 ....'}
    return {'qusetion': 'unknown'}

#啟動命令: uvicorn hello_world:app --reload

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)





