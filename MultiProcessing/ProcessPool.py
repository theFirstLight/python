import multiprocessing
import time


def work():
    print(f"{multiprocessing.current_process()} is working")
    time.sleep(0.2)


if __name__ == '__main__':
    process_pool = multiprocessing.Pool(9)
    print(f"cpu core num: {multiprocessing.cpu_count()}")
    for i in range(20):
        # process_pool.apply(work)
        process_pool.apply_async(work)

    # 如果采用异步的方式,需要下面两句代码
    process_pool.close()  # 不再接受新的任务
    process_pool.join()   # 让主进程等待进程池接收后再退出
