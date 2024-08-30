from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from auth_app import auth_app
from service_app import service_app

app = FastAPI(
    title='项目名称',
    description='描述',
    version='1.0.0'
)

# 路由
app.include_router(auth_app, prefix='/auth', tags=["认证授权"])
app.include_router(service_app, prefix='/server', tags=["业务功能"])

# 前端静态资源
app.mount('/static', StaticFiles(directory='./static'), name='static')

# 启动
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
