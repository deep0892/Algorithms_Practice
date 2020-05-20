# https://leetcode.com/discuss/interview-question/542597/
"""
Discription of question in above link
"""
from collections import Counter
import re
import heapq

class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
def topKFrequent(k, keywords, reviews):
    word_list = []
    
    for review in reviews:
        review = re.sub('[^a-z ]', '', review.lower())
        word_list += set(review.split())
    count = Counter(word_list)
    
    heap = []
    
    for word, freq in count.items():
        if word in keywords:
            heapq.heappush(heap, Element(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
    
    return [heapq.heappop(heap).word for _ in range(k)][::-1]

def main():
    k = 2
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
    ]
    
    print(topKFrequent(k, keywords, reviews))


if __name__ == "__main__":
    main()
