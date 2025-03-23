import numpy as np
from multiprocessing import Pool
import time

def total_distance_fast(left_list, right_list):
    if len(left_list) != len(right_list):
        raise ValueError("Lists must be of equal length")
    
    with Pool(2) as p:
        left_sorted, right_sorted = p.map(np.sort, [left_list, right_list])
    
    return np.sum(np.abs(left_sorted - right_sorted))

n_large = 1_000_000
left_list_large = np.random.randint(1, 1_000_000, n_large, dtype=np.int32)
right_list_large = np.random.randint(1, 1_000_000, n_large, dtype=np.int32)

start_time = time.time()
result_large = total_distance_fast(left_list_large, right_list_large)
end_time = time.time()

print(f"Optimized Execution Time: {end_time - start_time:.4f} seconds")
print(f"Result: {result_large}")
