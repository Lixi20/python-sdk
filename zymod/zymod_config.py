#!/usr/bin/python3
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from dataclasses import dataclass

from happy_python import HappyLog
from happy_python.happy_log import HappyLogLevel


@dataclass
class ZymodConfig:
    mod_name: str
    interval: int
    agent_host: str
    agent_port: int
    active: bool
    debug: int
    dry_run: bool


class ZymodConfigParser:
    _filename: str

    def __init__(self, filename: str) -> None:
        self._filename = filename

    def load(self, is_dry_run, is_verbose) -> ZymodConfig:
        conf = ConfigParser()
        conf.read(self._filename)

        if 'zymod' not in conf:
            raise Exception("配置文件缺少section")

        section = conf['zymod']

        _debug = section.getint('debug') if is_verbose is None else HappyLogLevel.DEBUG.value
        _dry_run = section.getboolean('dry_run') if is_dry_run is None else True

        mod_conf = ZymodConfig(mod_name=section.get('mod_name'),
                               active=section.getboolean('active'),
                               agent_host=section.get('agent_host'),
                               agent_port=section.getint('agent_port'),
                               debug=_debug,
                               dry_run=_dry_run,
                               interval=section.getint('interval'),
                               )

        hlog = HappyLog.get_instance()
        hlog.set_level(mod_conf.debug)

        return mod_conf
