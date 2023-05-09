from config.db import bd, app, ma

class Users(bd.Model):
    __tablename__ ='tbl_categoria'

    id = bd.Column(bd.Integer, primary_key = True)
    IdUsuario_Fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_usuario.id'))
    PuntosTot = bd.Column(bd.Integer)
    Nivel_Act=bd.Column(bd.Integer)
    
   
    def __init__(self, id,IdUsuario_Fk,PuntosTot,Nivel_Act):
        self.id = id
        self.IdUsuario_Fk = IdUsuario_Fk
        self.PuntosTot=PuntosTot
        self.Nivel_Act=Nivel_Act
    
with app.app_context():
    bd.create_all()
    
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','IdUsuario_Fk','PuntosTot','Nivel_Act')