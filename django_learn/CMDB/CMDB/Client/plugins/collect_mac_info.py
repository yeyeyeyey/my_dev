import os
import platform
# cmd1 = "/usr/sbin/system_profiler SPHardwareDataType"
# cmd2 = "/usr/sbin/system_profiler SPSoftwareDataType"
# output1 = os.popen(cmd1)
# output2 = os.popen(cmd2)
# print(output1.read())
# print(output2.read())
import subprocess
import json
def collect():
    """
    获取mac硬盘信息
    :return:
    """
    raw_data = {}
    #获取UUID
    res_uuid = subprocess.Popen("system_profiler SPHardwareDataType | grep 'UUID'",stdout=subprocess.PIPE,shell=True)
    UUID = res_uuid.stdout.read().decode().split(":")[1].strip()

    #获取ROM
    res_rom = subprocess.Popen("system_profiler SPHardwareDataType | grep ROM",stdout=subprocess.PIPE,shell=True)
    ROM = res_rom.stdout.read().decode().split(":")[1].strip()

    #获取serial序列化
    res_serial = subprocess.Popen("system_profiler SPHardwareDataType | grep Serial",stdout=subprocess.PIPE,shell=True)
    Serial_Number = res_serial.stdout.read().decode().split(":")[1].strip()

    #获取Memory
    res_memory = subprocess.Popen("system_profiler SPHardwareDataType | grep Memory",stdout=subprocess.PIPE,shell=True)
    Memory = res_memory.stdout.read().decode().split(":")[1].strip()

    #获取产品标识Model Identifier
    res_model = subprocess.Popen("system_profiler SPHardwareDataType | grep 'Model Identifier'",stdout=subprocess.PIPE,shell=True)
    Model_Identifier = res_model.stdout.read().decode().split(":")[1].strip()
    #获取processname
    res_processor_name = subprocess.Popen("system_profiler SPHardwareDataType | grep 'Processor Name'",stdout=subprocess.PIPE,shell=True)
    Processor_Name = res_processor_name.stdout.read().decode().split(":")[1].strip()
    res_processor_speed = subprocess.Popen("system_profiler SPHardwareDataType | grep 'Processor Speed'",stdout=subprocess.PIPE,shell=True)
    Processor_Speed = res_processor_speed.stdout.read().decode().split(":")[1].strip()
    res_processor_number = subprocess.Popen("system_profiler SPHardwareDataType | grep 'Number of Processors'",stdout=subprocess.PIPE,shell=True)
    Processor_Number = res_processor_number.stdout.read().decode().split(":")[1].strip()
    Processor_info = {}
    Processor_info['Processor_Name'] =Processor_Name
    Processor_info['Processor_Speed'] =Processor_Speed
    Processor_info['Processor_Number'] =Processor_Number



    #获取core_count内核数目
    res_core_count = subprocess.Popen("system_profiler SPHardwareDataType | grep Cores",stdout=subprocess.PIPE,shell=True)
    Core_Count = res_core_count.stdout.read().decode().split(":")[1].strip()

    #获取os操作系统信息
    res_os = subprocess.Popen("system_profiler SPSoftwareDataType | grep 'System Version'",stdout=subprocess.PIPE,shell=True)
    os_info = res_os.stdout.read().decode().split(":")[1].strip()

    #获取kernel 获取内核版本
    res_kernel = subprocess.Popen("system_profiler SPSoftwareDataType | grep 'Kernel Version'",stdout=subprocess.PIPE,shell=True)
    kernel = res_kernel.stdout.read().decode().split(":")[1].strip()


    #获取硬盘信息
    Physical_Driver = {}
    res_device_name = subprocess.Popen("system_profiler SPStorageDataType | grep 'Device Name'",stdout=subprocess.PIPE,shell=True)
    device_name = res_device_name.stdout.read().decode().split(":")[1].strip()

    res_media_name = subprocess.Popen("system_profiler SPStorageDataType | grep 'Media Name'",stdout=subprocess.PIPE,shell=True)
    media_name = res_media_name.stdout.read().decode().split(":")[1].strip()

    res_medium_type = subprocess.Popen("system_profiler SPStorageDataType | grep 'Medium Type'",stdout=subprocess.PIPE,shell=True)
    medium_type = res_medium_type.stdout.read().decode().split(":")[1].strip()
    Physical_Driver['device_name'] = device_name
    Physical_Driver['media_name'] = media_name
    Physical_Driver['medium_type'] = medium_type

    raw_data['Manufacturer'] = 'Apple'
    raw_data['UUID'] = UUID
    raw_data['ROM'] = ROM
    raw_data['sn'] = Serial_Number
    raw_data['Memory'] = Memory
    raw_data['Core_Count'] = Core_Count
    raw_data['os_info'] = os_info
    raw_data['kernel'] = kernel
    raw_data['Physical_Driver']=Physical_Driver
    raw_data['Model_Identifier']=Model_Identifier
    raw_data['Processor_info'] = Processor_info
    return raw_data
    # print(platform.system())
if __name__ == '__main__':
    # 收集信息功能测试
    # data = collect()
    # print(data)
    collect()