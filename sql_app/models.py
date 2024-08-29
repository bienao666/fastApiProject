# models.py
# 模型（models）用于建立供SQLAlchemy模块增删改查使用的对象，继承SQLAlchemy中的数据模型基类，根据项目需求建立数据模型
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship('Item', back_populates='owner')


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # 表a_user.items等于相应的Item表
    owner = relationship("User", back_populates="items")
