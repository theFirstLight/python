import multiprocessing
import time
import os


def work():
    for _ in range(10):
        print("work..")
        print(multiprocessing.current_process())
        print(f"subprocess pid: {multiprocessing.current_process().pid}")
        print(f"parent process pid: {os.getppid()}")
        time.sleep(0.2)


if __name__ == "__main__":
    process_obj = multiprocessing.Process(target=work)
    process_obj.start()
    for i in range(9):
        print(f"main processing: {multiprocessing.current_process()}")
        print(f"main processing pid: {multiprocessing.current_process().pid}")
        time.sleep(0.2)
