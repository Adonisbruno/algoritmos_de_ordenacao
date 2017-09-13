def quickSort(vet):
   quickSortHelper(vet,0,len(vet)-1)
   return vet

def quickSortHelper(vet, first, last):
   if first < last:
       splitpoint = partition(vet, first, last)
       quickSortHelper(vet, first, splitpoint-1)
       quickSortHelper(vet, splitpoint+1, last)

def partition(vet, first, last):
   pivor = vet[first]
   left = first+1
   right = last
   done = False
   while not done:
       while left <= right and vet[left] <= pivor:
           left = left + 1
       while vet[right] >= pivor and right >= left:
           right = right - 1
       if right < left:
           done = True
       else:
           temp = vet[left]
           vet[left] = vet[right]
           vet[right] = temp

   temp = vet[first]
   vet[first] = vet[right]
   vet[right] = temp

   return right

