"""
    用来测试PYTHONPATH设置后，是否python解释器能够找到这个路径下的模块。
    pycharm找不到，但是交互式解释器可以找到,pycharm也得每次edit config才能找到。
    mac中交互式解释器必须source完配置文件才能找到，每次都得source。
"""
print('加载了test_module模块')
