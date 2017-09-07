def buildheap(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end:
      break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
      
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

def heapsort(lst):
  for start in range((len(lst)-2)/2, -1, -1):
    buildheap(lst, start, len(lst)-1)

  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    buildheap(lst, 0, end - 1)
  return lst

#v = vector_random(20,-100,100)
#print v
#inicio = time.time()
#heapsort(v)
#fim = time.time()
#print "Tempo de execucao: %.10f"%(fim-inicio)
#print v
