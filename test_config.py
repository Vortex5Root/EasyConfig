import os
import shutil

import pytest

from easyconfig import Config_Manager
from easyconfig.Objects import Config


def test_start_config_manager():
    config_manager = Config_Manager('test_configs')
    assert config_manager.main_path.exists()
    assert config_manager.main_path.is_dir()
    assert config_manager.configs == {}

def test_new_config():
    config_manager = Config_Manager('test_configs')
    config = config_manager.new_config('test_config')
    assert config_manager.configs == {'test_config': config}
    assert config.path == config_manager.main_path
    assert config.config_name == 'test_config.json'

def test_new_config_sub_directory():
    config_manager = Config_Manager('test_configs')
    config = config_manager.new_config('test_config', 'sub_directory')
    assert "sub_directory/test_config" in config_manager.configs
    assert config_manager.configs["sub_directory/test_config"] == config
    assert config.path == config_manager.main_path / 'sub_directory'
    assert config.config_name == 'test_config.json'

def test_save_configs():
    config_manager = Config_Manager('test_configs')
    config = config_manager.new_config('test_config')
    config.test = 'test'
    config.save_config()
    config_manager.save_configs()
    config_manager.load_configs()
    assert "test_config" in config_manager.configs
    assert config_manager.configs["test_config"] == config
    assert (config_manager.configs["test_config"].path / config_manager.configs["test_config"].config_name).exists()
    assert config_manager.configs["test_config"].test == 'test'

def test_load_configs():
    config_manager = Config_Manager('test_configs')
    config = config_manager.new_config('test_config')
    config.test = 'test'
    config.save_config()
    config_manager.load_configs()
    assert "test_config" in config_manager.configs
    assert config_manager.configs["test_config"] == config
    assert (config_manager.configs["test_config"].path / config_manager.configs["test_config"].config_name).exists()
    assert config_manager.configs["test_config"].test == 'test'

def test_remove_configs():
    shutil.rmtree('test_configs')
    assert not os.path.exists('test_configs')