import pynvml
import psutil


def get_gpu_usage():
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

        # Get sum user memory info for the GPU
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        gpu_mem_util = 100 * mem_info.used / mem_info.total
        # gpu_mem_util keep 2 decimal places
        gpu_mem_util = round(gpu_mem_util, 2)
        gpu_usage["gpu_mem_util"] = gpu_mem_util
        # add gpu_name to gpu_usage dict
        gpu_usage[gpu_name] = {}
        # add gpu_temp to gpu_usage dict
        gpu_usage[gpu_name]["gpu_temp"] = gpu_temp
        # add gpu_util to gpu_usage dict
        gpu_usage[gpu_name]["gpu_util"] = gpu_util.gpu
        # add gpu_fan to gpu_usage dict
        gpu_usage[gpu_name]["gpu_fan"] = gpu_fan

        process_info = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
        if len(process_info) > 0:
            print("Running Processes:")
            for process in process_info:
                pid = process.pid
                gpu_mem = process.usedGpuMemory / 1024 ** 2

                try:
                    process = psutil.Process(pid)
                    # process_name = process.name()
                    user_name = process.username()
                except psutil.NoSuchProcess:
                    # process_name = "<unknown>"
                    user_name = "<unknown>"
                # add username to gpu_usage dict
                gpu_usage[gpu_name]["user_name"] = user_name
                # add used_memory to gpu_usage dict
                gpu_usage[gpu_name]["gpu_mem"] = gpu_mem
        else:
            gpu_usage[gpu_name]["user_name"] = "None"


    pynvml.nvmlShutdown()

    # print(f'gpu_usage: {gpu_usage}')


    return gpu_usage

if __name__ == '__main__':
    get_gpu_usage()
