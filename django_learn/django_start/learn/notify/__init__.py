import setting
# def send_info(content):
#     for path in learn.setting.NOTIFY_LIST:
#         print()
import importlib
def send_info(content):
    for path in setting.NOTIFY_LIST:
        # print(path)
        module_path,cls_name=path.rsplit('.',maxsplit=1)
        # print(module_path,cls_name)
        #根据字符串导入模块
        module = importlib.import_module(module_path)
        # a = importlib.import_module('')
        # print(module)
        cls = getattr(module,cls_name)
        obj = cls()
        # print(obj)
        obj.send(content)