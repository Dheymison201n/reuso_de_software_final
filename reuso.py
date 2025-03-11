from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicialização do aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definição do modelo Curso
class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    duracao = db.Column(db.Integer, nullable=False)  # Duração em semestres
    modalidade = db.Column(db.String(50), nullable=False)  # Presencial ou EAD

# Criando o banco de dados e tabelas
with app.app_context():
    db.create_all()

# Rota para listar todos os cursos
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    cursos = Curso.query.all()
    return jsonify([{
        'id': curso.id,
        'nome': curso.nome,
        'descricao': curso.descricao,
        'duracao': curso.duracao,
        'modalidade': curso.modalidade
    } for curso in cursos])

# Rota para obter um curso específico pelo ID
@app.route('/cursos/<int:curso_id>', methods=['GET'])
def obter_curso(curso_id):
    curso = Curso.query.get(curso_id)
    if curso:
        return jsonify({
            'id': curso.id,
            'nome': curso.nome,
            'descricao': curso.descricao,
            'duracao': curso.duracao,
            'modalidade': curso.modalidade
        })
    return jsonify({'erro': 'Curso não encontrado'}), 404

# Rota para adicionar um novo curso
@app.route('/cursos', methods=['POST'])
def adicionar_curso():
    dados = request.get_json()
    novo_curso = Curso(
        nome=dados['nome'],
        descricao=dados['descricao'],
        duracao=dados['duracao'],
        modalidade=dados['modalidade']
    )
    db.session.add(novo_curso)
    db.session.commit()
    return jsonify({'mensagem': 'Curso adicionado com sucesso!'}), 201

# Rota para atualizar um curso existente
@app.route('/cursos/<int:curso_id>', methods=['PUT'])
def atualizar_curso(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'erro': 'Curso não encontrado'}), 404
    
    dados = request.get_json()
    curso.nome = dados.get('nome', curso.nome)
    curso.descricao = dados.get('descricao', curso.descricao)
    curso.duracao = dados.get('duracao', curso.duracao)
    curso.modalidade = dados.get('modalidade', curso.modalidade)
    
    db.session.commit()
    return jsonify({'mensagem': 'Curso atualizado com sucesso!'})

# Rota para remover um curso pelo ID
@app.route('/cursos/<int:curso_id>', methods=['DELETE'])
def remover_curso(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'erro': 'Curso não encontrado'}), 404
    
    db.session.delete(curso)
    db.session.commit()
    return jsonify({'mensagem': 'Curso removido com sucesso!'})

# Executando a aplicação
if __name__ == '__main__':
    app.run(debug=True)
