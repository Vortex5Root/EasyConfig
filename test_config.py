import os
import shutil

import pytest

from easyconfig import Config_Manager
from easyconfig.Objects import Config


def test_start_config_manager():
    config_manager = Config_Manager('test_configs')
    assert config_manager.main_path.exists()
    assert config_manager.main_path.is_dir()

def test_new_config():
    config_manager = Config_Manager('test_configs')
    config = config_manager.new_config('test_config')
    assert 'test_config' in config_manager.configs
    assert config.path == config_manager.main_path
    assert config.config_name == 'test_config'

def test_new_config_sub_directory():
    config_manager = Config_Manager('test_configs')
    config = config_manager.new_config('test_config', 'sub_directory')
    assert "sub_directory/test_config" in config_manager.configs
    assert config_manager.configs["sub_directory/test_config"] == config
    assert config.path == config_manager.main_path / 'sub_directory'
    assert config.config_name == 'test_config'

def test_save_configs():
    config_manager = Config_Manager('test_configs')
    config = config_manager.new_config('test_config')
    config.test = 'test'
    config.test2 = 'test2'
    config.save_config()
    config_manager.save_configs()
    config_manager.load_configs()
    assert "test_config" in config_manager.configs
    assert config_manager.configs["test_config"].__dict__ == config.__dict__
    assert (config_manager.configs["test_config"].path / (config_manager.configs["test_config"].config_name + ".json")).exists()
    assert config_manager.configs["test_config"].test == 'test'

def test_update_config():
    config_manager = Config_Manager('test_configs')
    config_manager.load_configs()
    config = config_manager.configs["test_config"]
    config.test3 = 'test3'
    config.save_config()
    config_manager.save_configs()
    assert "test_config" in config_manager.configs
    assert config_manager.configs["test_config"].__dict__ == config.__dict__
    assert (config_manager.configs["test_config"].path / (config_manager.configs["test_config"].config_name + ".json")).exists()
    assert config_manager.configs["test_config"].test3 == 'test3'

def test_load_configs():
    config_manager = Config_Manager('test_configs')
    config_manager.load_configs()
    assert "test_config" in config_manager.configs
    assert config_manager.configs["test_config"].__dict__ != {}
    assert (config_manager.configs["test_config"].path / (config_manager.configs["test_config"].config_name + ".json")).exists()
    assert config_manager.configs["test_config"].test == 'test'
    assert config_manager.configs["test_config"].test2 == 'test2'
    assert config_manager.configs["test_config"].test3 == 'test3'

def test_get_config():
    config_manager = Config_Manager('test_configs')
    config_manager.load_configs()
    config = config_manager.get_config('test_config')
    assert config == config_manager.configs['test_config']

def test_get_value():
    config_manager = Config_Manager('test_configs')
    config_manager.load_configs()
    value = config_manager.get_value('test_config', 'test')
    assert value == 'test'

def test_set_value():
    config_manager = Config_Manager('test_configs')
    config_manager.load_configs()
    config_manager.set_value('test_config', 'test', 'new_test')
    assert config_manager.get_value('test_config', 'test') == 'new_test'

def test_remove_config():
    config_manager = Config_Manager('test_configs')
    config_manager.load_configs()
    config_manager.remove_config('test_config')
    assert 'test_config' not in config_manager.configs
    assert not (config_manager.main_path / 'test_config.json').exists()