import time

start = time.time()
x = 1
for i in range(11000000):
    x += i

print(x)
end = time.time()
print("time: ", end-start)
