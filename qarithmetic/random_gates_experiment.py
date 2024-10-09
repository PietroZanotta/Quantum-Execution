from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, mult
from numpy.random import uniform, choice
from sympy import symbols, Matrix, I, nsimplify, Rational
from sympy import init_printing, pretty_print
import re
import numpy as np
from qiskit.quantum_info import Operator
import itertools

def remove_small_elements(expr, threshold=1e-6):
    return expr.xreplace({x: 0 if abs(x) < threshold else x for x in expr.atoms() if x.is_number})

def random_selection():
    option_list = range(0, 2)
    operation = choice(option_list)

    operation = 0

    if operation == 0:
        # addition
        a = QuantumRegister(2)
        b = QuantumRegister(3)
        contr_reg = QuantumRegister(5) 
        cb = ClassicalRegister(3)
        qc = QuantumCircuit(a, b, cb)
        qc_with_cnot = QuantumCircuit(a, b, contr_reg)

        qc.barrier()

        # random H
        for i in range(0, int(uniform(0, 10))):
            tar = int(uniform(0,5))

            qc_with_cnot.h(tar)
            qc.h(tar)

        qc.barrier()

        # random cnot
        for i in range(0, int(uniform(0, 10))):
            contr = int(uniform(0, 5))
            tar = int(uniform(5, 10))
            
            qc_with_cnot.cx(contr, tar)
            # qc.cx(contr, tar)

        qc.barrier()
        print(qc_with_cnot)

        dummy_qc = QuantumCircuit(a, b)
        p = uniform()
        add(dummy_qc, a, b, 2)
        
        if p > 0.5:
            qc.append(dummy_qc, range(0,5))
            qc_with_cnot.append(dummy_qc, range(0,5))

            print("addition")
        else:
            qc.append(dummy_qc.inverse(), range(0,5))
            qc_with_cnot.append(dummy_qc.inverse(), range(0,5))

            print("inverse addition")

        matrix = Operator(qc).data
        matrix_with_cnot = Operator(qc_with_cnot).data

        binary_variables = [f'{i:05b}'[::-1] for i in range(2**(5))] 
        variables = symbols(binary_variables)

        binary_with_cnot = [f'{i:010b}'[::-1][:5] for i in range(2**10)]
        variables_with_cnot = symbols(binary_with_cnot)

        vector = Matrix(variables)
        M = Matrix(matrix)  
        result = M * vector

        vector_with_cnot = Matrix(variables_with_cnot)
        M_with_cnot = Matrix(matrix_with_cnot)  
        result_with_cnot = Matrix(M_with_cnot[:2**5, :]) * vector_with_cnot

        print("a")
        init_printing()
        result_simplified = result.applyfunc(lambda x: remove_small_elements(x))
        # pretty_print(result_simplified)

        print("b")

        result_with_cnot_simplified = result_with_cnot.applyfunc(lambda x: remove_small_elements(x))

        difference = result_simplified - Matrix(result_with_cnot_simplified[:2**5])

        # pretty_print(remove_small_elements(difference))

        is_equal = remove_small_elements(difference) == Matrix([0] * 32)

        # Output the result
        if is_equal:
            print("The vectors are equal.")
        else:
            print("The vectors are not equal.")
            print(qc)
            print(qc_with_cnot)

    if operation == 1:
        # multiplication
        a = QuantumRegister(2)
        b = QuantumRegister(2)
        m = QuantumRegister(3)
        qc = QuantumCircuit(a, b, m)
        contr_reg = QuantumRegister(4) 
        qc_with_cnot = QuantumCircuit(a, b, m, contr_reg)

        qc.barrier()

        # random H
        for i in range(0, int(uniform(0, 10))):
            tar = int(uniform(0,4))

            qc_with_cnot.h(tar)
            qc.h(tar)

        qc.barrier()

        # random cnot
        for i in range(0, int(uniform(0, 10))):
            contr = int(uniform(0, 4))
            tar = int(uniform(7, 11))
            
            qc_with_cnot.cx(contr, tar)

        qc.barrier()
        print(qc_with_cnot)


        dummy_qc = QuantumCircuit(a, b, m)
        
        mult(dummy_qc, a, b, m, 1)
        
        p = uniform()
        if p > 0.5:
            qc.append(dummy_qc, range(0,7))
            qc_with_cnot.append(dummy_qc, range(0,7))

            print("multiplication")
        else:
            qc.append(dummy_qc.inverse(), range(0,7))
            qc_with_cnot.append(dummy_qc.inverse(), range(0,7))

            print("inverse multiplication")

        matrix = Operator(qc).data
        matrix_with_cnot = Operator(qc_with_cnot).data

        binary_variables = [f'{i:07b}'[::-1] for i in range(2**(7))] 
        variables = symbols(binary_variables)

        binary_with_cnot = [f'{i:011b}'[::-1][:7] for i in range(2**11)]
        variables_with_cnot = symbols(binary_with_cnot)

        vector = Matrix(variables)
        M = Matrix(matrix)  
        result = M * vector

        vector_with_cnot = Matrix(variables_with_cnot)
        M_with_cnot = Matrix(matrix_with_cnot)  
        result_with_cnot = Matrix(M_with_cnot[:2**7, :]) * vector_with_cnot
        # result_with_cnot = result_with_cnot[:2**5]



        print("a")
        init_printing()
        result_simplified = result.applyfunc(lambda x: remove_small_elements(x))
        # pretty_print(result_simplified)

        print("b")

        result_with_cnot_simplified = result_with_cnot.applyfunc(lambda x: remove_small_elements(x))

        difference = result_simplified - Matrix(result_with_cnot_simplified[:2**7])

        # pretty_print(remove_small_elements(difference))

        is_equal = remove_small_elements(difference) == Matrix([0] * 2**7)

        # Output the result
        if is_equal:
            print("The vectors are equal.")
            # print(qc)
            print(qc_with_cnot)
        else:
            print("The vectors are not equal.")
            print(qc)
            print(qc_with_cnot)
    

random_selection()