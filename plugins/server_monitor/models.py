from sqlalchemy import Integer, String, Column

from settings import Base


class Server(Base):
    __tablename__ = "tb_servers"

    id = Column(Integer, primary_key=True)
    server_host = Column(String(15), nullable=False, comment="服务器地址")
    server_port = Column(Integer, default=22, comment="服务器端口")
    server_user = Column(Integer, default='root', comment="服务器用户")
    remark = Column(String(128), comment="备注")

    def __repr__(self):
        return "<Server(host='%s', port='%s', user='%s')>" % (
            self.server_host, self.server_port, self.server_user)
