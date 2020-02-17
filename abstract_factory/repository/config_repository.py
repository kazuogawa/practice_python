import configparser
from configparser import ConfigParser


class ConfigRepository:
    def __init__(self):
        config_ini: ConfigParser = configparser.ConfigParser()
        config_ini.read('abstract_factory/config/config.ini', encoding='utf-8')
        self.svg_text: str = config_ini['DEFAULT']['SVG_TEXT']
        self.svg_scale: int = int(config_ini['DEFAULT']['SVG_SCALE'])
        self.svg_start: str = config_ini['DEFAULT']['SVG_START']
