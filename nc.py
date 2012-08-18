#!/usr/bin/python
def main():
	import ninja_syntax
	import sys
	conf=open("conf.ninja")
	sys.stdout=build=open("build.ninja","w")
	for l in conf:
		if l=="%\n":
			x=""
			for l in conf:
				if l=="%\n":break
				x+=l
			exec(x)
		else:build.write(l)
	build.write("\n")
main()