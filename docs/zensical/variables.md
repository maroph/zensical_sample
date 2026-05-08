# Variables
How to define own variables is described in the chapter 
[Zensical Documentation: Macros](https://zensical.org/docs/setup/extensions/macros/#include_yaml-zensicaltoml).

## Own variables
The variables are defined in the module _data/variables.py_ or the YAML file
_data/variables.yml_.

* __Author__: {{ author }} 
* __Version__: {{ version }} 

## Built-in template variables
* __Python__: {{ environment['python_version'] }} 
* __System__: {{ environment['system'] }}
* __System Version__: {{ environment['system_version'] }}
* __Now__: {{ now() }} 

---

## Git metadata

Git: {{ git }}

---

## Built-in template variable macros_info
{{ macros_info() }} 

