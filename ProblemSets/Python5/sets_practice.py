#!/usr/bin/env python3

mySet = {'3','14','15','9','26','5','35','9'}
mySet2 = {'60','22','14','0','9'}

print('intersection: ',mySet.intersection(mySet2))
print('difference: ',mySet.difference(mySet2))
print('union: ',mySet.union(mySet2))
print('symmetrical difference: ',mySet.symmetric_difference(mySet2))
