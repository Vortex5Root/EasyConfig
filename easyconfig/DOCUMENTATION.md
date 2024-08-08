<h1 align="center">Easy Config</h1>

<p align="center">
    <a href="https://github.com/Vortex5Root/EasyConfig/releases"><img alt="Dynamic TOML Badge" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FVortex5Root%2FEasyConfig%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.version&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAtFBMVEVHcEyWYTihdkuXYzrBjlqhbkHepWuzglG8hFGWYjmzglHepmz3z5iygVCWYjmWYjmxgVDsvorMlmDepmybaD2oe02ufU2leUzdpWqzglGfdUrgqnH616j%2F4LKWYjmvf1C3hVPepmyWYjmWZDuWYjmzglGWYjmwfk7fp22aZjz93a7VoGmpfFKdbEe4hlTFkFzwxZH30aDpuYO%2BnICUbUbGkl3jrnbjr3eSYjuuiWzNq4fjvI5PAatoAAAAJXRSTlMA4v34FBH4Jwwn4l8IXFG6%2FrWcv2PCZqdJxeX291Ci4uVQ5eQoZPLoqAAAAIxJREFUCNdFzscCgjAQBNA1JIAGVMDeW0iEAPb6%2F%2F9lCuqc9s1eBkDHpxTDN8E8mroJ9S1G0Sw7noSbrAMAHLvidshMERPwVlUuxF0Vb7ltgtdi5VUV%2BetcNAwZKyv%2BeP7J%2BD6VRaq5rKmiOUGoW3OzAzxEF2npLIgaGPbN1%2Bm07S4SjvkPOnjQI%2Bb4AGCaEYNClUKKAAAAAElFTkSuQmCC&label=Package%20Version"></a>
</p>

-------

<p align="center">
    <a href="https://github.com/Vortex5Root/EasyConfig/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Vortex5Root/EasyConfig.svg" alt="License">
    <a href="https://github.com/Vortex5Root/EasyConfig/releases"><img src="https://img.shields.io/github/downloads/Vortex5Root/EasyConfig/total.svg" alt="GitHub all releases"></a><br>
    <a href="https://github.com/Vortex5Root/EasyConfig/network"><img src="https://img.shields.io/github/forks/Vortex5Root/EasyConfig.svg" alt="GitHub forks"></a>
    <a href="https://github.com/Vortex5Root/EasyConfig/stargazers"><img src="https://img.shields.io/github/stars/Vortex5Root/EasyConfig.svg" alt="GitHub stars"></a>
    <a href="https://github.com/Vortex5Root/EasyConfig/watchers"><img src="https://img.shields.io/github/watchers/Vortex5Root/EasyConfig.svg" alt="GitHub watchers"></a><br>
    <a href="https://github.com/Vortex5Root/EasyConfig/issues"><img src="https://img.shields.io/github/issues/Vortex5Root/EasyConfig.svg" alt="GitHub issues"></a>
    <a href="https://github.com/Vortex5Root/EasyConfig/pulls"><img src="https://img.shields.io/github/issues-pr/Vortex5Root/EasyConfig.svg" alt="GitHub pull requests"></a>
    <a href="https://github.com/Vortex5Root/EasyConfig/commits/master"><img src="https://img.shields.io/github/last-commit/Vortex5Root/EasyConfig.svg" alt="GitHub last commit"></a><br>
</p>

<h2 align="center"> Introduction </h2>

> This Documetaion aims to provide a good understanding of the EasyConfig library. It is designed to be easy to use and easy to understand. It is also designed to be easy to use with other libraries and frameworks.

<h2 align="center"> Index </h2>

| Topic | sub-topic |
| --- | --- |
| [Dependencies](#dependencies) | |
| [Installation](#installation) | |
| [Documentation](#documentation) |  |
| | [How to use EasyConfig](#how-to-use-easyconfig) |
| | [How to add a new configuration](#how-to-add-a-new-configuration) |
| | [How to remove a configuration](#how-to-remove-a-configuration) |
| | [How to get a configuration](#how-to-get-a-configuration) |
| | [How to get a value from a configuration](#how-to-get-a-value-from-a-configuration) |
| | [How to get all the configurations](#how-to-get-all-the-configurations) |
| | [How to get all the configuration names](#how-to-get-all-the-configuration-names) |
| | [How set a value in a configuration](#how-set-a-value-in-a-configuration) |
| | [How to save the configurations](#how-to-save-the-configurations) |
| | [How to load the configurations](#how-to-load-the-configurations) |
| [Acknowledgements](#acknowledgements) | |


<h2 align="center">Dependencies</h2>

| Name | Version | Description |
| --- | --- | --- |
| [![Linux](https://img.shields.io/badge/Linux-A81D33?style=for-the-badge&logo=linux&logoColor=ffffff)](https://www.linux.org/) | 5.14.0 | Linux is a family of open-source Unix-like operating systems based on the Linux kernel. |
| [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) | >=3.11 | Python is an interpreted high-level general-purpose programming language. |
| [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json?style=for-the-badge)](https://python-poetry.org/) | 1.1.8 | Poetry is a tool for dependency management and packaging in Python. |

<h2 align="center">Installation</h2>

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
```bash
poetry add git+https://github.com/Vortex5Root/EasyConfig.git
```

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
```bash
pip install git+https://github.com/Vortex5Root/EasyConfig.git#egg=easyconfig
```

<h2 align="center">Documentation</h2>

------

<h3 align="center">How to use EasyConfig</h3>

```python
from easyconfig import Config_Manager

config = Config_Manager(working_dir="configs") # You can also pass a constume working directory
```

<h3 align="center">How to add a new configuratio</h3>

```python
config.add_config("config_name", {"key": "value"})
```

<h3 align="center">How to remove a configuration</h3>

```python
config.remove_config("config_name")
```

<h3 align="center">How to get a configuration</h3>

```python
config.get_config("config_name")
```

<h3 align="center">How to get a value from a configuration</h3>

```python
config.get_value("config_name", "key")
```

<h3 align="center">How to get all the configurations</h3>

```python
config.get_all_configs()
```

<h3 align="center">How to get all the configuration names</h3>

```python
config.get_all_config_names()
```

<h3 align="center">How set a value in a configuration</h3>

```python
config.set_value("config_name", "key", "value")
```

<h3 align="center">How to save one the configuration</h3>

```python
config.save_config("config_name")
```

<h3 align="center">How to save all the configurations</h3>

```python
config.save_configs()
```

<h3 align="center">How to load the configurations</h3>

```python
config.load_configs()
```

<h2 align="center">Acknowledgements</h2>

<p align="center">
    <br>[Coder]<br>
    <a href="https://github.com/Vortex5Root"><img src=https://avatars.githubusercontent.com/u/102427260?s=200&v=4 width=50 style="border-radius: 50%;"><br>Vortex5Root <br><b>        {Full-Stack Software Engineer}</b></a><br>
    <br>[Contributor]<br>
    <a href="https://github.com/PandemicOfNukes"><img src=https://avatars.githubusercontent.com/u/59929476?s=200&v=4 width=50 style="border-radius: 50%;"><br>PandemicOfNukes <br><b>        {Student}</b></a><br><br>
</p>
