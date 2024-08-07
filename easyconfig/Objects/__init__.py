import os
from pathlib import Path

import json
from typing import Dict

class Config:

    path : Path 
    config_name : str

    def __init__(self, path: Path, config_name: str):
        self.path = path
        if config_name.endswith('.json'):
            self.config_name = config_name
        else:
            self.config_name = config_name + '.json'
    
    def load_config(self):
        info = json.loads(open(self.path / self.config_name, 'r').read())
        for key in info:
            setattr(self, key, info[key])
        
    def save_config(self):
        info = {}
        for key in self.__dict__:
            print(key)
            if key not in ['path', 'config_name']:
                info[key] = getattr(self, key)
        with open(self.path / self.config_name, 'w') as f:
            f.write(json.dumps(info, indent=4))

    def remove_config(self):
        os.remove(self.path / self.config_name)

    def __str__(self):
        return str(self.__dict__)
    
    def json(self):
        return json.dumps(self.__dict__, indent=4)