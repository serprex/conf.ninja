#!/usr/bin/python
def main():
	import sys, re, itertools
	expr=re.compile(r"{\$.*?\$}")
	conf=open("conf.ninja")
	sys.stdout=build=open("build.ninja","w")
	for l in conf:
		if l=="{\n":
			exec("".join(itertools.takewhile(lambda x:x!="}\n", conf)))
		else:
			for start,end in reversed([m.span() for m in expr.finditer(l)]):
				if l[start+2]=="$":l=l[:start+2]+l[start+3:]
				else:l=l[:start]+eval(l[start+2:end-2])+l[end:]
			build.write(l)
	build.write("\n")
main()