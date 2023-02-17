import time
for i in range(0,101):
    status = i*"#" + (100-i)*"-" 
    print(f"\r{status} {i}%", end="")
    time.sleep(0.1)