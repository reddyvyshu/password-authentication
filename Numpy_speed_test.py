import time
import numpy as np

size = 1000000

python_list = list(range(size))
numpy_array = np.arange(size)

start = time.time()
result_list = [x * 2 for x in python_list]
end = time.time()
list_time = end - start

start = time.time()
result_array = numpy_array * 2
end = time.time()
array_time = end - start

print("Python List Time:", list_time)
print("NumPy Array Time:", array_time)
