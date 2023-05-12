from config.db import bd, app, ma

class Nivel(bd.Model):
    __tablename__ ='tbl_nivel'

    id = bd.Column(bd.Integer, primary_key = True)
    nombre_nv=bd.Column(bd.String(10))
    
   
    def __init__(self,nombre_nv):
        self.nombre_nv = nombre_nv
    
with app.app_context():
    bd.create_all()
    
class NivelSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_nv')