from config.db import bd, app, ma

class Pregunta(bd.Model):
    __tablename__ ='tbl_pregunta'

    id = bd.Column(bd.Integer, primary_key = True)
    NomCorto=bd.Column(bd.String(50))
    Idtematica_FK = bd.Column(bd.Integer,bd.ForeignKey('tbl_tematica.id'))
    enunciado=bd.Column(bd.String(100))
    puntos=bd.Column(bd.Integer)

    def __init__(self,NomCorto,Idtematica_FK,enunciado,puntos):
        self.NomCorto = NomCorto
        self.Idtematica_FK =Idtematica_FK     
        self.enunciado= enunciado
        self.puntos=puntos
    
with app.app_context():
    bd.create_all()
    
class PreguntaSchema(ma.Schema):
    class Meta:
        fields = ('id','NomCorto','Idtematica_FK','enunciado','puntos')