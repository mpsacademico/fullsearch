# Full Search

Um sistema web em Flask para testes de buscas inteligentes com Elasticsearch!

## Ambiente de desenvolvimento (Linux)

- Python 3.5.2
- Flask 0.12.2
- Elasticsearch 6.0.0
- virtualenv

### Usando o virtualenv
1. Instala o virtualenv no Python 3
```
pip3 install virtualenv
```
2. Cria os diretórios do ambiente virtual no caminho escolhido
```
cd /path/
virtualenv flask
```
OBS: para selecionar uma versão específica de Python
```
virtualenv --python=/usr/bin/pythonX.Y <path/to/new/virtualenv/>
```
3. Ativa o ambiente virtual anteriormente criado
```
cd /path/flask
source bin/activate 
```
4. O bash é modificado conforme o ambiente ativado
```
(flask)$
```
5. Desativa o ambiente virtual
```
deactivate
```

### Usando o Flask
```
(flask)$ pip3 install flask

git clone "https://github.com/mpsacademico/fullsearch.git"

cd /path/fullsearch
FLASK_APP=main.py flask run
```

### Domínio para Testes

- https://www.encyclopedia-titanica.org/
