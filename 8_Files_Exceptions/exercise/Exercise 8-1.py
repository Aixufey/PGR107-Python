def main():
    filename = "hello.txt"
    file = open(filename, "w")    
    file.write("Hello, World!")
    file.close()

    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()

main()