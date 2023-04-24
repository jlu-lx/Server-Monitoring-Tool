import psutil
import socket

def get_other_info():
    other_info = {}
    memory_info = psutil.virtual_memory()  # 内存信息

    # 获取磁盘使用情况
    disk_partitions = psutil.disk_partitions()

    for partition in disk_partitions:
        # 获取硬盘使用情况
        disk_usage = psutil.disk_usage(partition.mountpoint)
        print("Partition: {}".format(partition.device))
        print("Total space: {:.2f} GB".format(disk_usage.total / (1024**3)))
        print("Used space: {:.2f} GB".format(disk_usage.used / (1024**3)))
        print("Free space: {:.2f} GB".format(disk_usage.free / (1024**3)))
        print("Usage percentage: {:.2f}%".format(disk_usage.percent))
        # return other_info

    # 获取服务器名称
    server_name = socket.gethostname()    # wsn-01、wsn-02...
    print("server name:",server_name)

    # other_info["disk_usage"] = 
    other_info["memory_info"] = memory_info
    other_info["server_name"] = server_name


if __name__ == '__main__':
    get_other_info()