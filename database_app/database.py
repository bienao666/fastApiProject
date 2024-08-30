from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库访问地址
SQLALCHEMY_DATABASE_URL = "sqlite:///./databse.sqlite3"

# 启动引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encodings='utf-8', echo=True, connect_args={"check_same_thread": False}
)

# 启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=True)

# 数据模型的基类
Base = declarative_base(bind=engine, name='Base')
