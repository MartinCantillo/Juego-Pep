from config.db import bd, app, ma

class Respuesta(bd.Model):
    __tablename__ ='tbl_respuesta'

    id = bd.Column(bd.Integer, primary_key = True)
    IDpregunta_FK= bd.Column(bd.Integer,bd.ForeignKey('tbl_pregunta.id'))
    EnuncRespu = bd.Column(bd.String(50))
    PuntosRespu = bd.Column(bd.Integer)
    
   

    def __init__(self,IDpregunta_FK,EnuncRespu, PuntosRespu):
        self.IDpregunta_FK =IDpregunta_FK
        self.EnuncRespu =EnuncRespu    
        self.PuntosRespu= PuntosRespu
    
with app.app_context():
    bd.create_all()
    
class RespuestaSchema(ma.Schema):
    class Meta:
        fields = ('id','IDpregunta_FK','EnuncRespu','PuntosRespu')