import time


n = 25
for i in range(n):
    time.sleep(0.1)
    progress = int(i / n * 50)
    print(f'running {i+1} of {n} {progress*"."}', end='\r', flush=True)


