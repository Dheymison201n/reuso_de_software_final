-- Criar a tabela cursos
CREATE TABLE IF NOT EXISTS curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    duracao INTEGER NOT NULL,
    modalidade TEXT NOT NULL
);

-- Inserir cursos de exemplo
INSERT INTO curso (nome, descricao, duracao, modalidade) VALUES
('Redes de Computadores', 'Curso voltado para infraestrutura e segurança de redes.', 8, 'Presencial'),
('Sistemas de Informação', 'Curso voltado para gestão e desenvolvimento de software.', 8, 'Presencial'),
('Design Digital', 'Curso que integra design gráfico e tecnologias digitais.', 8, 'Presencial'),
('Engenharia de Computação', 'Curso focado em hardware e software.', 10, 'Presencial'),
('Engenharia de Software', 'Curso especializado no desenvolvimento de software.', 8, 'Presencial'),
('Sistemas e Mídias Digitais', 'Curso voltado para multimídia e tecnologia digital.', 8, 'EAD'),
('Ciência da Computação', 'Curso que abrange teoria da computação e programação.', 8, 'Presencial');
