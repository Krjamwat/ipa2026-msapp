import os
from consumer import consume

host = os.getenv("RABBITMQ_HOST", "rabbitmq")
consume(host)