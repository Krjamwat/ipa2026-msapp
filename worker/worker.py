import os
from consumer import consume

host = os.getenv("RABBITMQ_DEFAULT_HOST", "rabbitmq")
consume(host)
