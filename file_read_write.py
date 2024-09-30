def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    write_to_file('example.txt', 'Hello, World!')
    print("Written content to the file")
    content = read_from_file('example.txt')
    print("Content read from file:", content)

if __name__ == "__main__":
    main()
