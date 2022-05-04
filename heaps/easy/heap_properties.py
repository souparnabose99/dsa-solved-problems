

def is_min_heap(heap):
    # No need to check for leaf nodes: 2*i +2<= N, N = i-2/2
    num_of_items = (len(heap) - 2) // 2
    for i in range(num_of_items):
        # Check heap property: Parent should be smaller than children for min heap
        if heap[i] > heap[2*i + 1] or heap[i] > heap[2*i + 2]:
            return False
    return True


hp = [1, 2, 3, 4, 5]
print(is_min_heap(hp))


