import squid
import numpy as np
import time
import sys

squid.mchrom.init()

start = float(input("Start: "))
end = float(input("End: "))
step = float(input("Step: "))
no_samples = int(input("No. of Samples: "))
file_name = str(input("File Name: "))

angles = np.array(np.arange(start, end+step, step))
print(angles)

with open(file_name, "a") as file:

    inst = squid.open_instrument(squid.CONFIG)
    squid.initialise_instrument(inst)

    for i in angles:

        squid.mchrom.goTo(i)
        time.sleep(0.5)

        timestamps, values = squid.acquire(inst, no_samples, squid.CONFIG["delay"])

        if not values:
            print("[ERROR] No data collected. Nothing saved.")
            sys.exit(1)

        arr = np.array(values)

        string = str(i) + "," + str(np.mean(arr)) + "," +  str(np.std(arr)) +"\n"

        file.write(string)
        file.flush()