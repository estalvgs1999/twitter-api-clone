from typing import Dict
from uuid import UUID
from datetime import date, datetime

def serialize(d: Dict):
    for key in d:
        val = d[key]
        # For nested objects
        if type(val) is dict:
            serialize(val)
            continue
        if type(val) in [UUID, datetime, date]:
            d[key] = str(val)
    return d
