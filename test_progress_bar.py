import time

def print_progressbar(total, current, barsize=60):
    progress = int(current*barsize/total)
    completed = str(int(current*100/total)) + '%'
    print('[', chr(9608)*progress, ' ', completed, '.'*(barsize-progress), '] ', str(current)+'/'+str(total), sep='', end='\r', flush=True)



total = 600
barsize = 60
print_frequency = max(min(total//barsize, 100), 1)
print("Start Task..", flush=True)
for i in range(1, total+1):
    time.sleep(0.0001)
    if i%print_frequency == 0 or i == 1:
        print_progressbar(total, i, barsize)
print("\nFinished", flush=True)



# here is a much simpler one
n = 25
for i in range(n):
    time.sleep(0.1)
    s = '.' * i
    print(s,  int(i/n*100), end='\r', flush=True)

# the format is
# print("some string that grows", end='\r', flush=True)

# even easier
n = 25
for i in range(n):
    time.sleep(0.1)
    print(f'running {i} of {n}', end='\r', flush=True)


