#!/usr/bin/env python3

# iterate through each element in seq_list with `for` loop
# print length and sequence for each element

seq_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seq_list:
	print(f"{seq_list.index(seq)} \t {len(seq)} \t {seq}") 

