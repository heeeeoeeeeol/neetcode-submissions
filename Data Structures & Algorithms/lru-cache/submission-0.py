class Node:
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.recent = Node()
        self.oldest = Node(prev = self.recent)
        self.recent.next = self.oldest
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        
        n = self.d[key]
        n.next.prev = n.prev
        n.prev.next = n.next
        n.next = self.recent.next
        n.prev = self.recent
        self.recent.next = n      
        n.next.prev = n
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            n = self.d[key]
            n.val = value
            n.next.prev = n.prev
            n.prev.next = n.next
            n.next = self.recent.next
            n.prev = self.recent
            self.recent.next = n
            n.next.prev = n

        else:
            tmp = Node(key, value, self.recent.next, self.recent)
            tmp.next.prev = tmp
            self.recent.next = tmp
            self.d[key] = tmp

            if len(self.d) > self.cap:
                del self.d[self.oldest.prev.key]
                self.oldest.prev = self.oldest.prev.prev
                self.oldest.prev.next = self.oldest



        
