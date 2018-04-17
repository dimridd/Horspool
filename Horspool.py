#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 02:44:27 2018

@author: divyanshu
"""

#%%

table = [0]*256
rest = []
sigma = "ACGT"

def bc1(pat, m):
	for i in range(len(table)):
		table[i] = m
	
	for i in range(m):
		pre = table[ord(pat[i])-65]
		table[ord(pat[i])-65] = m-i-1;
		if table[ord(pat[i])-65] == 0:
			table[ord(pat[i])-65] = pre
			
	return table	

text = "GCATCGCAGAGAGTATACAGTACG"
pat = "GCAGAGAG"
#bc = bc1(pat.upper(), len(pat))

def cmp(pat, text, j, m):
	count = 0
	for i in range(m):
		if pat[i] == text[i+j]:
			count += 1
	
	if count == m:
		return 1
	else:
		return 0

def horspool(pat, m, text, n):
	j = 0
	bc = bc1(pat.upper(), len(pat))
	c = 0
	matches = 0
	
	while j <= n-m:
		
		c = text[j+m-1]
		if pat[m-1] == c and cmp(pat, text, j, m-1):
			matches += 1
			
		
		j += bc[ord(c)-65]
		
	return matches

def main():
	text = "GCATCGCAGAGAGTATACAGTACG"
	pat = "GCAGAGAG"
	#sigma = "ACGT"
	
	print(horspool(pat, len(pat), text, len(text)))

if __name__ == '__main__':
	main()	
	