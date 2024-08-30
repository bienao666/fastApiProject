from sqlalchemy import Boolean, Column, Integer, String, DateTime, func

from database_app.database import Base


class User(Base):
    __tablename__ = "user"  # 表名

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, comment='账号邮箱')
    hashed_password = Column(String, comment='密码')
    is_active = Column(Boolean, default=True, comment='状态：0未激活，1已激活')
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    __mapper_args__ = {"order_by": ["-created_at"]}  # 排序

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, is_active={self.is_active}"
