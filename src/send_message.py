import time
import psutil
from utils.gpu_info import get_gpu_info
from utils.cpu_info import get_cpu_usage
from utils.other_info import get_other_info
import json
import socket

# 设置发送间隔时间，单位为秒
SEND_INTERVAL = 600

# 目标服务器的IP和端口号
HOST = 'example.com'
PORT = 1234

while True:
    # 获取CPU信息
    cpu_usage = get_cpu_usage()
    # 获取GPU信息
    gpu_usage = get_gpu_info()
    # 获取其他信息
    other_usage = get_other_info()

    # 将所有信息合并成一个字典
    all_usage = {
        'cpu_usage': cpu_usage,
        'gpu_usage': gpu_usage,
        'other_usage': other_usage
    }

    # 将字典转换成JSON格式
    json_usage = json.dumps(all_usage)

    # 创建一个TCP套接字对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # 连接到目标服务器
        sock.connect((HOST, PORT))

        # 发送JSON格式的数据
        sock.sendall(json_usage.encode('utf-8'))

        # 接收服务器的响应
        response = sock.recv(1024)

        # 打印响应结果
        print(response.decode('utf-8'))

    # 延时10分钟后再发送数据
    time.sleep(SEND_INTERVAL)
