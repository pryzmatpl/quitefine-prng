import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Python function to call the PRNG C++ program and collect outputs
def generate_prng_outputs(executable_path, rounds, upper_bound, iterations=1000000):
    results = []
    
    for _ in range(iterations):        
        process = subprocess.Popen(
            [executable_path, str(rounds), str(upper_bound)], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
            text=True
        )
        stdout, stderr = process.communicate()
                
        for line in stdout.splitlines():
            if "Resulting preSeed" in line:
                # Extract the number after "Resulting preSeed: "
                try:
                    result = int(line.split()[-1])
                    results.append(result)
                except ValueError:
                    continue
    
    return results

executable_path = "./rand"  
rounds = 5
upper_bound = 10

prng_outputs = generate_prng_outputs(executable_path, rounds, upper_bound)

# Plot a histogram of the PRNG outputs
plt.figure(figsize=(10, 6))
plt.hist(prng_outputs, bins=np.arange(upper_bound + 1) - 0.5, edgecolor='black', density=True)
plt.title("Histogram of PRNG Outputs")
plt.xlabel("Output Value")
plt.ylabel("Frequency")
plt.xticks(range(upper_bound))

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
