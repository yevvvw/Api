import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from public.users import U_R, create_tables

create_tables()

app = FastAPI()

app.include_router(U_R)

@app.get('/', response_class = HTMLResponse)
async def index():
    return "<b> Привет, пользователь! </b>"