import time
import tracemalloc

N = 1_000_000

# List processing
tracemalloc.start()
start = time.time()

data = [x * 2 for x in range(N)]

list_time = time.time() - start
list_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()


# Generator processing
tracemalloc.start()
start = time.time()

data = (x * 2 for x in range(N))
for x in data:
    pass

gen_time = time.time() - start
gen_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("List:", list_time, "seconds,", list_memory, "bytes")
print("Generator:", gen_time, "seconds,", gen_memory, "bytes")
