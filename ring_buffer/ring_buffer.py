class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.oldest_value_index = 0 

    def append(self, item):
        ring_length = len(self.ring)
        if ring_length == self.capacity: 
            self.ring[self.oldest_value_index] = item
            if self.oldest_value_index + 1 == self.capacity: 
                self.oldest_value_index = 0
            else: 
                self.oldest_value_index += 1
        else: 
            self.ring.append(item)
 
    def get(self):
        return self.ring