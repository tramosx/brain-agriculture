# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para dentro do container
COPY . /app/

# Exponha a porta em que a aplicação vai rodar
EXPOSE 5000

# Defina o comando para rodar a aplicação
CMD ["python", "app.py"]
