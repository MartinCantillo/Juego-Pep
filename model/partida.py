from config.db import bd, app, ma

class Partida(bd.Model):
    __tablename__ ='tbl_partida'

    id = bd.Column(bd.Integer, primary_key = True)
    Idusuario_fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_usuario.id'))
    IdNivel_fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_nivel.id'))
    Idpregunta_fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_pregunta.id'))
    Ptos_Resp=bd.Column(bd.Integer)

    def __init__(self,Idusuario_fk,IdNivel_fk ,Idpregunta_fk,Ptos_Resp):
        self.Idusuario_fk =Idusuario_fk
        self.IdNivel_fk =IdNivel_fk     
        self.Idpregunta_fk= Idpregunta_fk
        self.Ptos_Resp=Ptos_Resp
    
with app.app_context():
    bd.create_all()
    
class PartidaSchema(ma.Schema):
    class Meta:
        fields = ('id','Idusuario_fk','IdNivel_fk','Idpregunta_fk','Ptos_Resp')
