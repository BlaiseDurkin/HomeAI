
import numpy as np
import matplotlib.pyplot as plt

"""
 --- test script ---

TODO
 - incorporate into system

"""

#assume signal 1 or 0

sig = [0,0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
indices = [i for i in range(len(sig)) ]
accum_sig = []
total = 0

threshold = 2.5
max_val = 2*threshold


def sig_val(sig):
    val = 1
    if sig == 0:
        val = -1
    return val


for i in range(len(sig)):
    val = sig_val(sig[i])
    accum_sig.append(min(max_val, max( (total + val), 0)))
    if total <= 0:
        total += max(val, 0)
    else:
        total += val
print(sig)
print(accum_sig)

plt.figure(figsize=(14, 8))
plt.plot(indices, sig,
         color='tab:blue', linewidth=3, linestyle='-', label='signal')
plt.plot(indices, accum_sig,
         color='tab:orange', linewidth=3, linestyle='-', label='processed signal')
plt.axhline(y=threshold, color='black', linestyle='--', linewidth=1.5, alpha=0.7,
            label='threshold')
plt.title('signal', fontsize=15)
plt.xlabel('time')
plt.ylabel('signal')
plt.grid(True, alpha=0.25)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()