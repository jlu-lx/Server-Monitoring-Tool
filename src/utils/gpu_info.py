import pynvml
import psutil


def get_gpu_info():
    gpu_info = {}  # create a dict
    pynvml.nvmlInit()
    num_gpus = pynvml.nvmlDeviceGetCount()

    for i in range(num_gpus):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        name = pynvml.nvmlDeviceGetName(handle)
        print(f"GPU {i}: {name}")
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        print(f"GPU {i} temperature: {temp}°C")
        # Get the GPU utilization percentage
        gpu_util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        print(f"GPU {i} utilization: {gpu_util.gpu} %")
        # Get the GPU fan speed
        fan_speed  = pynvml.nvmlDeviceGetFanSpeed(handle)
        # 获取风扇转速
        print(f"GPU {i} fan speed: {fan_speed }%")
        # Get memory info for the GPU
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        mem_percent = 100 * mem_info.used / mem_info.total

        # Get the list of running processes on the GPU
        process_info = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)

        print(f"Total Memory{i}: {mem_info.total/1024**2:.2f} MB")
        print(f"Free Memory{i}: {mem_info.free/1024**2:.2f} MB")
        print(f"Used Memory{i}: {mem_info.used/1024**2:.2f} MB\n")
        print(f"Used Memory percent {i}: {mem_percent:.2f}%\n")

        if len(process_info) > 0:
            print("Running Processes:")
            for process in process_info:
                pid = process.pid
                used_memory = process.usedGpuMemory / 1024 ** 2
                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                    username = process.username()
                except psutil.NoSuchProcess:
                    process_name = "<unknown>"
                    username = "<unknown>"

                print(f"Process ID: {pid}")
                print(f"Used Memory: {used_memory:.2f} MB")
                print(f"Process Name: {process_name}")
                print(f"User Name: {username}")
        else:
            print("No running processes found.")

    pynvml.nvmlShutdown()



    return gpu_info

if __name__ == '__main__':
    get_gpu_info()