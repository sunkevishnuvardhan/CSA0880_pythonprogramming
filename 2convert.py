def convert_strings(s1, s2):
    def convert_to_lower(s):
        return ''.join(c.lower() if c.isupper() else c for c in s)
    
    converted_s1 = convert_to_lower(s1)
    converted_s2 = convert_to_lower(s2)
    
    return converted_s1, converted_s2

s1 = "HeLlo"
s2 = "WORLD"
converted_s1, converted_s2 = convert_strings(s1, s2)
print(f"Converted s1: {converted_s1}")
print(f"Converted s2: {converted_s2}")

