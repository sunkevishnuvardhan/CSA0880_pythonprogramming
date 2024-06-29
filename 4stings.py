def count_matching_characters(s1, s2):
    if len(s1) != len(s2):
        return "Strings must be of the same length."

    count = 0
   
    for char1, char2 in zip(s1, s2):
        if char1 == char2:
            count += 1
    
    return count
s1 = "what"
s2 = "watch"
matches = count_matching_characters(s1, s2)
print(f"Number of matching characters at the same index: {matches}")
