import uvicorn
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title = "FastAPI with Dialogflow for AI customer service (Beta)",
    description = "FastAPI 串接 Dialogflow 智能客服應用",
    version = "1.0.0",
    docs_url = "/",
    redoc_url = "/redocs",
    openapi_tags = [{
            'name': '問答獲取',
            'description': '取得用戶詢問接口'}],
            
)

class qaInfo(BaseModel):
    answers: str


@app.get('/question/{question}', tags= ['問答獲取'])
async def result_with_query(question: str, query_string: Optional[str]=None):
    """
    Result With Query 路徑請求參數
    | question: 問題
    | query_string: 查詢參數(選填)
    | return: 返回值
    """
    return {'question': question, 'query_string': query_string}

@app.post('/question/{question}', tags= ['問答獲取'])
async def result_with_qainfo(question: str, qaInfo: qaInfo):
    """
    Result With QaInfo 路徑請求響應模型
    | question: 問題
    | query_string: 響應模型
    | return: 返回值
    """
    return {'question': question, 'qaInfo': qaInfo}


class qamaker(str, Enum):
    locations = "地點"
    opentime = "營業時間"

@app.get('/enum', tags= ['問答獲取'])
async def result_with_enum(qa: qamaker):
    """
    Result With Enum 路徑請求列舉
    | qa: 問題
    | return: 返回值
    """
    if qa == qamaker.locations:
        return {'回答': '我們的門市地點為XXXX'}
    if qa == qamaker.opentime:
        return {'回答': '營業時間為 ....'}
    return {'qusetion': 'unknown'}

#啟動命令: uvicorn hello_world:app --reload

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)





