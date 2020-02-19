#!/usr/bin/python3
# coding: utf-8
import subprocess

def main(data1):
	target = data1
	cmd = ["./xray","subdomain","--target",target,"--text-output","output_"+target+".txt"]
	rsp=subprocess.check_output(cmd)
	print(rsp)


if __name__=='__main__':
	file = open("subdomain.txt")
	for text in file.readlines():
		data1=text.strip('\n')
		main(data1)