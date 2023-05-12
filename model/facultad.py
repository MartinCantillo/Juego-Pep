from config.db import bd, app, ma

class Facultad(bd.Model):
    __tablename__ ='tbl_facultad'

    id = bd.Column(bd.Integer, primary_key = True)
    nombre_fa = bd.Column(bd.String(50))
   
    def __init__(self,nombre_fa):
        self.nombre_fa = nombre_fa
    
with app.app_context():
    bd.create_all()
    
class FacultadSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_fa')