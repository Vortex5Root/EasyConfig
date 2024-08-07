from typing  import Dict
from pathlib import Path

from .Objects import Config

class Config_Manager:

    main_path : Path
    configs : Dict[str, Config] = {}

    def __init__(self, working_dir : str):
        self.main_path = Path(working_dir)
        if not self.main_path.exists():
            self.main_path.mkdir()
        else:
            if not self.main_path.is_dir():
                raise Exception(f'{working_dir} is not a directory')
            self.load_configs()

    def new_config(self, config_name: str, sub_directory: str = None):
        if sub_directory is not None:
            path = self.main_path / sub_directory
            if not path.exists():
                path.mkdir()
            config = Config(path, config_name)
            config_name = sub_directory + '/' + config_name
        else:
            config = Config(self.main_path, config_name)
        self.configs[config_name] = config
        return config
    
    def get_config(self, config_name: str):
        if config_name in self.configs:
            return self.configs.get(config_name)
    
    def remove_config(self, config_name: str):
        if config_name in self.configs:
            self.configs[config_name].remove_config()
            del self.configs[config_name]

    def unload_config(self, config_name: str):
        if config_name in self.configs:
            del self.configs[config_name]

    def get_value(self, config_name: str, key: str):
        if config_name in self.configs:
            return getattr(self.configs[config_name], key)

    def get_all_configs(self):
        return self.configs
    
    def get_all_config_names(self):
        return self.configs.keys()
    
    def set_value(self, config_name: str, key: str, value):
        if config_name in self.configs:
            setattr(self.configs[config_name], key, value)

    def load_configs(self):
        for file in self.main_path.iterdir():
            if file.is_file() and file.suffix == '.json':
                config = Config(self.main_path, file.name)
                config.load_config()
                self.configs[file.name] = config

    def save_config(self, config_name: str):
        if config_name in self.configs:
            self.configs[config_name].save_config()
    
    def save_configs(self):
        for key in self.configs:
            self.configs[key].save_config()
