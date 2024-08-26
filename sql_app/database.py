#database.py
#引入SQLAlchemy的主要组件，并初始化数据库连接
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

#数据库访问地址
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#启动引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# engine = create_engine("mysql://user:pwd@localhost/college",echo = True)

#启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#数据模型的基类
Base = declarative_base()

