from config.db import bd, app, ma

class Categoria(bd.Model):
    __tablename__ ='tbl_categoria'

    id = bd.Column(bd.Integer, primary_key = True)
    ctg_name = bd.Column(bd.String(50))
   
    def __init__(self,ctg_name):
        self.ctg_name = ctg_name
    
with app.app_context():
    bd.create_all()
    
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id','ctg_name')