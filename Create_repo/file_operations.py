def save_to_file(content,filename):
    with open(filename,'w') as f:
        f.write(content)

def read_from_file(filename):
    with open("test_file.txt",'r') as f:
        content = f.read()
        return content

save_to_file("""Hi Hello! How are you?
I am Good""","test_file.txt")
read_from_file("test_file.txt")