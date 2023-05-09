from config.db import bd, app, ma

class Users(bd.Model):
    __tablename__ ='tbl_pregunta'

    id = bd.Column(bd.Integer, primary_key = True)
    NomCorto=bd.Column(bd.String(50))
    Idtematica_FK = bd.Column(bd.Integer,bd.ForeignKey('tbl_tematica.id'))
    enunciado=bd.Column(bd.String(100))
    puntos=bd.Column(bd.Integer)

    def __init__(self, id, NomCorto,Idtematica_FK,enunciado,puntos):
        self.id = id
        self.NomCorto = NomCorto
        self.Idtematica_FK =Idtematica_FK     
        self.enunciado= enunciado
        self.puntos=puntos
        self.IdNiveles_Fkk=IdNiveles_Fk
    
with app.app_context():
    bd.create_all()
    
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','NomCorto','Idtematica_FK','enunciado','puntos')