# file_read_write.py
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    write_to_file('example.txt', 'Hello, World!')
    print("Written content to the file")

if __name__ == "__main__":
    main()
