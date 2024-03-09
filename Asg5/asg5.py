# Ayub Yusuf
# Assignment #5

# Description:
# This Python script simulates three page replacement algorithms: FIFO (First In First Out), LRU (Least Recently Used), and Optimal. 

import os
import random

class PageReplacement:
    # FIFO algorithm: pages are evicted in the same order they were added.
    @staticmethod
    def fifo(pages, frames):
        memory, faults, queue = set(), 0, []  # Initialize memory set, fault counter, and FIFO queue.
        for page in pages:
            if page not in memory:
                if len(memory) < frames:  # If there's room, add the page directly.
                    memory.add(page)
                    queue.append(page)
                else:  # Otherwise, replace the oldest page.
                    memory.remove(queue.pop(0))
                    memory.add(page)
                    queue.append(page)
                faults += 1  # Increment fault count for each miss.
        return faults

    # LRU algorithm: least recently used page is replaced.
    @staticmethod
    def lru(pages, frames):
        memory, faults, stack = set(), 0, []  # Memory set, fault counter, and LRU stack.
        for page in pages:
            if page not in memory:
                if len(memory) < frames:  # Add the page if there's room.
                    memory.add(page)
                else:  # Replace the least recently used page.
                    memory.remove(stack.pop(0))
                    memory.add(page)
                faults += 1
            elif page in stack:  # Update stack if page is accessed.
                stack.remove(page)
            stack.append(page)  # Add page as most recently used.
        return faults

    # Optimal algorithm: replaces the page that will not be used for the longest period.
    @staticmethod
    def optimal(pages, frames):
        memory, faults = set(), 0
        for i, page in enumerate(pages):
            if page not in memory:
                if len(memory) < frames:  # Add the page if there's room.
                    memory.add(page)
                else:  # Find and replace the page with the farthest future use.
                    farthest_index, farthest_page = -1, None
                    for m in memory:
                        if m not in pages[i + 1:]:  # If a page is not used again, it's the best candidate.
                            farthest_page = m
                            break
                        else:  # Otherwise, find the page used farthest in the future.
                            next_use = pages[i + 1:].index(m) + i + 1
                            if next_use > farthest_index:
                                farthest_index, farthest_page = next_use, m
                    memory.remove(farthest_page)
                    memory.add(page)
                faults += 1  # Increment.
        return faults

# Simulates page replacement for each algorithm across a range of frame sizes.
def simulate_page_replacement(strings, frames_range):
    results = {}
    for index, string in enumerate(strings): 
        results[index] = {"FIFO": [], "LRU": [], "Optimal": []}
        for frames in frames_range:  
            # Append the number of faults for each algorithm to the results dictionary.
            results[index]["FIFO"].append(PageReplacement.fifo(string, frames))
            results[index]["LRU"].append(PageReplacement.lru(string, frames))
            results[index]["Optimal"].append(PageReplacement.optimal(string, frames))
    return results

if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_file_path = os.path.join(script_dir, "output.txt")

    # Header with assignment information
    output_file = open(output_file_path, "w")  # Open file for writing

    output_file.write("Ayub Yusuf, 3.8.2024, Assignment 5.\n\n")

    # Simulation setup
    random_page_string = [random.randint(0, 9) for _ in range(20)]
    fixed_page_string1 = [0, 7, 0, 1, 2, 0, 8, 9, 0, 3, 0, 4, 5, 6, 7, 0, 8, 9, 1, 2]
    fixed_page_string2 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    page_strings = [random_page_string, fixed_page_string1, fixed_page_string2]
    frame_range = range(1, 8)  # Number of frames ranges from 1 to 7

    # Run the simulation
    results = simulate_page_replacement(page_strings, frame_range)

    # Print the results with improved formatting
    for index, result in results.items():
        for frames in frame_range:
            output_file.write(f"For {frames} page frames, and using string page reference string:\n")
            output_file.write(f"{','.join(map(str, page_strings[index]))}\n")
            output_file.write(f"   FIFO had {result['FIFO'][frames - 1]} page faults.\n")
            output_file.write(f"   LRU had {result['LRU'][frames - 1]} page faults.\n")
            output_file.write(f"   Optimal had {result['Optimal'][frames - 1]} page faults.\n")

    output_file.close()  # Close the file after writing
