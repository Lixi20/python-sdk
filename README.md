## 从 pip 安装

`pip install python-sdk`

## 使用方法

### 使用

比如：

`from python_sdk import say_hello'`
## 本地打包安装

### 打包

安装依赖包：

`pip install -U setuptools wheel`

运行：

`python setup.py bdist_wheel`

在 `dist` 目录下会生成类似 `python_sdk-1.0.0-py3-none-any.whl` 的安装包。


### 本地安装

全局安装：
     
`pip install -U python_sdk-1.0.0-py3-none-any.whl`
 
用户目录安装：
    
`pip install --user -U python_sdk-1.0.0-py3-none-any.whl`

### 卸载

`pip uninstall python-sdk`