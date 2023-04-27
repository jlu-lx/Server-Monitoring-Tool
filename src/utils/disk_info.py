import psutil
import socket

def get_disk_usage():
    
    disk_info = {}

    # 获取磁盘使用情况
    disk_partitions = psutil.disk_partitions()

    i = 0
    for partition in disk_partitions:
        # 获取硬盘使用情况
        disk_usage = psutil.disk_usage(partition.mountpoint)
        if disk_usage.total / 1024**3 >100:
            disk_name = partition.device
            disk_util = disk_usage.percent
            disk_index = "disk" + str(i)
            i += 1
            disk_info[disk_index] = {}
            disk_info[disk_index][disk_index+"_util"] = disk_util
            disk_info[disk_index]["disk_name"] = disk_name


            # print("Partition: {}".format(partition))
            # print("Total space: {:.2f} GB".format(disk_usage.total / (1024**3)))
            # print("Used space: {:.2f} GB".format(disk_usage.used / (1024**3)))
            # print("Free space: {:.2f} GB".format(disk_usage.free / (1024**3)))
            # print("Usage percentage: {:.2f}%".format(disk_usage.percent))
            # return other_info
        
    # print(f"disk_info: {disk_info}")
    return disk_info

if __name__ == '__main__':
    get_disk_usage()