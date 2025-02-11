
import re

def extract_baby_names(file_name):
    with open(file_name, 'r') as f:
        html = f.read()
    
    pattern = r'<td>([A-Za-z]+)</td>'
    matches = re.findall(pattern, html)
    
    return matches

def bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
    return names

def binary_search(names, target):
    low = 0
    high = len(names) - 1
    while low <= high:
        mid = (low + high) // 2
        if names[mid] == target:
            return mid
        elif names[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
"""These functions extracts baby names from an HTML file, sorts them using Bubble Sort, 
and then performs a binary search to find a specific name."""
def main():
    file_name = 'baby2008.html'
    baby_names = extract_baby_names(file_name)
    print("Extracted Baby Names:")
    print(baby_names)
    
    sorted_baby_names = bubble_sort(baby_names)
    print("\nSorted Baby Names:")
    print(sorted_baby_names)
    
    target_name = 'Emily'
    index = binary_search(sorted_baby_names, target_name)
    if index != -1:
        print(f"\nFound '{target_name}' at index {index}.")
    else:
        print(f"\n'{target_name}' not found in the list.")

if __name__ == "__main__":
    main()

