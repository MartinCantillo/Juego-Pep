from config.db import bd, app, ma

class Estudiante(bd.Model):
    __tablename__ ='tbl_estudiante'

    id = bd.Column(bd.Integer, primary_key = True)
    idusuario_fk=bd.Column(bd.Integer,bd.ForeignKey('tbl_usuario.id')) 
    nombre_estud = bd.Column(bd.String(50))
    idfacultad_fk=bd.Column(bd.Integer,bd.ForeignKey('tbl_facultad.id'))
    idprograma_fk=bd.Column(bd.Integer,bd.ForeignKey('tbl_programa.id'))

    def __init__(self, idusuario_fk, nombre_estud,idfacultad_fk,idprograma_fk):
        self.idusuario_fk = idusuario_fk
        self.nombre_estud = nombre_estud
        self.idfacultad_fk = idfacultad_fk
        self.idprograma_fk = idprograma_fk
    
with app.app_context():
    bd.create_all()
    
class EstudianteSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_estud','idsuario_fk','idfacultad_fk','idprograma_fk')