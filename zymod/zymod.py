#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import signal
from argparse import ArgumentParser
from pathlib import Path

import grpc
from happy_python import HappyLog

from zymod import ZymodConfig
from zymod import zhiyan_rpc_pb2
from zymod import zhiyan_rpc_pb2_grpc
from zymod.zymod_config import ZymodConfigParser

__version__ = '1.3.2'


# noinspection PyUnusedLocal
def interrupt_from_keyboard_handler(signum, frame):
    print('\n检测到用户发送终止信号，退出程序中......')
    exit(1)


class Zymod:
    hlog = HappyLog.get_instance()
    mod_conf: ZymodConfig
    parser: ArgumentParser

    def __init__(self, mod_config: Path, is_dry_run_from_cmd_args, is_verbose_from_cmd_args):
        signal.signal(signal.SIGINT, interrupt_from_keyboard_handler)

        if not mod_config.exists():
            self.hlog.error('智眼模块配置文件（%s）不存在' % mod_config)
            exit(1)

        self.hlog = HappyLog.get_instance(str(mod_config))

        is_dry_run = True if is_dry_run_from_cmd_args else None
        is_verbose = True if is_verbose_from_cmd_args else None
        self.mod_conf = ZymodConfigParser(str(mod_config)).load(is_dry_run, is_verbose)

    def upload(self, name: str, datetime: int, content: dict):
        fn_name = 'mod_send_request_grpc'

        hlog = HappyLog.get_instance()
        hlog.enter_func(fn_name)

        hlog.var('name', name)
        hlog.var('datetime', datetime)

        json_str_content = json.dumps(content)
        hlog.debug('content=\n%s' % json_str_content)

        if self.mod_conf.dry_run:
            hlog.debug('zymod：在不做任何更改的情况下试运行.....')
        else:
            hlog.debug('zymod：正在上传到agent.....')

            channel = grpc.insecure_channel(self.mod_conf.agent_host + ':' + str(self.mod_conf.agent_port))
            client = zhiyan_rpc_pb2_grpc.ZhiYanStub(channel)
            response = client.zymod(zhiyan_rpc_pb2.ZhiYanRequest(
                name=name,
                datetime=datetime,
                content=json_str_content
            ))

            hlog.var('response', response)

        hlog.exit_func(fn_name)

    @staticmethod
    def build_help_parser(prog: str, description: str, version: str) -> ArgumentParser:
        parser = ArgumentParser(prog=prog, description=description)

        parser.add_argument('-c',
                            '--conf',
                            help='指定智眼模块配置文件（默认：/etc/zhiyan/conf.d/processes.conf）',
                            dest='mod_conf',
                            type=str,
                            default='/etc/zhiyan/conf.d/processes.conf')
        parser.add_argument('-n',
                            '--dry-run',
                            help='在不做任何更改的情况下试运行，通常和"-v"参数一起使用',
                            dest='dry_run',
                            action='store_true')
        parser.add_argument('-v',
                            '--verbose',
                            help='显示详细信息',
                            dest='verbose',
                            action='store_true')
        parser.add_argument('-V',
                            '--version',
                            help='显示版本信息',
                            action='version',
                            version='zymod version: %(prog)s/v' + version)

        return parser

    @staticmethod
    def build_help(prog: str, description: str, version: str):
        parser = Zymod.build_help_parser(prog=prog, description=description, version=version)
        return parser.parse_args()

    @staticmethod
    def build_help_with_parser(parser: ArgumentParser):
        return parser.parse_args()
