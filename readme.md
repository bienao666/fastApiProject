## 启动应用

    在命令行输入

    uvicorn main:app --reload

    默认端口为8000，运行后可以通过浏览器访问

    API访问端口： http://127.0.0.1:8000

    API文档和交互调试： http://127.0.0.1:8000/docs

    API可选文档：http://127.0.0.1:8000/redoc

    API原始数据：http://127.0.0.1:8000/openapi.json


## 导出依赖，删除里面的pip

    pip list --format=freeze >requirement.txt

## 安装依赖

    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

## 镜像源列表

    阿里云：https://mirrors.aliyun.com/pypi/simple/
    腾讯云:：https://mirrors.cloud.tencent.com/pypi/simple/
    清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
    华为云:：https://mirrors.huaweicloud.com/repository/pypi/simple/
    网易:：https://mirrors.163.com/pypi/simple/
