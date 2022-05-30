all: kc2.pdf kc.pdf

kc.pdf: kc.py
	python3 kc.py

kc2.pdf: kc2.py ../pynomo/*.py
	echo compiling kc2
	python3 kc2.py
