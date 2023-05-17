from config.db import bd, app, ma

class Usuario(bd.Model):
    __tablename__ ='tbl_usuario'

    id = bd.Column(bd.Integer, primary_key = True)
    nom_usuario=bd.Column(bd.String(50))
    IdCategoria_Fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_categoria.id'))
    estado=bd.Column(bd.String(1))
    clave_usuario=bd.Column(bd.String(30))
    avatar_rut=bd.Column(bd.String(50))
    emailusuario_pk=bd.Column(bd.String(50))

    def __init__(self,nom_usuario,IdCategoria_Fk,estado,clave_usuario,avatar_rut,emailusuario_pk):
        self.nom_usuario = nom_usuario
        self.IdCategoria_Fk =IdCategoria_Fk      
        self.estado = estado
        self.clave_usuario=clave_usuario
        self.avatar_rut=avatar_rut
        self.emailusuario_pk=emailusuario_pk
    
with app.app_context():
    bd.create_all()
    
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id','nom_usuario','IdCategoria_Fk','estado','clave_usuario','avatar_rut','emailusuario_pk')