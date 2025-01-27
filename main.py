path_to_file = "books/frankenstein.txt"

def main():


    

    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
    
    word_count = len(file_contents.split())
    print(word_count)


def character_counter(path_to_file):
    
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    
    text = file_contents.split()
    
    
    characters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    char_count = {}

    
    for char in characters:
        char_count[char] = 0

    
    for word in text:
        word = word.lower() 
        for char in word:
            if char in characters:  
                char_count[char] += 1
    
    char_count[' '] += file_contents.count(' ')

    print(char_count)
    

             

        
        
        
main()
character_counter(path_to_file)