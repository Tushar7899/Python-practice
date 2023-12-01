import os
import shutil

print(os.getcwd())

total ,used, free = shutil.disk_usage("/")
# The output gives in bytes
print("total disk space is :",total)
print("used disk space is :",used)
print("free disk space is :",free)

# The output get in gb but not shows in GB at last
print("total disk space is :",total // (2**30 ))
print("used disk space is :",used // (2**30))
print("free disk space is :",free // (2**30))

# This output get  in GB format and shows in last a a GB
print(f"total disk space is {total // (2**30)} GB")
print(f"total disk space is {used // (2**30)} GB")
print(f"total disk space is {free // (2**30)} GB")
