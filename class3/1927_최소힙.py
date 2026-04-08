import sys

##### 클래스 기반 구현 #####
class MinHeap:
    def __init__(self):
        self.heap = [0] # 1-based indexing을 위해 더미 데이터 삽입

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1) # 방금 삽입한 자리부터, 처음까지 훑어보며 힙 속성을 복구

    def delete(self):
        if len(self.heap) <= 1:
            return 0 # 힙에 원소가 없다면 0을 출력
        
        # 최솟값 저장 -> 자리 바꾸기 -> 끝 노드 삭제
        val = self.heap[1]
        self.heap[1] = self.heap[len(self.heap)-1]
        self.heap.pop()

        # 이제 힙처럼 만들어야하는데, 더미 데이터만 있으면 할 필요 x
        if len(self.heap) > 1:
            self._heapify_down(1) # 처음부터 시작해, 아래로 가면 힙속성 복구 (왜 down은 1에서 시작해야하는지?)

        return val

    def _heapify_up(self, idx):
        """삽입된 노드를 올바른 위치로 끌어올립니다."""
        while idx > 1:
            parent_idx = idx//2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx] # swap
                idx = parent_idx
            else:
                break

    def _heapify_down(self, idx):
        """루트에서부터 자식들을 비교하며 올바른 위치로 끌어내립니다."""
        while 2*idx < len(self.heap):
            left_idx = 2*idx
            right_idx = 2*idx+1

            # 더 작은 자식을 찾음
            if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[left_idx]: # 오른 자식이 존재하여 더 작음
                s_idx = right_idx
            else:
                s_idx = left_idx
            
            # 더 작은 자식보다, 현재노드가 더 크면 스왑
            if self.heap[idx] > self.heap[s_idx]: 
                self.heap[idx], self.heap[s_idx] = self.heap[s_idx], self.heap[idx]
                idx = s_idx
            else:
                break

if __name__ == "__main__":
    input = sys.stdin.readline 

    N = int(input().rstrip())
    min_heap = MinHeap()

    for _ in range(N):
        num = int(input().rstrip())

        if num == 0:
            val = min_heap.delete()
            print(val)
        else:
            min_heap.insert(num)

