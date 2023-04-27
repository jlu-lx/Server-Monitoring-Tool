import pynvml
import psutil


def get_gpu_info():
    gpu_usage = {}  # create a dict
    pynvml.nvmlInit()
    num_gpus = pynvml.nvmlDeviceGetCount()

    for i in range(num_gpus):

        

        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        # 把name字符串中的空格替换为下划线
        gpu_name = gpu_name.replace(" ", "_")+"_"+str(i)
        gpu_temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        gpu_util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        gpu_fan  = pynvml.nvmlDeviceGetFanSpeed(handle)

        # Get memory info for the GPU
        # mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        # gpu_mem = 100 * mem_info.used / mem_info.total
        # Get the list of running processes on the GPU
        
        # add gpu_name to gpu_usage dict
        gpu_usage["gpu_name"] = gpu_name
        # add gpu_temp to gpu_usage dict
        gpu_usage["gpu_temp"] = gpu_temp
        # add gpu_util to gpu_usage dict
        gpu_usage["gpu_util"] = gpu_util.gpu
        # add gpu_fan to gpu_usage dict
        gpu_usage["gpu_fan"] = gpu_fan


        print(f"GPU {i}: {gpu_name}")
        print(f"GPU {i} temperature: {gpu_temp}°C")
        # Get the GPU utilization percentage
        print(f"GPU {i} utilization: {gpu_util.gpu} %")
        # Get the GPU fan speed
        # 获取风扇转速
        print(f"GPU {i} fan speed: {gpu_fan }%")
        # print(f"Used Memory percent {i}: {gpu_mem:.2f}%\n")
        process_info = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
        if len(process_info) > 0:
            print("Running Processes:")
            for process in process_info:
                pid = process.pid
                gpu_mem = process.usedGpuMemory / 1024 ** 2

                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                    user_name = process.username()
                except psutil.NoSuchProcess:
                    process_name = "<unknown>"
                    user_name = "<unknown>"
                # add username to gpu_usage dict
                gpu_usage["user_name"] = user_name
                # add used_memory to gpu_usage dict
                gpu_usage["gpu_mem"] = gpu_mem

                print(f"{user_name}Used Memory: {gpu_mem:.2f} MB")
                print(f"User Name: {user_name}")
        else:
            print("No running processes found.")

    pynvml.nvmlShutdown()
    

    print(f'gpu_usage: {gpu_usage}')


    return gpu_usage

if __name__ == '__main__':
    get_gpu_info()