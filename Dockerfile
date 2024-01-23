# Dockerfile
FROM ubuntu:20.04

# Set the DEBIAN_FRONTEND to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY . /app

# Install pandoc and texlive
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl wget && \
    curl -LO https://github.com/jgm/pandoc/releases/download/3.1.11/pandoc-3.1.11-1-amd64.deb && \
    dpkg -i pandoc-3.1.11-1-amd64.deb && \
    apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra librsvg2-bin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm pandoc-3.1.11-1-amd64.deb

# Install PostgreSQL 16 repository
RUN apt-get update && \
    apt install lsb-core -y && \
    sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get -y install postgresql
    # apt-get install -y postgresql

# Install Node.js and npm
RUN apt-get install -y nodejs npm

# Install @dbml/cli globally using npm
RUN npm install -g @dbml/cli

RUN npm cache clean -f && \
    npm install -g n && \
    n stable
    
# Install dependencies for psycopg2
RUN apt-get install -y libpq-dev

RUN pip install -r requirements.txt

EXPOSE 80

# ENV NAME World

CMD ["python3", "generation.py"]
