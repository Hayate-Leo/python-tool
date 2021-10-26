import concurrent.futures
import time

start = time.perf_counter()


def wait_time(sec):
    print(f'{sec}秒待機中．．．')
    time.sleep(sec)
    return f'{sec}秒待機終了'

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(wait_time, secs)

    # secs = [5, 4, 3, 2, 1]

    # for sec in secs:
    #     print(f'{sec}秒待機中．．．')
    #     time.sleep(sec)
    #     print(f'{sec}秒待機終了')
    
    # results = map(wait_time, secs)
    for result in results:
        print(result)

    finish = time.perf_counter()
    print(f'{round(finish-start, 2)}秒で終了')