import pynvml
import psutil
import socket
from .cpu_info import get_cpu_usage
from .disk_info import get_disk_usage

def get_server_usage():
    server_usage = {}                           # create a dict

    # 获取服务器名称
    server_name = socket.gethostname()          # wsn-01、wsn-02...
    mem_util = psutil.virtual_memory()          # 内存信息
    cpu_usage = get_cpu_usage()
    disk_usage = get_disk_usage()


    server_usage["server_name"] = server_name
    server_usage["mem_util"] = mem_util.percent
    server_usage["cpu_usage"] = cpu_usage
    server_usage["disk_usage"] = disk_usage

    return server_usage

if __name__ == '__main__':

    print(f'get_server_usage: {get_server_usage()}')
    # get_server_usage()
    # save_time = get_current_time()
    # print(f'save_time: {save_time}')
