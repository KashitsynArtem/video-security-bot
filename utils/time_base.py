import time


async def get_current_time():
    return time.time()


async def delta_time(start_time, stop_time):
    return start_time - stop_time

