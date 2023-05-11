from config.db import bd, app, ma

class Users(bd.Model):
    __tablename__ ='tbl_programa'

    id = bd.Column(bd.Integer, primary_key = True)
    nombrepro = bd.Column(bd.String(50))
    idfacultad_fk=bd.Column(bd.Integer,bd.ForeignKey('tbl_facultad.id'))
   
    def __init__(self, id, nombrepro,idfacultad_fk):
        self.id = id
        self.nombre_fa = nombrepro
        self.idfacultad_fk = idfacultad_fk
    
with app.app_context():
    bd.create_all()
    
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','nombrepro','idfacultad_fk')