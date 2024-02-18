# Python implementation of above algorithm
from typing import List
def pageFaults_LRU(pages: List[int], n: int, capacity: int):

    # To represent set of current pages. We use
    # an unordered_set so that we quickly check
    # if a page is present in set or not
    s = set()

    # To store least recently used indexes
    # of pages.
    indexes = {}

    # Start from initial page
    page_faults: int = 0
    page_hits: int = 0
    for i in range(n):

        # Check if the set can hold more pages
        if len(s) < capacity:

            # Insert it into set if not present
            # already which represents page fault
            if pages[i] not in s:
                s.add(pages[i])

                # increment page fault
                page_faults += 1

            # Store the recently used index of
            # each page
            indexes[pages[i]] = i

            # If the set is full then need to perform lru
        # i.e. remove the least recently used page
        # and insert the current page
        else:

            # Check if current page is not already
            # present in the set
            if pages[i] not in s:

                # Find the least recently used pages
                # that is present in the set
                lru = float('inf')
                for page in s:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        val = page

                # Remove the indexes page
                s.remove(val)

                # insert the current page
                s.add(pages[i])

                # increment page fault
                page_faults += 1

            elif pages[i] in s:
                page_hits += 1

            # Update the current page index
            indexes[pages[i]] = i

    return page_faults, page_hits

from typing import Any
# Python program to illustrate
# page faults in LRU

# Counts no. of page faults
def pageFaults(n, c, pages):

    # Initialise count to 0
    count = 0
    hits = 0
    # To store elements in memory of size c
    v = []

    # Iterate through all elements of pages
    for i in range(n):

        # Find if element is present in memory or not
        if pages[i] not in v:

            # If memory is full
            if len(v) == c:

                # Remove the first element
                # As it is least recently used
                v.pop(0)

            # Add the recent element into memory
            v.append(pages[i])

            # Increment the count
            count += 1
        else:

            # If element is present
            # Remove the element
            # And add it at the end as it is
            # the most recent element
            v.remove(pages[i])
            v.append(pages[i])
            hits += 1

    # Return total page faults
    return count, hits

class LRU:
    def __init__(self, page_frames):
        self.page_frames = page_frames
        self.page_dict = {}  # Use a dictionary for efficient access and updates
        self.page_faults = 0
        self.page_hits = 0

    def access(self, page):
        if page in self.page_dict:
            self.page_hits += 1
            self.update_usage(page)  # Update usage count and timestamp
        else:
            self.page_faults += 1
            if len(self.page_dict) == self.page_frames:
                self.evict_least_used()  # Evict least recently used page
            self.page_dict[page] = [1, 0]  # New page with usage count 1 and initial timestamp

    def update_usage(self, page):
        self.page_dict[page][0] += 1  # Increment usage count
        for other_page in self.page_dict:
            if other_page != page:
                self.page_dict[other_page][1] -= 1  # Decrement timestamps of other pages

    def evict_least_used(self):
        min_usage = float('inf')
        min_page = None
        for page, (usage, timestamp) in self.page_dict.items():
            if usage < min_usage or (usage == min_usage and timestamp < self.page_dict[min_page][1]):
                min_usage = usage
                min_page = page
        del self.page_dict[min_page]

    def get_page_faults(self):
        return self.page_faults

    def get_page_hits(self):
        return self.page_hits