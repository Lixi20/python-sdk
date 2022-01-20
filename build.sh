#!/usr/bin/sh

python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. zymod/zhiyan_rpc.proto || exit
rm -rf build/ dist/ && python setup.py bdist_wheel || exit
pip install -U --force-reinstall dist/zymod-*-py3-none-any.whl