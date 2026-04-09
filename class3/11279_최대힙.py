import sys


class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)

    def delete(self):
        # 힙에 원소가 없으면, 여기선 0을 출력하기로한다.
        if len(self.heap) <= 1:
            return 0
        
        # 최댓값을 저장 -> 끝노드랑 교체 -> 끝노드 제거
        val = self.heap[1]
        self.heap[1] = self.heap[len(self.heap)-1] 
        self.heap.pop()

        # 힙에 원소가 있으면 힙속성 유지
        if len(self.heap) > 1:
            self._heapify_down(1)
        
        return val
    
    def _heapify_up(self, idx): # idx빼고 멀쩡한 노드에서, idx를 제자리 찾게해주는 함수
        while idx > 1: # 부모 노드가 없을 때까지
            parent_idx = idx//2
            
            if self.heap[parent_idx] < self.heap[idx]: # 부모가 더 작으면 문제가 있는 것.
                self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break # idx가 자리를 찾았으므로 종료

    def _heapify_down(self, idx):
        while 2*idx < len(self.heap): # 자식노드가 말단 전에 존재하는경우
            left_idx = 2*idx
            right_idx = 2*idx + 1

            # 두 자식 중 더 큰 인덱스를 찾음
            if right_idx < len(self.heap) and self.heap[left_idx] < self.heap[right_idx]:
                l_idx = right_idx
            else:
                l_idx = left_idx

            # 더 큰 자식보다, 현재 노드가 더 작으면 스왑
            if self.heap[l_idx] > self.heap[idx]:
                self.heap[l_idx], self.heap[idx] = self.heap[idx], self.heap[l_idx]
                idx = l_idx
            else:
                break

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().rstrip())
    maxheap = MaxHeap()
    for _ in range(N):
        num = int(input().rstrip())

        if num == 0:
            result = maxheap.delete()
            print(result)
        else:
            maxheap.insert(num)



