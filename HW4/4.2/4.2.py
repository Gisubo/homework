import math
import time
import concurrent.futures
import multiprocessing
import csv

def integrate_segment(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def integrate_worker(args):
    # пробовал с lambda запускать, не проходило) пришлось так сделать

    return integrate_segment(*args)


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_cls=concurrent.futures.ThreadPoolExecutor):
    chunk_size = n_iter // n_jobs
    args = [(f, a + i * (b - a) / n_jobs, a + (i + 1) * (b - a) / n_jobs, chunk_size) for i in range(n_jobs)]
    with executor_cls(max_workers=n_jobs) as executor:
        results = list(executor.map(integrate_segment, *args))

    return sum(results)


if __name__ == "__main__":
    cpu_num = multiprocessing.cpu_count()
    n_iter = int(1e9)
    results = []

    for executor_cls, name in [(concurrent.futures.ThreadPoolExecutor, "ThreadPool"), (concurrent.futures.ProcessPoolExecutor, "ProcessPool")]:
        for i in range(8):
            n_jobs = 1 if i==0 else i*2
            start_time = time.time()
            integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=n_iter, executor_cls=executor_cls)
            time_result = time.time() - start_time
            results.append((name, n_jobs, time_result))
            print(f"{name} with {n_jobs} jobs: {time_result:.4f} sec")

