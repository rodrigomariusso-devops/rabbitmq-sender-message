# rabbitmq-sender-message

## Descrição
Este projeto é um script Python para enviar mensagens a uma fila RabbitMQ específica, permitindo testar a comunicação e a entrega de mensagens na fila.

## Como usar

### 1. Clone o repositório:
```bash
git clone https://github.com/rodrigomariusso-devops/rabbitmq-sender-message.git
cd rabbitmq-sender-message
```

### 2. Instale as dependências
```bash
pip install pika
```

### 3. Configure as credenciais do RabbitMQ
Edite o arquivo `app.py` e altere as credenciais conforme necessário:
```python
usuario = 'seu_usuario'
senha = 'sua_senha'
ip = 'seu_host'
porta = 5672  # Porta padrão do RabbitMQ
```

### 4. Execute o script
```bash
python app.py
```

O script se conectará ao servidor RabbitMQ, declarará a fila `teste_replica` e enviará uma mensagem de teste.

## Estrutura do Projeto
```
rabbitmq-sender-message/
│── app.py               # Script Python para envio de mensagens ao RabbitMQ
```

## Requisitos
- Python 3
- Biblioteca `pika` instalada (`pip install pika`)

## Possíveis Melhorias Futuras
- Implementar suporte para mensagens personalizadas via entrada do usuário
- Criar logs estruturados
- Adicionar suporte para configurações via variáveis de ambiente
