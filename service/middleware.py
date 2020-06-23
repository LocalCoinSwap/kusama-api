from ksmutils import Kusama

from .settings import ARBITRATOR_KEY
from .settings import NODE_PROVIDER

print("-" * 90)
print(NODE_PROVIDER)
kusama = Kusama(arbitrator_key=ARBITRATOR_KEY, node_url=NODE_PROVIDER)
kusama.connect()
kusama.runtime_info()
