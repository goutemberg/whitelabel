FROM python:3.11.3-alpine3.18
LABEL mantainer="goutemberg@icloud.com"

# Essa variável de ambiente é usada para controlar se o Python deve 
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em 
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

# Copia a pasta "whitelabel" e "scripts" para dentro do container.
COPY ./ /projeto_whitelabel
COPY scripts /scripts
COPY requirements.txt /app/requirements.txt

# Entra na pasta djangoapp no container DFDFF
WORKDIR /projeto_whitelabel

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
EXPOSE 8000

# RUN executa comandos em um shell dentro do container para construir a imagem. 
# O resultado da execução do comando é armazenado no sistema de arquivos da 
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# imagem e torná-la mais eficiente.
RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /app/requirements.txt && \    
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  mkdir -p /projeto_whitelabel/staticfiles && \
  mkdir -p /projeto_whitelabel/static && \
  mkdir -p /projeto_whitelabel/home/static && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chown -R duser:duser /projeto_whitelabel/staticfiles && \
  chown -R duser:duser /projeto_whitelabel/static && \
  chown -R duser:duser /projeto_whitelabel/home/static && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R 755 /projeto_whitelabel/staticfiles && \
  chmod -R +x /scripts && \
  chmod -R 755 /projeto_whitelabel/static && \
  chmod -R 755 /projeto_whitelabel/home/static && \ 
# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
ENTRYPOINT ["/bin/sh", "/scripts/commands.sh"]


