import numpy as np

# https://en.wikipedia.org/wiki/Machine_epsilon#Values_for_standard_hardware_arithmetics

def compute_epsilon(type_caster):
    epsilon = type_caster(1)
    while True:
        if epsilon + type_caster(1) <= type_caster(1):
            break
        epsilon = type_caster(epsilon/2)
    return 2*epsilon

type_names = {
    'float16(half)':np.half,
    'float32(single)':np.single,
    'float64(double)':np.double,
    'float80(longdouble)':np.longdouble,
}

print('computing machine epsilons...')
for type_name, type_caster in type_names.items():
    epsilon = compute_epsilon(type_caster)
    print(f'  for type {type_name}) = {epsilon}')
