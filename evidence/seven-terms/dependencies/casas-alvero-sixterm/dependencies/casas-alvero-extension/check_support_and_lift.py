#!/usr/bin/env python3
"""Exact support filter and finite indexing checks for the structural note.

Only finite arithmetic is verified here. The all-e valuation/Lucas argument
and the cited CLO theorem remain written mathematical dependencies.
"""
from itertools import product, combinations
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
    expected_rows = {
        2: [4,16], 3: [2,9,10,11,18,19],
        5: [5,10,15], 17: [2,3,17,18,19], 19: [19],
    }
    rows = {p:[m for m in range(2,20) if comb(20,m)%p] for p in expected_rows}
    if rows != expected_rows:
        raise ValueError('Binomial support row differs')
    if any(comb(20,19)%p == 1 for p in (3,17)):
        raise ValueError('Singleton coefficient obstruction failed')
    required = [{19},{4,16},{5,10,15},{2,3,17,18}]
    if sum(map(len,required)) != len(set.union(*required)):
        raise ValueError('Four required sets are not disjoint')
    expected_table = {
        (2,4,5):5, (4,5,18):17, (2,4,10):1, (3,4,10):1,
        (4,10,17):0, (4,10,18):7, (2,4,15):17, (4,15,18):3,
        (2,5,16):13, (5,16,18):12, (2,10,16):18, (3,10,16):14,
        (10,16,17):11, (10,16,18):2, (2,15,16):9, (15,16,18):2,
    }
    records=[]
    for a,b,c in product((4,16),(5,10,15),(2,3,17,18)):
        support=sorted((a,b,c,19))
        if not set(support)&{2,9,10,11,18}:
            continue
        missing=[j for j in range(2,19) if j not in support]
        matrix=matrix_for_missing_coefficients(missing)
        det=determinant_integer(matrix)
        residue=determinant_mod(matrix,19)
        if det%19!=residue or expected_table[tuple(support[:-1])]!=residue:
            raise ValueError('Determinant/table mismatch')
        records.append({'support':support,'determinant':det,'residue_mod19':residue})
    if len(records)!=16 or [r['support'] for r in records if r['residue_mod19']==0]!=[[4,10,17,19]]:
        raise ValueError('Final support filter differs')
    fixture=[list(js) for js in combinations(range(2,11),2)
             if determinant_mod(matrix_for_missing_coefficients(js),11)==0]
    if fixture!=[[3,8],[5,6],[6,8],[6,9],[7,9]]:
        raise ValueError('CLO degree-12 indexing fixture failed')
    J=[1,2,3,5,6,7,13,14,15,16,18]
    K=sorted(20-j for j in J)
    visible=[j for j in range(1,20) if comb(20,j)%13]
    if sorted(set(visible)-{4,17,19})!=J:
        raise ValueError('Structural mask differs')
    forbidden=sorted(set(range(2,20))-set(J))
    if forbidden!=[4,8,9,10,11,12,17,19]:
        raise ValueError('Centered complement differs')
    examples=[]
    for e in (0,1,2):
        q=13**e; n=20*q
        actual=[r for r in range(1,n) if comb(n,r)%13]
        if actual!=[q*j for j in visible]:
            raise ValueError('Lucas finite-example indexing failed')
        for degree in (20,16,3,1):
            for k in range(1,degree+1):
                if comb(q*degree,q*k)%13!=comb(degree,k)%13:
                    raise ValueError('Hasse-Frobenius finite-example identity failed')
        examples.append({'e':e,'q':q,'degree':n,'required_indices':[q*j for j in J],
                         'derivative_orders':[q*k for k in K]})
    print(json.dumps({'status':'PASS','prime_rows':rows,'support_count':16,
        'records':records,'remaining_support':[4,10,17,19],
        'published_degree12_fixture':fixture,'J':J,'K':K,
        'forbidden_centered_mask':forbidden,'lucas_examples':examples,
        'scope':'Finite binomial rows, determinants, and examples e=0,1,2; all-e transfer is proved symbolically in PROOF.md.'},indent=2))

if __name__=='__main__':
    main()
