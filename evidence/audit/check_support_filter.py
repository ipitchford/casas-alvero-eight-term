#!/usr/bin/env python3
"""Instantiate Castryck--Laterveer--Ounaies Theorem 2 in degree 20.

Conditional on that theorem and Proposition 15, a centered nontrivial CA
polynomial with exactly three nonleading nonzero coefficients must have
support (5,16,19). This code does NOT exclude that last triple.
"""
from itertools import combinations
from math import comb
import json


def determinant_integer(matrix):
    a = [r[:] for r in matrix]
    sign, previous = 1, 1
    for k in range(len(a)-1):
        pivot = next((j for j in range(k,len(a)) if a[j][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[pivot],a[k] = a[k],a[pivot]
            sign = -sign
        q = a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                numerator = q*a[i][j]-a[i][k]*a[k][j]
                if numerator % previous:
                    raise ValueError('Bareiss nonexact division')
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = q
    return sign*a[-1][-1]


def determinant_mod(matrix,p):
    a = [[v%p for v in row] for row in matrix]
    result = 1
    for k in range(len(a)):
        pivot = next((j for j in range(k,len(a)) if a[j][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[pivot],a[k] = a[k],a[pivot]
            result = -result
        q = a[k][k]
        result = result*q%p
        for i in range(k+1,len(a)):
            c = a[i][k]*pow(q,-1,p)%p
            a[i] = [(x-c*y)%p for x,y in zip(a[i],a[k])]
    return result%p


def matrix_for_missing_coefficients(js):
    # Source: Theorem 2, displayed matrix (2). The indices are coefficient
    # positions j with f^(d-j)(0)=0, NOT the nonzero support positions.
    return [[-1]+[j*comb(j-2,k-2) if k<=j else 0 for k in js] for j in js] + [
            [-1]+[(-1)**j for j in js]]


def main():
    records=[]
    for a,b in combinations(range(2,19),2):
        js=[j for j in range(2,19) if j not in (a,b)]
        matrix=matrix_for_missing_coefficients(js)
        det=determinant_integer(matrix)
        residue=determinant_mod(matrix,19)
        if det%19 != residue:
            raise ValueError('independent determinant algorithms disagree')
        records.append({'support':[a,b,19],'vanishing_indices':js,
                        'determinant':det,'mod19':residue})
    survivors=[r['support'] for r in records if r['mod19']==0]
    expected=[[4,17,19],[5,16,19],[10,11,19],[10,12,19]]
    if survivors != expected:
        raise ValueError('surviving-support identity mismatch')
    prime_power_allowed=[r for r in records
                         if set(r['support']) & {4,16}
                         and set(r['support']) & {5,10,15}]
    final=[r['support'] for r in prime_power_allowed if r['mod19']==0]
    if len(prime_power_allowed)!=6 or final!=[[5,16,19]]:
        raise ValueError('prime-power pruning mismatch')
    # Reproduce the five explicit degree-12 two-index examples printed
    # immediately after Theorem 2, checking indexing against a source fixture.
    degree12=[list(js) for js in combinations(range(2,11),2)
              if determinant_mod(matrix_for_missing_coefficients(js),11)==0]
    if degree12!=[[3,8],[5,6],[6,8],[6,9],[7,9]]:
        raise ValueError('published degree-12 fixture mismatch')
    print(json.dumps({'status':'PASS','source':'https://arxiv.org/html/1208.5404#S1.Thm2',
                      'dependency':'Castryck-Laterveer-Ounaies Theorem 2 and Proposition 15',
                      'unfiltered_support_count':comb(18,3),
                      'supports_after_simple_mean_root_condition':len(records),
                      'excluded_by_determinant':len(records)-len(survivors),
                      'determinant_survivors':survivors,
                      'six_prime_power_allowed':prime_power_allowed,
                      'final_survivors':final,'published_degree12_fixture':degree12,
                      'records':records},indent=2))


if __name__=='__main__':
    main()
