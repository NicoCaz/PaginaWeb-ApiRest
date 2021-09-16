from flask import Flask,jsonify
from flask_cors import CORS
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey, MetaData
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_marshmallow import Marshmallow


#########################################################
#
#                   Aca empieza model.py   
#
#########################################################

db_url='localhost:5432'
db_name='user-db'
db_user='postgres'
db_password='AGJKSDNIKGjnlJBJBLJNFPA'

engine=create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Base=declarative_base()
metadata_obj = MetaData()
app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

class Usuarios(Base):
    __tablename__='usuarios'

    id = Column(Integer, primary_key=True)
    nombre=Column(String, nullable=False)
    categorias=relationship('categorias',cascade='all,delete-orphan',backref="usuarios")
class Categorias(Base):
    __tablename__='categorias'
    
    id = Column(Integer, primary_key=True)
    id_usuario=Column(Integer,ForeignKey('usuario.id'))
    id_madre=Column(Integer,ForeignKey('categorias.id'))
    nombre=Column(String)
    orden=Column(Integer)
    hijo=relationship('Categorias',cascade='all,delete-orphan')
    
"""
class CategoriasSchema(ma.Schema):
    class Meta:
        model = Categorias
        load_instance = True
    
    id = ma.auto_field()
    id_madre = ma.auto_field()
    nombre = ma.auto_field()
    orden = ma.auto_field()
    id_usuario=ma.auto_field()
    hijos = ma.auto_field()


class UsuariosSchema(ma.Schema):
    class Meta:
        model = Usuarios
        load_instance = True
    id = ma.auto_field()
    nombre= ma.auto_field()
    categorias=ma.auto_field()

    """

Usuarios.create(engine,cheackfirst=True)
Categorias.create(engine,cheackfirst=True)
#Base.metadata.create_all(engine)
#Session=sessionmaker()
#Session.configure(bind=engine)


#########################################################
#
#                   Aca termina model.py   
#
#########################################################


"""

#################################################### AGREGA
categorias_post_args = reqparse.RequestParser()
categorias_post_args.add_argument('nombre', type=str, help="Nombre de la categoria requerido", required=True)
categorias_post_args.add_argument('id_madre', type=int)
#################################################### ELIMINA
categorias_delete_args = reqparse.RequestParser()
categorias_delete_args.add_argument('id', type=int, help="id de la categoria requerido", required=True)
#################################################### MODIFICA
categorias_put_args = reqparse.RequestParser()
categorias_put_args.add_argument('id', type=int)
categorias_put_args.add_argument('nombre', type=str)
categorias_put_args.add_argument('id1', type=int)
categorias_put_args.add_argument('id2', type=int)
#####################################################

"""

@app.route('/usuario/<user_id>')
def post(self,user_id):
   session=Session()
   usuarios=session.query(Usuarios).all()
   schema=UsuariosSchema(many=True)
   datos=schema.dump(usuarios)
   session.close()
   return jsonify(datos.data)




if __name__ == "__main__":
    app.run(debug=True)