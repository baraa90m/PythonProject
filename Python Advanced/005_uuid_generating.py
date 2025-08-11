"""
uuid: is a built-in module for generating universally unique identifiers (UUIDs).
"""

import uuid

class Entity:
    def __init__(self):
        self._id = str(uuid.uuid4())

e = Entity()
print(e._id)