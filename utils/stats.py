import psutil

max_mem = 0
max_cpu = 0


async def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss / 1024 / 1024  # Convert to MB


async def get_cpu_load():
    return psutil.cpu_percent()


async def stats():
    global max_mem, max_cpu
    memory_usage = await get_memory_usage()
    cpu_load = await get_cpu_load()

    if memory_usage > max_mem:
        print(f"Memory Usage: {memory_usage} MB")
        max_mem = memory_usage

    if cpu_load > max_cpu:
        print(f"CPU Load: {cpu_load}%")
        max_cpu = cpu_load

    return f'Memory Usage: {memory_usage} MB\n' \
           f'CPU Load: {cpu_load}%'

