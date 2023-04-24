import pyudev
import socket


context = pyudev.Context()
for device in context.list_devices(subsystem='block', DEVTYPE='disk'):
    # 处理磁盘信息
    print(f"Disk: {device.device_node}")
    print(f"  Size: {device.attributes.asint('size')} bytes")  

# 获取主机名称
hostname = socket.gethostname()

# 输出主机名称和Linux系统名称
print("Hostname:", hostname)
print("Linux system name:", hostname)
