from config.db import bd, app, ma

class Tematica(bd.Model):
    __tablename__ ='tbl_tematica'

    id = bd.Column(bd.Integer, primary_key = True)
    nombre_tematica=bd.Column(bd.String(30))
    tope_tem=bd.Column(bd.Integer)
    
   
    def __init__(self,nombre_tematica,tope_tem):
        self.nombre_tematica=nombre_tematica
        self.tope_tem = tope_tem
    
with app.app_context():
    bd.create_all()
    
class TematicaSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_tematica','tope_tem')