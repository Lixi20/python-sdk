# libzymod-python

智眼Python SDK

## 生成gRPC代码

安装依赖：

`pip install -U grpcio protobuf grpcio-tools`

生成gRPC代码：

`python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. zymod/zhiyan_rpc.proto`

gRPC工具会生成两个Python文件：

* zymod/zhiyan_rpc_pb2.py
* zymod/zhiyan_rpc_pb2_grpc.py

## 注意事项

生成 `zymod/zhiyan_rpc_pb2_grpc.py` 文件后，需要确认其中导入 `zhiyan_rpc_pb2.py` 是否正确：

```python
from zymod import zhiyan_rpc_pb2 as zymod_dot_zhiyan__rpc__pb2
```

## 安装SDK

### 从 pip 安装

`pip install -U zymod`

### 使用方法

#### 使用

比如：

`from zymod import upload`

### 本地打包安装

#### 打包

安装依赖包：

`pip install -U setuptools wheel`

运行：

`rm -rf build/ dist/ zymod.egg-info/ && python setup.py bdist_wheel`

在 `dist` 目录下会生成类似 `zymod-1.0.0-py3-none-any.whl` 的安装包。

#### 本地安装

全局安装：

`sudo pip install -U dist/zymod-*-py3-none-any.whl`

用户目录安装：

`pip install --user -U dist/zymod-*-py3-none-any.whl`

#### 卸载

`pip uninstall zymod`

### 上传至PyPI

#### 配置文件

`~/.pypirc`

```
[distutils]
index-servers=
    pypi

[pypi]
username: <用户名>
password: <密码>
```

#### 安装上传工具

`pip install -U twine`

#### 上传

`twine upload dist/*`

如果使用国内镜像源，需要等一两天国内服务器才会同步官方源。

可以临时指定官方源安装：

`python3 -m pip install -i https://pypi.org/simple/ example-pkg`
