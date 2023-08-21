def consonant_value(m):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    max_value = 0
    current_value = 0
    
    for char in m:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
    return max(max_value, current_value)


print(consonant_value("maimuna"))  
print(consonant_value("strength"))  
print(consonant_value("sky"))  
