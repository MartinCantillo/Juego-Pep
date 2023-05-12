from config.db import bd, app, ma
class Administrativo(bd.Model):
    __tablename__ ='tbl_administrativo'

    id = bd.Column(bd.Integer, primary_key = True)
    Idusuario_fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_usuario.id'))
    nombre_admin=bd.Column(bd.String(50))
    IdFacultad_fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_facultad.id'))
    idPrograma_fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_programa.id'))
    

    def __init__(self,Idusuario_fk ,nombre_admin,IdFacultad_fk,idPrograma_fk):
        self.Idusuario_fk  = Idusuario_fk 
        self.nombre_admin = nombre_admin      
        self.IdFacultad_fk = IdFacultad_fk
        self.idPrograma_fk = idPrograma_fk
    
with app.app_context():
    bd.create_all()
    
class AdministrativoSchema(ma.Schema):
    class Meta:
        fields = ('id','Idusuario_fk','nombre_admin','IdFacultad_fk','idPrograma_fk')