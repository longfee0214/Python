import multiprocessing
import threading
import time


class TimeoutException(Exception):
    pass


def do_task():
    try:
        # 执行任务
        time.sleep(4)
    except TimeoutException as e:
        print(e)


def timeout_task():
    p = multiprocessing.Process(target=do_task)
    p.start()
    p.join(5)

    if p.is_alive():
        # 停止进程
        p.terminate()
        raise TimeoutException("Task timed out")


if __name__ == "__main__":
    timeout_task()
