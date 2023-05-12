#importo las dependencias de trabajo
from flask import Flask, request, jsonify, json, render_template
#importo las configuraciones de la bd
from config.db import app, bd

#importamos los modelos

from model.tematica import Tematica, TematicaSchema
from model.nivel import Nivel, NivelSchema
from model.facultad import Facultad, FacultadSchema
from model.categoria import Categoria, CategoriaSchema
from model.usuario import Usuario, UsuarioSchema
from model.tablerouser import Tablerouser, TablerouserSchema
from model.pregunta import Pregunta, PreguntaSchema
from model.respuesta import Respuesta, RespuestaSchema
from model.programa import Programa, ProgramaSchema
from model.estudiante import Estudiante, EstudianteSchema
from model.partida import Partida, PartidaSchema
from model.inftema import Inftema, InftemaSchema
from model.administrativo import Administrativo, AdministrativoSchema

administrativo_schema = AdministrativoSchema()
administrativo_schema = AdministrativoSchema(many=True)

categoria_schema = CategoriaSchema()
categoria_schema = CategoriaSchema(many=True)

estudiante_schema = EstudianteSchema()
estudiante_schema= EstudianteSchema(many=True)

facultad_schema = FacultadSchema()
facultad_schema =  FacultadSchema(many=True)

inftema_schema =  InftemaSchema()
inftema_schema =  InftemaSchema(many=True)

nivel_schema =  NivelSchema()
nivel_schema =  NivelSchema(many=True)

partida_schema =  PartidaSchema()
partida_schema =  PartidaSchema(many=True)

pregunta_schema =  PreguntaSchema()
pregunta_schema =  PreguntaSchema(many=True)

programa_schema =  ProgramaSchema()
programa_schema =  ProgramaSchema(many=True)

respuesta_schema =  RespuestaSchema()
respuesta_schema =  RespuestaSchema(many=True)

tablerouser_schema =  TablerouserSchema()
tablerouser_schema =  TablerouserSchema(many=True)

tematica_schema =  TematicaSchema()
tematica_schema =  TematicaSchema(many=True)

usuario_schema =  UsuarioSchema ()
usuario_schema =  UsuarioSchema (many=True)



@app.route("/", methods=['GET'])
def index():
    nombre= "Loggin"
    return render_template('Login.html')

#AGREGAR
@app.route("/savetematica", methods=['POST'])
def savetematica():
    nombre_tematica = request.json['nombre_tematica']
    tope_tem = request.json['tope_tem']
    newtematica = Tematica(nombre_tematica, tope_tem)
    bd.session.add(newtematica)
    bd.session.commit()
    return "guardado"

@app.route("/savenivel", methods=['POST'])
def savenivel():
    nombre_nv = request.json['nombre_nv']
    newnivel = Nivel(nombre_nv)
    bd.session.add(newnivel)
    bd.session.commit()
    return "guardado"

@app.route("/savefacultad", methods=['POST'])
def savefacultad():
    nombre_fa = request.json['nombre_fa']
    newfacultad = Facultad(nombre_fa)
    bd.session.add(newfacultad)
    bd.session.commit()
    return "guardado"

@app.route("/savecategoria", methods=['POST'])
def savecategoria():
    ctg_name = request.json['ctg_name']
    newcategoria = Categoria(ctg_name)
    bd.session.add(newcategoria)
    bd.session.commit()
    return "guardado"

@app.route("/saveusuario", methods=['POST'])
def saveusuario():
    nom_usuario = request.json['nom_usuario']
    IdCategoria_Fk = request.json['IdCategoria_Fk']
    estado = request.json['estado']
    clave_usuario = request.json['clave_usuario']
    emailusuario_pk = request.json['emailusuario_pk']
    newusuario = Usuario(nom_usuario, IdCategoria_Fk, estado, clave_usuario, emailusuario_pk)
    bd.session.add(newusuario)
    bd.session.commit()
    return "guardado"

@app.route("/savetablerouser", methods=['POST'])
def savetablerouser():
    IdUsuario_Fk = request.json['IdUsuario_Fk']
    PuntosTot = request.json['PuntosTot']
    Nivel_Act = request.json['Nivel_Act']
    newtablerouser = Tablerouser(IdUsuario_Fk, PuntosTot, Nivel_Act)
    bd.session.add(newtablerouser)
    bd.session.commit()
    return "guardado"

@app.route("/savepregunta", methods=['POST'])
def savepregunta():
    NomCorto = request.json['NomCorto']
    Idtematica_FK = request.json['Idtematica_FK']
    enunciado = request.json['enunciado']
    puntos = request.json['puntos']
    newpregunta = Pregunta(NomCorto, Idtematica_FK, enunciado, puntos)
    bd.session.add(newpregunta)
    bd.session.commit()
    return "guardado"

@app.route("/saverespuesta", methods=['POST'])
def saverespuesta():
    IDpregunta_FK = request.json['IDpregunta_FK']
    EnuncRespu = request.json['EnuncRespu']
    PuntosRespu = request.json['PuntosRespu']
    newrespuesta = Respuesta(IDpregunta_FK, EnuncRespu, PuntosRespu)
    bd.session.add(newrespuesta)
    bd.session.commit()
    return "guardado"

@app.route("/saveprograma", methods=['POST'])
def saveprograma():
    nombrepro = request.json['nombrepro']
    idfacultad_fk = request.json['idfacultad_fk']
    newprograma = Programa(nombrepro, idfacultad_fk)
    bd.session.add(newprograma)
    bd.session.commit()
    return "guardado"

@app.route("/saveestudiante", methods=['POST'])
def saveestudiante():
    idusuario_fk = request.json['idusuario_fk']
    nombre_estud = request.json['nombre_estud']
    idfacultad_fk = request.json['idfacultad_fk']
    idprograma_fk = request.json['idprograma_fk']
    newestudiante = Estudiante(idusuario_fk, nombre_estud, idfacultad_fk, idprograma_fk)
    bd.session.add(newestudiante)
    bd.session.commit()
    return "guardado"

@app.route("/savepartida", methods=['POST'])
def savepartida():
    Idusuario_fk = request.json['Idusuario_fk']
    IdNivel_fk = request.json['IdNivel_fk']
    Idpregunta_fk = request.json['Idpregunta_fk']
    Ptos_Resp = request.json['Ptos_Resp']
    newpartida = Partida(Idusuario_fk, IdNivel_fk, Idpregunta_fk, Ptos_Resp)
    bd.session.add(newpartida)
    bd.session.commit()
    return "guardado"

@app.route("/saveinftema", methods=['POST'])
def saveinftema():
    Titulo_inftem = request.json['Titulo_inftem']
    Det_inftema = request.json['Det_inftema']
    Idtematica_Fk = request.json['Idtematica_Fk']
    IdNivel_fk = request.json['IdNivel_fk']
    newinftema = Inftema(Titulo_inftem, Det_inftema, Idtematica_Fk, IdNivel_fk)
    bd.session.add(newinftema)
    bd.session.commit()
    return "guardado"

@app.route("/saveadministrativo", methods=['POST'])
def saveadministrativo():
    Idusuario_fk = request.json['Idusuario_fk']
    nombre_admin = request.json['nombre_admin']
    IdFacultad_fk = request.json['IdFacultad_fk']
    idPrograma_fk = request.json['idPrograma_fk']
    newadministrativo = Administrativo(Idusuario_fk, nombre_admin, IdFacultad_fk, idPrograma_fk)
    bd.session.add(newadministrativo)
    bd.session.commit()
    return "guardado"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')