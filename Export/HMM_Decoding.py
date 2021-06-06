import numpy as np


pi = np.array([0.5,0.5])
# a_ij = a[i,j]
a = np.array([[0.7, 0.3],[0.1, 0.9]])
# b_i(o_j) = b[i,j]
b = np.array([[0.05, 0.15, 0.80],[0.75, 0.15, 0.10]])
states = ['hot','cold']
observations = ['1 solo', '2 solos', '3 solos']

input_seq = [2,2,0]

T = len(input_seq)
N = len(pi)

# Initialisation
delta = [[pi[i]*b[i,input_seq[0]] for i in range(N)]]
psi = [['' for i in range(N)]]
print('\n'.join([f'delta_1({states[i]:s}) = {delta[0][i]}' for i in range(N)]))
print('psi_1(i) = 0 \n')

# Induction
for t in range(T-1):
    temp_delta = []
    temp_psi = []
    for i in range(N):
        delta_a = [delta[t][j]*a[j,i] for j in range(N)]
        s = np.max(delta_a)
        bi = b[i,input_seq[t+1]]
        temp_psi.append(np.argmax(delta_a))
        temp_delta.append(s*bi)
        print(f'delta_{t+2:d}({states[i]:s}) = {temp_delta[i]:.7g}')
        print(f'psi_{t+2:d}({states[i]:s}) = {states[temp_psi[i]]:s}\n')
    delta.append(temp_delta)
    psi.append(temp_psi)

# Termination
q = []
P_best = np.max(delta[T-1])
q = np.argmax(delta[T-1])
print(f'q*_{T} = {states[q]}\n')

qs = [0 for i in range(T)]
qs[-1] = q
for t in range(T-2,-1,-1):
    qs[t] = psi[t+1][qs[t+1]]
    print(f'q*_{t+1} = psi_{t+2}({states[qs[t+1]]:s}) = {states[qs[t]]:s}')

print(f'\nMost probable sequence will be ' + ','.join([states[i] for i in qs]))
print(f'P_best = {P_best}')


