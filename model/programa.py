from config.db import bd, app, ma

class Programa(bd.Model):
    __tablename__ ='tbl_programa'

    id = bd.Column(bd.Integer, primary_key = True)
    nombrepro = bd.Column(bd.String(50))
    idfacultad_fk=bd.Column(bd.Integer,bd.ForeignKey('tbl_facultad.id'))
   
    def __init__(self,nombrepro,idfacultad_fk):
        self.nombrepro = nombrepro
        self.idfacultad_fk = idfacultad_fk
    
with app.app_context():
    bd.create_all()
    
class ProgramaSchema(ma.Schema):
    class Meta:
        fields = ('id','nombrepro','idfacultad_fk')