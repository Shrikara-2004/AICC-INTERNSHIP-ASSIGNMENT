# NumPy Speed Test

import numpy as np
import time

# Create 1 million numbers using Python list
python_list = list(range(1000000))

# Create 1 million numbers using NumPy array
numpy_array = np.arange(1000000)

# Test operation with Python list
start_time = time.time()

result_list = [x * 2 for x in python_list]

end_time = time.time()
list_time = end_time - start_time

print("Time taken by Python list:", list_time, "seconds")

# Test operation with NumPy array
start_time = time.time()

result_array = numpy_array * 2

end_time = time.time()
numpy_time = end_time - start_time

print("Time taken by NumPy array:", numpy_time, "seconds")