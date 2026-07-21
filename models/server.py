class Server():
    def __init__(self,name,ip,user,port):
        self.name=name
        self.ip=ip
        self.user=user
        self.port=port
    def to_dict(self):
        return {"name":self.name,"ip":self.ip,"user":self.user,"port":self.port}


