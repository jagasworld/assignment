# file_read_write.py
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    content = read_from_file('example.txt')
    print("Content read from file:", content)

if __name__ == "__main__":
    main()
