import numpy as np
import matplotlib.pyplot as plt


def sampling_from_poisson(number, para_lambda):
    samples = []
    sample_counter = 0
    while(sample_counter < number):
        cdf_input = np.random.random()
        sample = np.divide(np.log(1 - cdf_input), -para_lambda)
        print(sample)
        samples.append(sample)
        sample_counter = sample_counter + 1
    return samples


samples = sampling_from_poisson(40, 5)
arrive_times = [0]
for i in range(len(samples)):
    arrive_times.append(samples[i]+arrive_times[-1])

x = np.arange(1, 42,1)
plt.plot(x, arrive_times)
plt.yticks([1,2,3,4,5,6,7,8,9,10])
#plt.show()



