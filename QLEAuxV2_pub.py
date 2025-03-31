import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import MCXGate, MCPhaseGate

def make_TMZ(TruthModels=("00",), KBname='KB', theta=np.pi):

    NTrues = len(TruthModels)

    assert NTrues >= 1, "KB must have at least one logical model/true case."
    
    # Number of input symbols
    n = len(TruthModels[0])

    assert NTrues <= 2**n, f"{NTrues=}; {n=}"
    
    # Create a N-controlled Toffoli gate
    mcrz_gate = MCPhaseGate(theta, n)
    
    # Make the KB
    KB = QuantumCircuit(n+1, name=KBname)

    syms = [i for i in range(n+1)]

    for TCase in TruthModels:
        
        # Make controlled pattern
        for i,t in enumerate(TCase):
            if t == '0':
                KB.x(n-1 - i)

        # Add the cx gate
        KB.append(mcrz_gate, syms)

        # Get back the original input
        for i,t in enumerate(TCase):
            if t == '0':
                KB.x(n-1 - i)
    # end for TCase
    
    KB.to_gate() 
    
    return KB

def make_TM(TruthModels=("00",), KBname='KB'):

    NTrues = len(TruthModels)

    assert NTrues >= 1, "KB must have at least one logical model/true case."
    
    # Number of input symbols
    n = len(TruthModels[0])

    assert NTrues < 2**n, f"{NTrues=}; {n=}"
    
    # Create a N-controlled Toffoli gate
    mcx_gate = MCXGate(n)
    
    # Make the KB
    KB = QuantumCircuit(n+1, name=KBname)

    syms = [i for i in range(n+1)]

    for TCase in TruthModels:
        # Make controlled pattern
        for i,t in enumerate(TCase):
            if t == '0':
                KB.x(n-1 - i)

        # Add the cx gate
        KB.append(mcx_gate, syms)

        # Get back the original input
        for i,t in enumerate(TCase):
            if t == '0':
                KB.x(n-1 - i)
    # end for TCase
    
    KB.to_gate() # Make a gate named 'oracle'
    
    return KB


def grouping(all_counts, glist=['01 00', '01 01', '01 10', '01 11'], exclude=False):
    '''
    * group everything in glist when exclude=False
    * group everything NOT in glist when exclude=True
    '''
    g = []
    if not exclude:
        for k in glist:
            g += all_counts[k]
    else:
        for k in all_counts:
            if k in glist:
                continue

            g += all_counts[k]
    
    return g


def combi(MPicks=2, items=["00", "01", "10", "11"]):
    '''
    Get the all combinations of items.
    '''

    cres = [[]]
    for p in range(MPicks):
        # print(p)

        ctmp = []
        for it in items:

            cc = []            
            # print(f'{it=}; {cres=}')
            for jt in cres:
                # print(f'* {jt=}')
                if it in jt:
                    continue
                    
                nit = [it] + jt
                nit.sort()
                
                if nit in ctmp:
                    continue
                    
                cc.append(nit)
                # print('cc =', cc)
            ctmp.extend(cc)
            # print('ctmp =', ctmp)            
        cres = ctmp
        # print()

    return cres



def collectByState(count_list):
    '''
    count_list : a list of count result, where count result is a dict.
                 The dict has eigenstates as keys.
    Return: dict, whose keys are eigenstates and values are combined counts from every repeats.
    '''

    StateCount = {}
    for i, co in enumerate(count_list):
        # Debug
        # print(i, co.keys())

        # Traverse keys of each count result
        for k in co:
            if k in StateCount:
                StateCount[k] += [co[k]]
            else:
                StateCount[k] = [co[k]]
        
    # end for i, co
    return StateCount
