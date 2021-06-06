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
alpha = [[pi[i]*b[i,input_seq[0]] for i in range(N)]]
psi = [['' for i in range(N)]]

# Induction
for t in range(T-1):
    temp_alpha = []
    temp_psi = []
    for i in range(N):
        alpha_a = [alpha[t][j]*a[j,i] for j in range(N)]
        s = np.max(alpha_a)
        bi = b[i,input_seq[t+1]]
        temp_psi.append(np.argmax(alpha_a))
        temp_alpha.append(s*bi)
    alpha.append(temp_alpha)
    psi.append(temp_psi)

# Termination
q = []
P_best = np.max(alpha[T-1])
q = np.argmax(alpha[T-1])

qs = [0 for i in range(T)]
qs[-1] = q
for t in range(T-2,-1,-1):
    qs[t] = psi[t+1][qs[t+1]]

print(f'\nMost probable sequence will be ' + ','.join([states[i] for i in qs]))
print(f'P_best = {P_best}')


