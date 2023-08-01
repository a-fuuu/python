'''
Deque(Deck) 자료구조는 doulbe-ended한 성질을 갖고있어
양쪽 끝에 있는 element를 insert하거나 delete할 수 있다.
python에서는 built-in deque 자료구조를 갖고 있다 - collections deque 
'''
from collections import deque

my_deque = deque()

# element를 끝에 삽입
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# element를 맨 앞에 삽입
my_deque.appendleft(0)
my_deque.appendleft(-1)

# 끝에 있는 element를 제거
my_deque.pop()

# 맨 앞에 있는 element를 제거
my_deque.popleft()


'''
우선순위 큐는 element 삽입 시에 우선순위를 부여할 수 있다.
해당 우선순위를 바탕으로 높은 우선순위에 해당하는 element를 
효율적으로 검색할 수 있다. python에는 우선순위 큐 관련 built-in function은 없으나
heapq 모듈을 사용할 수 있다. 
'''

import heapq

my_priority_queue = []

heapq.heappush(my_priority_queue, (3, 'Task C'))
heapq.heappush(my_priority_queue, (1, 'Task A'))
heapq.heappush(my_priority_queue, (2, 'Task B'))

highest_priority_task = heapq.heappop(my_priority_queue) # priority가 가장 높은(1) Task A가 나온다.

print(highest_priority_task)