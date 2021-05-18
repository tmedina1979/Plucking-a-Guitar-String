import random

# this creates a class we want to represent as the ringbuffer
# create an empty array to initalize the buffer
# empty buffer created focus on fixing first and last and use that to insert elements and remove elements from last


class RingBuffer:
    # we initalize the ring buffer marking the first and last elements, the array with the random strings
    #number of elements in the array and a max capacity that is 10
    
    def __init__(self, first, last, plucklist, size):
        self.first = 0
        self.last = 0
        self.plucklist = []
        self.size = 0
        
    #create an empty buffer
    def createbuffer(self, capacity):
        self.plucklist = [0]*capacity
        return RingBuffer

    #check the size
    def checkSize(self):
        #returns length of array
        return self.size
    #check if array is empty
    def isEmpty(self):
        #returns bool
        if self.size == 0:
            return True 
        else:
            return False
    #check if array is at capacity
    def isFull(self,capacity):
        #returns bool
        if self.size == capacity:
            return True 
        else:
            return False
    #add element to the array
    def enqueue(self):
        #check if its full before you add; cannot add more after 10
        if self.isFull() == True:
            print("Buffer is full")
        #if its the first element you are putting in then make that self.last(last most inserted item)
        if self.isEmpty() == True:
            #adding a randomly plucked string
            x = '{0:.1f}'.format(random.uniform(-.5,.5))
            #add element to the back
            self.plucklist.insert(-1,)
            #new element is now self.last
            self.last = 0
        #else theres already another element and space to add a new one
        else:
            x = '{0:.1f}'.format(random.uniform(-.5,.5))
            self.plucklist.append(x)
            #the previous element becomes the least recently inserted
            self.first = 0
            #the new element becomes the most recently inserted
            self.last +=1
        self.size + 1
    # remove an element from the array
    def dequeue(self):
        if self.isEmpty():
            print('buffer is empty')
        else:
            x = self.plucklist.pop(self.first)
            self.last -=1
            self.size - 1
            return x
    #look at the first element
    def peek(self):
        return self.plucklist[self.first]


'''
ringbuffer initalizes array to 0's
guitar class function adds values to these 0's and first and last keeps track of where the array begins and ends
and the size but making sure that it never exceeds capacity

'''

class GuitarString(RingBuffer):
    def __init__(self, freq, size, plucklist):
        self.freq = 44_100
        self.size = size
        self.notes = plucklist
    
    def pluck():
        pass
    def tic():
        pass
    def sample():
        pass
    def time():
        pass




def main():
    capacity = 10
    nb = RingBuffer.createbuffer(nb, capacity)
    nb.createbuffer(capacity)
    print(nb.plucklist)










if __name__ == "__main__":
    main()