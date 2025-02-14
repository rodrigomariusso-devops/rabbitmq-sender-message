import pika

# Configurações de conexão
usuario = ''
senha = ''
host = ''
porta = 5672

# Estabelece uma conexão com o RabbitMQ usando as credenciais e host fornecidos
credentials = pika.PlainCredentials(usuario, senha)
connection_params = pika.ConnectionParameters(
    host=host,
    port=porta,
    credentials=credentials,
    heartbeat=600  # Tempo em segundos para o heartbeat
)

try:
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declara a fila
    channel.queue_declare(queue='teste_replica')

    # Mensagem a ser publicada
    mensagem = 'Olá, RabbitMQ!'

    # Publica a mensagem na fila
    channel.basic_publish(exchange='',
                          routing_key='teste_replica',
                          body=mensagem)

    print(f" [x] Mensagem enviada: '{mensagem}'")

except pika.exceptions.AMQPConnectionError as e:
    print(f"Erro de conexão: {e}")

finally:
    # Fecha a conexão
    if connection and connection.is_open:
        connection.close()
