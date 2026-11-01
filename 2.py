import heapq

def huffman(character, frequency):
    heap=[]
    
    for i in range(len(character)):
        heap.append([frequency[i],character[i]])
        
    heapq.heapify(heap)   # converts into min-heap
    
    while len(heap)>1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = [left[0] + right[0], [left[1], right[1]]]
        heapq.heappush(heap,new_node)
        
    codes = {}
    
    def generate(node,code):
        if isinstance(node, str):
            codes[node]=code
        else:
            generate(node[0], code + "0")
            generate(node[1], code + "1")
            
    generate(heap[0][1],"")
    return codes

n= int(input("Enter the no of characters "))
character = []
frequency = []

for i in range(n):
    character.append(input("\nEnter the character "))
    frequency.append(int(input("\nEnter the frequency ")))

codes = huffman(character,frequency)

for ch in character:
    print(ch,":",codes[ch])