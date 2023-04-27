import psutil
import json
import requests

def get_cpu_usage():

    # create a dict
    cpu_usage = {}  
    # 获取 CPU 占用率
    cpu_util = psutil.cpu_percent(2)
    # 获取物理核心数和逻辑核心数
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)

    cpu_usage["cpu_util"] = cpu_util
    cpu_usage["cpu_cores"] = physical_cores


    return cpu_usage

if __name__ == '__main__':
    get_cpu_usage()



    # disk = psutil.disk_usage('/')
    # print(f"Disk: {disk.total} (total), {disk.used} (used), {disk.free} (free)")

    # # 获取硬件内存使用情况
    # mem = psutil.virtual_memory()
    # mem_total = mem.total // (1024 * 1024) # 硬件内存总量（MB）
    # mem_used = mem.used // (1024 * 1024) # 已使用硬件内存（MB）
    # mem_free = mem.free // (1024 * 1024) # 空闲硬件内存（MB）
    # print("Hardware memory usage:", mem_total, mem_used, mem_free)
    # print("CPU usage: {}%".format(cpu_usage))
    # print("Physical cores: {}".format(physical_cores))
    # print("Logical cores: {}".format(logical_cores))



    # print("CPU usage: {}".format(cpu_usage))
