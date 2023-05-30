#importo las dependencias de trabajo
from flask import Flask, request, jsonify, json, render_template, redirect, session,url_for
#importo las configuraciones de la bd
from config.db import app, bd
from sqlalchemy.orm import aliased
import random



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
preguntas_schema =  PreguntaSchema(many=True)

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

respuestas_schema =  RespuestaSchema(many=True)

id_pregunta_act =1


#RUTAS DIRECTAS
@app.route("/", methods=['GET'])
def index():
    nombre= "Login"
    return render_template('Login.html')

@app.route("/admin", methods=['GET'])
def admin():
    nombre= "Admin"
    return render_template('admin.html')

@app.route("/inftema", methods=['GET'])
def inftema():
    nombre= "Inftema"
    return render_template('inftema.html')

@app.route("/creadospormi", methods=['GET'])
def creadospormi():
    nombre= "Creados por mí"
    return render_template('creadospormi.html')

@app.route("/crearpreguntas", methods=['GET'])
def crearpreguntas():
    nombre= "Crear preguntas"
    return render_template('crearpreguntas.html')

@app.route("/creartematicas", methods=['GET'])
def creartematicas():
    nombre= "Crear tematicas"
    return render_template('creartematicas.html')

@app.route("/Registro", methods=['GET'])
def registrar():
    nombre= "registrar"
    return  render_template('Registro.html')

@app.route("/Ccontraseña", methods=['GET'])
def Contraseña():
    nombre= "contraseña"
    return  render_template('Ccontraseña.html')

@app.route("/pregunta", methods=['GET'])
def pregunta():
    return  render_template('index.html')

@app.route("/frquestions", methods=['GET'])
def frquestions():
    return render_template('frquestions.html')

@app.route("/jugando", methods=['GET'])
def jugando():
    return render_template('jugando.html')

@app.route("/layout", methods=['GET'])
def layout():
    return render_template('layout.html')

@app.route("/avatar", methods=['GET'])
def avatar():
    return render_template('avatar.html')

@app.route("/menuPrincipal", methods=['GET'])
def menuPrincipal():
    return render_template('menuPrincipal.html')

@app.route("/nivel", methods=['GET'])
def nivel():
    nombre= "Nivel"
    return render_template('nivel.html')


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
    avatar_rut = request.json['avatar_rut']
    emailusuario_pk = request.json['emailusuario_pk']
    newusuario = Usuario(nom_usuario, IdCategoria_Fk, estado, clave_usuario, avatar_rut,emailusuario_pk)
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
    try:
        Titulo_inftem = request.json['Titulo_inftem']
        Det_inftema = request.json['Det_inftema']
        Idtematica_Fk = request.json['Idtematica_Fk']
        IdNivel_fk = request.json['IdNivel_fk']
        newinftema = Inftema(Titulo_inftem, Det_inftema, Idtematica_Fk, IdNivel_fk)
        bd.session.add(newinftema)
        bd.session.commit()
        return "guardado"
    except Exception as e:
        return str(e)

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

#ACTUALIZAR

@app.route("/actutematica", methods=['POST'])
def actutematica():    
    id = request.json['id'] 
    nombre_tematica = request.json['nombre_tematica'] 
    tope_tem = request.json['tope_tem']
    tematica = Tematica.query.get(id)  
    tematica.nombre_tematica = nombre_tematica
    tematica.tope_tem = tope_tem
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actunivel", methods=['POST'])
def actunivel():    
    id = request.json['id'] 
    nombre_nv = request.json['nombre_nv'] 
    nivel = Nivel.query.get(id)  
    nivel.nombre_nv = nombre_nv
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actufacultad", methods=['POST'])
def actufacultad():    
    id = request.json['id'] 
    nombre_fa = request.json['nombre_fa'] 
    facultad = Facultad.query.get(id)  
    facultad.nombre_fa = nombre_fa
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actucategoria", methods=['POST'])
def actucategoria():    
    id = request.json['id'] 
    ctg_name = request.json['ctg_name'] 
    categoria = Categoria.query.get(id)  
    categoria.ctg_name = ctg_name
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actuusuario", methods=['POST'])
def actuusuario():    
    id = request.json['id'] 
    nom_usuario = request.json['nom_usuario']
    IdCategoria_Fk = request.json['IdCategoria_Fk']
    estado = request.json['estado']
    clave_usuario = request.json['clave_usuario']
    avatar_rut = request.json['avatar_rut']
    emailusuario_pk = request.json['emailusuario_pk']
    usuario = Usuario.query.get(id)  
    usuario.nom_usuario = nom_usuario
    usuario.IdCategoria_Fk = IdCategoria_Fk
    usuario.estado = estado
    usuario.clave_usuario = clave_usuario
    usuario.avatar_rut = avatar_rut
    usuario.emailusuario_pk = emailusuario_pk
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actutablerouser", methods=['POST'])
def actutablerouser():    
    id = request.json['id'] 
    IdUsuario_Fk = request.json['IdUsuario_Fk']
    PuntosTot = request.json['PuntosTot']
    Nivel_Act = request.json['Nivel_Act']
    tablerouser = Tablerouser.query.get(id)  
    tablerouser.IdUsuario_Fk = IdUsuario_Fk
    tablerouser.PuntosTot = PuntosTot
    tablerouser.Nivel_Act = Nivel_Act
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actupregunta", methods=['POST'])
def actupregunta():    
    id = request.json['id'] 
    NomCorto = request.json['NomCorto']
    Idtematica_FK = request.json['Idtematica_FK']
    enunciado = request.json['enunciado']
    puntos = request.json['puntos']
    pregunta = Pregunta.query.get(id)  
    pregunta.NomCorto = NomCorto
    pregunta.PuntosTot = Idtematica_FK
    pregunta.enunciado = enunciado
    pregunta.puntos = puntos
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/acturespuesta", methods=['POST'])
def acturespuesta():    
    id = request.json['id'] 
    IDpregunta_FK = request.json['IDpregunta_FK']
    EnuncRespu = request.json['EnuncRespu']
    PuntosRespu = request.json['PuntosRespu']
    respuesta = Respuesta.query.get(id)  
    respuesta.IDpregunta_FK = IDpregunta_FK
    respuesta.EnuncRespu = EnuncRespu
    respuesta.PuntosRespu = PuntosRespu
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actuprograma", methods=['POST'])
def actuprograma():    
    id = request.json['id'] 
    nombrepro = request.json['nombrepro']
    idfacultad_fk = request.json['idfacultad_fk']
    programa = Programa.query.get(id)  
    programa.nombrepro = nombrepro
    programa.idfacultad_fk = idfacultad_fk
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actuestudiante", methods=['POST'])
def actuestudiante():    
    id = request.json['id'] 
    nidusuario_fk = request.json['idusuario_fk']
    nombre_estud = request.json['nombre_estud']
    idfacultad_fk = request.json['idfacultad_fk']
    idprograma_fk = request.json['idprograma_fk']
    estudiante = Estudiante.query.get(id)  
    estudiante.nidusuario_fk = nidusuario_fk
    estudiante.nombre_estud = nombre_estud
    estudiante.idfacultad_fk = idfacultad_fk
    estudiante.idprograma_fk = idprograma_fk
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actuepartida", methods=['POST'])
def actupartida():    
    id = request.json['id'] 
    Idusuario_fk = request.json['Idusuario_fk']
    IdNivel_fk = request.json['IdNivel_fk']
    Idpregunta_fk = request.json['Idpregunta_fk']
    Ptos_Resp = request.json['Ptos_Resp']
    partida = Partida.query.get(id)  
    partida.Idusuario_fk = Idusuario_fk
    partida.IdNivel_fk = IdNivel_fk
    partida.Idpregunta_fk = Idpregunta_fk
    partida.Ptos_Resp = Ptos_Resp
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actuinftema", methods=['POST'])
def actuinftema():    
    id = request.json['id'] 
    Titulo_inftem = request.json['Titulo_inftem']
    Det_inftema = request.json['Det_inftema']
    Idtematica_Fk = request.json['Idtematica_Fk']
    IdNivel_fk = request.json['IdNivel_fk']
    inftema = Inftema.query.get(id)  
    inftema.Titulo_inftem = Titulo_inftem
    inftema.Det_inftema = Det_inftema
    inftema.Idtematica_Fk = Idtematica_Fk
    inftema.IdNivel_fk = IdNivel_fk
    bd.session.commit()     
    return "actualización exitosa"

@app.route("/actuadministrativo", methods=['POST'])
def actuadministrativo():    
    id = request.json['id'] 
    Idusuario_fk = request.json['Idusuario_fk']
    nombre_admin = request.json['nombre_admin']
    IdFacultad_fk = request.json['IdFacultad_fk']
    idPrograma_fk = request.json['idPrograma_fk']
    administrativo = Administrativo.query.get(id)  
    administrativo.Idusuario_fk = Idusuario_fk
    administrativo.nombre_admin = nombre_admin
    administrativo.IdFacultad_fk = IdFacultad_fk
    administrativo.idPrograma_fk = idPrograma_fk
    bd.session.commit()     
    return "actualización exitosa"

#ELIMINAR POR ID

@app.route("/deltemactica", methods=['POST'])
def deltemactica():    
    id = request.json['id'] 
    tematica = Tematica.query.get(id)    
    bd.session.delete(tematica)
    bd.session.commit()     
    return jsonify(tematica_schema.dump(tematica))

@app.route("/delnivel", methods=['POST'])
def delnivel():    
    id = request.json['id'] 
    nivel = Nivel.query.get(id)    
    bd.session.delete(nivel)
    bd.session.commit()     
    return jsonify(nivel_schema.dump(nivel))

@app.route("/delfacultad", methods=['POST'])
def delfacultad():    
    id = request.json['id'] 
    facultad = Facultad.query.get(id)    
    bd.session.delete(facultad)
    bd.session.commit()     
    return jsonify(facultad_schema.dump(facultad))

@app.route("/decategoria", methods=['POST'])
def delcategoria():    
    id = request.json['id'] 
    categoria = Categoria.query.get(id)    
    bd.session.delete(categoria)
    bd.session.commit()     
    return jsonify(categoria_schema.dump(categoria))

@app.route("/delusuario", methods=['POST'])
def delusuario():    
    id = request.json['id'] 
    usuario = Usuario.query.get(id)    
    bd.session.delete(usuario)
    bd.session.commit()     
    return jsonify(usuario_schema.dump(usuario))

@app.route("/deltablerouser", methods=['POST'])
def deltablerouser():    
    id = request.json['id'] 
    tablerouser = Tablerouser.query.get(id)    
    bd.session.delete(tablerouser)
    bd.session.commit()     
    return jsonify(tablerouser_schema.dump(tablerouser))

@app.route("/delpregunta", methods=['POST'])
def delpregunta():    
    id = request.json['id'] 
    pregunta = Pregunta.query.get(id)    
    bd.session.delete(pregunta)
    bd.session.commit()     
    return jsonify(pregunta_schema.dump(pregunta))

@app.route("/delrespuesta", methods=['POST'])
def delrespuesta():    
    id = request.json['id'] 
    respuesta = Respuesta.query.get(id)    
    bd.session.delete(respuesta)
    bd.session.commit()     
    return jsonify(respuesta_schema.dump(respuesta))

@app.route("/delprograma", methods=['POST'])
def delprograma():    
    id = request.json['id'] 
    programa = Programa.query.get(id)    
    bd.session.delete(programa)
    bd.session.commit()     
    return jsonify(programa_schema.dump(programa))

@app.route("/delestudiante", methods=['POST'])
def delestudiante():    
    id = request.json['id'] 
    estudiante = Estudiante.query.get(id)    
    bd.session.delete(estudiante)
    bd.session.commit()     
    return jsonify(estudiante_schema.dump(estudiante))

@app.route("/delpartida", methods=['POST'])
def delpartida():    
    id = request.json['id'] 
    partida = Partida.query.get(id)    
    bd.session.delete(partida)
    bd.session.commit()     
    return jsonify(partida_schema.dump(partida))

@app.route("/delinftema", methods=['POST'])
def delinftema():    
    id = request.json['id'] 
    inftema = Inftema.query.get(id)    
    bd.session.delete(inftema)
    bd.session.commit()     
    return jsonify(inftema_schema.dump(inftema))

@app.route("/deladministrativo", methods=['POST'])
def deladministrativo():    
    id = request.json['id'] 
    administrativo = Administrativo.query.get(id)    
    bd.session.delete(administrativo)
    bd.session.commit()     
    return jsonify(administrativo_schema.dump(administrativo))
#consultas
@app.route('/consultatematica', methods=['GET'])
def ConsultaTematica():
    results = bd.session.query(Tematica).all() 
    dato={}   
    i=0
    for tematica in results:
        i+=1	       
        dato[i] = {
        'id' :tematica.id,
        'nombre_tematica':tematica.nombre_tematica ,
        'tope_tem': tematica.tope_tem           
        }
      
    print(tematica.nombre_tematica  )  
    return jsonify(dato)

@app.route('/consultanivel', methods=['GET'])
def Consultanivel():
    results = bd.session.query(Nivel).all() 
    dato={}   
    i=0
    for nivel in results:
        i+=1	       
        dato[i] = {
        'id' :nivel.id, 
        'nombre_nv':nivel.nombre_nv          
        }
      
    print(nivel.nombre_nv )  
    return jsonify(dato)

  #Consulta para obtener las preguntas registradas
@app.route('/consultaP', methods=['POST'])
def getData():
    data = request.json
    IdtematicaFK = data.get('Idtematica_FK')
 
    results = consultar_base_de_datos(IdtematicaFK)

    for result in results:
        print(result)

    return jsonify(results)

def consultar_base_de_datos(IdtematicaFK):
   results = bd.session.query(Pregunta). \
   filter(Pregunta.Idtematica_FK== IdtematicaFK).all()
   dato={}   
   i=0
   for pregunta in results:
        i+=1	       
        dato[i] = {
        'id': pregunta.id,
        'enunciado': pregunta.enunciado,              
        }
   return dato
#Consulta para poder editar las preguntas y respuestas

@app.route('/cargardatosp', methods=['POST'])
def cargarDatos():
    data = request.json
    id = data.get('id')
    results = consultar(id)
    
    return jsonify(results)

def consultar(id):
   results = bd.session.query(Pregunta,Respuesta).join(Respuesta).filter(Pregunta.id==id).all()
   dato={}   
   i=0
   
   for pregunta, respuesta in results:
        i+=1	       
        dato[i] = {
        'id': pregunta.id,
        'enunciado': pregunta.enunciado, 
        'id' :respuesta.id ,
        'EnuncRespu': respuesta.EnuncRespu,
        'PuntosRespu': respuesta.PuntosRespu        
        }
      
   return dato

@app.route('/consultapregunta', methods=['GET'])
def ConsultaPregunta():
    results = bd.session.query(Pregunta).all() 
    dato={}   
    i=0
    for pregunta in results:
        i+=1	       
        dato[i] = {
        'id' :pregunta.id,
        'NomCorto':pregunta.NomCorto,
        'Idtematica_FK': pregunta.Idtematica_FK,
        'enunciado':  pregunta.enunciado,
        'puntos': pregunta.puntos          
        }
     
    return jsonify(dato)  

@app.route('/traerpregu', methods=['GET'])
def traerpregu():
    #registro = bd.session.query(Pregunta).all() 
    registro = bd.session.query(Pregunta).filter(Pregunta.id ==id_pregunta_act ).all()
    regi={}
    i=0
    for pregunta in registro:
        i+=1
        regi[i]={
        'id' : pregunta.id,
        'nombrecorto':pregunta.NomCorto,
        'enunciado':  pregunta.enunciado,
        'puntos': pregunta.puntos          
        }
    return jsonify(regi) 
    
@app.route('/traeresp', methods=['GET'])
def traeresp():
    #con la siguiente consulta obtenemos los 4
    #registros de respuestas, filtrados por el ID de la pregunta con que se relaciona.
    registro = bd.session.query(Respuesta).filter(Respuesta.IDpregunta_FK == 1).all() 
    regi={}
    r1="";p1=0;r2="";p2=0;r3="";p3=0;r4="";p4=0
    for respuesta in registro:
        #condicional para asignar cada respuesta a una variable.
        if respuesta.id==1:
            r1=respuesta.EnuncRespu
            p1=respuesta.PuntosRespu
        if respuesta.id==2:
            r2=respuesta.EnuncRespu
            p2=respuesta.PuntosRespu
        if respuesta.id==3:
            r3=respuesta.EnuncRespu
            p3=respuesta.PuntosRespu
        if respuesta.id==4:
            r4=respuesta.EnuncRespu
            p4=respuesta.PuntosRespu   
        regi[1]={
        'r1' : r1,
        'p1': p1,
        'r2': r2,
        'p2': p2,
        'r3': r3,
        'p3': p3,
        'r4': r4,
        'p4': p4          
        } 
        
    return jsonify(regi) 

@app.route('/ttt', methods=['GET'])
def ttt():
    registro = bd.session.query(Respuesta).filter(Respuesta.IDpregunta_FK == id_pregunta_act).all() 
    regi={}
    i=0
    for res in registro:
        i+=1
        regi[i]={
        'id' : res.id,
        'enunciado': res.EnuncRespu,
        'puntos': res.PuntosRespu          
        }
    return jsonify(regi) 

@app.route('/modifica_general', methods=['GET'])
def modifica_general():
    global id_pregunta_act
    id_pregunta_act= id_pregunta_act+1
    return("correcto")


#VALIDACION

@app.route("/valiusuarios", methods=['POST'])
def valiusuarios():
    emailusuario_pk = request.json['emailusuario_pk']
    clave_usuario = request.json['clave_usuario']
    usuario = bd.session.query(Usuario.id).filter(Usuario.emailusuario_pk == emailusuario_pk, Usuario.clave_usuario == clave_usuario).all()
    resultado = usuario_schema.dump(usuario)
    dato={}   
  
    if len(resultado)>0: 
        session['email']=emailusuario_pk
        dato[0] = {
            'StatusCode':'200',
            'payload':True,                     
        }      
        return jsonify(dato)
    else:
        return redirect('/')  
    
@app.route("/menuprincipal", methods=['GET'])
def menuprincipal():
    if 'email' in session:
        return render_template('menuPrincipal.html',usuario=session['email'])
    else:
        return redirect('/')  
    
@app.route("/menuadmin", methods=['GET'])
def menuadmin():
    if 'email' in session:
        return render_template('layout.html',usuario=session['email'])
    else:
        return redirect('/')
#elminar respuesta con filtro
@app.route("/delrespuestas", methods=['POST'])
def delrespuestas():    
    IDpre_FK = request.json['IDpregunta_FK'] 
    respuestas = Respuesta.query.filter_by(IDpregunta_FK=IDpre_FK).all()
  
    if respuestas:
        for respuesta in respuestas:
            bd.session.delete(respuesta)
        bd.session.commit()     
        return jsonify(respuestas_schema.dump(respuestas))
    else:
        return jsonify({'message': 'No se encontraron respuestas para el filtro especificado.'}), 404

@app.route("/actualizarpreg", methods=['POST'])
def Updatepregunta():    
    id = request.json['id'] 
    enunciado = request.json['enunciado']
    pregunta = Pregunta.query.get(id)  
    pregunta.enunciado = enunciado
    bd.session.commit()     
    return "actualización exitosa"

#Actualizar contraseña de usuario
@app.route("/actucontra", methods=['POST'])
def actucontra():    
    emailusuario_pk = request.json['emailusuario_pk']
    clave_usuario = request.json['clave_usuario']
    user = Usuario.query.filter_by(emailusuario_pk=emailusuario_pk).first()
    
    if user:
        user.clave_usuario = clave_usuario
        bd.session.commit()
        return "Actualización exitosa"
    else:
        return "Usuario no encontrado"
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')