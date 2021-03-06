def memory_check(function):
    import psutil
    import os

    def wrapper():
        memory_usage_dict = dict(psutil.virtual_memory()._asdict())
        memory_usage_percent = memory_usage_dict['percent']
        print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
        # current process RAM usage
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

        result = function()

        memory_usage_dict = dict(psutil.virtual_memory()._asdict())
        memory_usage_percent = memory_usage_dict['percent']
        print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
        # current process RAM usage
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
        print("--" * 30)

        return result
    return wrapper

