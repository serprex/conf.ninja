#!/usr/bin/python
def main():
	from subprocess import call
	from tempfile import NamedTemporaryFile
	conf=open("conf.ninja")
	build=open("build.ninja","w")
	fl=conf.readline()
	if fl[:2]=="#!":s=fl[2:].split()
	else:
		s=["python"]
		conf.seek(0)
	for l in conf:
		if l=="%\n":
			x=[]
			for l in conf:
				if l=="%\n":break
				x+=l,
			build.flush()
			i=NamedTemporaryFile("w")
			i.write("".join(x))
			i.flush()
			call(s+[i.name],stdout=build)
		elif l[0]=="!":
			build.flush()
			call(l[1:-1].split(),stdout=build)
		else:build.write(l)
	build.write("\n")
	build.close()
	call("ninja")
main()