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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')