from config.db import bd, app, ma

class Inftema(bd.Model):
    __tablename__ ='tbl_inftema'

    id = bd.Column(bd.Integer, primary_key = True)
    Titulo_inftem = bd.Column(bd.String(50))
    Det_inftema =bd.Column(bd.String(50))
    Idtematica_Fk= bd.Column(bd.Integer,bd.ForeignKey('tbl_tematica.id'))
    IdNivel_fk = bd.Column(bd.Integer,bd.ForeignKey('tbl_nivel.id'))
    
   

    def __init__(self, id,Titulo_inftem,Det_inftema, IdNivel_fk ,Idtematica_Fk):
        self.id = id
        self.Titulo_inftem =Titulo_inftem
        self.IdNivel_fk =IdNivel_fk     
        self.Det_inftema= Det_inftema
        self.Idtematica_Fk=Idtematica_Fk
    
with app.app_context():
    bd.create_all()
    
class InftemaSchema(ma.Schema):
    class Meta:
        fields = ('id','Titulo_inftem','IdNivel_fk','Det_inftema','Idtematica_Fk')