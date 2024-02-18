# Python3 implementation of FIFO page
# replacement in Operating Systems.
from queue import Queue
from typing import List


# Function to find page faults using FIFO
def pageFaults_FIFO(pages: List[int], n: int, capacity: int):
    # To represent set of current pages.
    # We use an unordered_set so that we
    # quickly check if a page is present
    # in set or not
    s = set()

    # To store the pages in FIFO manner
    indexes = Queue()

    # Start from initial page
    page_faults: int = 0
    page_hits: int = 0

    for i in range(0, n, 1):

        # Check if the set can hold
        # more pages
        if len(s) < capacity:

            # Insert it into set if not present
            # already which represents page fault
            if pages[i] not in s:
                s.add(pages[i])

                # increment page fault
                page_faults += 1

                # Push the current page into
                # the queue
                indexes.put(pages[i])

        # If the set is full then need to perform FIFO
        # i.e. remove the first page of the queue from
        # set and queue both and insert the current page
        else:

            # Check if current page is not
            # already present in the set
            if pages[i] not in s:

                # Pop the first page from the queue
                val = indexes.queue[0]

                indexes.get()

                # Remove the indexes page
                s.remove(val)

                # insert the current page
                s.add(pages[i])

                # push the current page into
                # the queue
                indexes.put(pages[i])

                # Increment page faults
                page_faults += 1

            else:
                page_hits += 1

    return page_faults, page_hits

class FIFO:
    def __init__(self, page_frames):
        self.page_frames = page_frames
        self.page_queue = []
        self.page_faults = 0
        self.page_hits = 0

    def access(self, page):
        if page in self.page_queue:
            self.page_hits += 1
            self.page_queue.remove(page)
            self.page_queue.append(page)
        else:
            self.page_faults += 1
            if len(self.page_queue) == self.page_frames:
                self.page_queue.pop(0)
            self.page_queue.append(page)

    def get_page_faults(self):
        return self.page_faults

    def get_page_hits(self):
        return self.page_hits