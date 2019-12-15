import sys
import platform
class InfoCollection(object):
    def collect(self):
        #收集平台信息
        #首先判断当前平台，根据平台不同，执行不同的方法
        try:
            func = getattr(self,platform.system().lower())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前系统：[%s]!"%platform.system())

    @staticmethod
    def linux():
        from plugins.collect_linux_info import collect
        return collect()

    @staticmethod
    def windows():
        from plugins.collect_windows_info import Win32Info
        return Win32Info.collect()

    @staticmethod
    def darwin():
        from plugins.collect_mac_info import collect
        return collect()
    @staticmethod
    def build_report_data(data):
        #留下一个接口，方便以后增加功能或者过滤数据
        pass
        return data

    # 首先通过Python内置的platform模块获取执行main脚本的操作系统类别，通常是windows和Linux，暂时不支持其它操作系统；
    # 根据操作系统的不同，反射获取相应的信息收集方法，并执行；
    # 如果是客户端不支持的操作系统，比如苹果系统，则提示并退出客户端。