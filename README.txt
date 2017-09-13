Modelo de entrada
	python main.py entrada.txt "SS|IS|HS|MS|QS|CS|RS" > saida.txt
onde:
	SS - Selection sort
	IS - Insertion sort
	HS - Heap sort
	MS - Merge sort
	QS - Quick sort
	CS - Counting sort
	RS - Radix sort

Exemplo: python main.py entrada.txt IS > saida.txt


Para executar o Teste:
	Sistema utilizado no teste, disponível em resultados/
	- Intel core i5 2.4Ghz
	- 8GB 1.600 MHz RAM
	- 240GB SSD FURY Kingston
	OBS: Uso da CPU ficou limitado a 25%.
	Exemplo: 
		python measureTime.py instancias-num/num.1000.1.in
		python measureTime.py instancias-num/num.10000.2.in
		python measureTime.py instancias-num/num.100000.1.in
	
OBS: python 2.7