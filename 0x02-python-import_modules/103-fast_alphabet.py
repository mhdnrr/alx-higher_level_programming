import string

def generate_alphabet():
    alphabet = string.ascii_uppercase
    index = 0
    final_output = ""
    
    def generate_output():
        nonlocal index
        nonlocal final_output
        
        if index < len(alphabet):
            final_output += alphabet[index]
            index += 1
            generate_output()
    
    generate_output()
    
    return final_output

output = generate_alphabet()
print(output)
