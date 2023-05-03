import time
from utils.gpu_info import get_gpu_usage
from utils.cpu_info import get_cpu_usage
from utils.server_info import get_server_usage
import json
import socket


#指定要发送到的主机和端口
host = "192.168.0.100"
port = 12345

# 定义时间_间隔变量，单位为秒
time_interval = 600

# 创建一个socket对象
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 获取当前的日期和时间，分钟以十分钟为单位，秒置零
def get_current_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    current_time = current_time[:-4] + "0:00"
    return current_time


def send_message():
    # 连接到指定的主机和端口
    sock.connect((host, port))

    # 获取CPU信息
    cpu_usage = get_cpu_usage()
    gpu_usage = get_gpu_usage()
    server_usage = get_server_usage()

    # # 打印CPU信息
    # print(f"cpu_usage: {cpu_usage}")
    # # 打印GPU信息
    # print(f"gpu_usage: {gpu_usage}")
    # # 打印磁盘信息
    # print(f"server_usage: {server_usage}")

    # 将CPU、GPU和磁盘信息打包成一个JSON格式的字符串
    data = {
        "cpu_usage": cpu_usage,
        "gpu_usage": gpu_usage,
        "server_usage": server_usage,
        "save_time": get_current_time(),
    }
    print(f"data: {data}")
    json_data = json.dumps(data)

    print(f"json_data: {json_data}")
    # # 发送数据
    sock.sendall(json_data.encode())
    # # 关闭连接
    sock.close()

if __name__ == "__main__":
    while True:
        send_message()
        time.sleep(time_interval)  # Send data every 10 minutes (600 seconds)