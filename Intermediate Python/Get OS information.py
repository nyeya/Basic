import os,platform,time
reader = "Platform: {} {} \nArchitecture: {} \nProcessor: {} processor"
print(reader.format(platform.system(),platform.release(),platform.architecture()[0],platform.machine()))
