FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Add supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5000 8501

CMD ["/usr/bin/supervisord"]
