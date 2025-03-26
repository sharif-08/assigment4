try:
    file = open("sample.txt",'r')
    reading_file = file.read()
    print(reading_file)
    file.close()

except:
    print("Error : the file'sample.txt' was not found")

