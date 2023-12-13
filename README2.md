 ## 1. Connecting to database
    - main.py

 ## 2. generating model from database
    - sqlacodegen --outfile models.py postgresql://postgres:jmrozek@localhost:5432/Project1

 ## 3. generating graph from database
    - graph.py


## sql->dbml
npm install -g @dbml/cli


## dbml->graph not working
npm install -g @softwaretechnik/dbml-renderer

## dbml -> graph but svg
pip install git+https://github.com/aviallon/dbml2dot.git
