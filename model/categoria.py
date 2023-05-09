from config.db import bd, app, ma

class Users(bd.Model):
    __tablename__ ='tbl_categoria'

    id = bd.Column(bd.Integer, primary_key = True)
    ctg_name = bd.Column(bd.String(50))
   
    def __init__(self, id, ctg_name):
        self.id = id
        self.ctg_name = ctg_name
    
with app.app_context():
    bd.create_all()
    
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','ctg_name')