user_input =input("enter text to write to file : ")
file = open('output.txt',"w")
writing_file = file.write(user_input + "\n")
file.close()
print("data successfully written to output.txt.")

user_append =input("enter additional text to append : ")
file = open("output.txt",'a')
appending_file = file.write(user_append + '\n')
file.close()
print("data successfully appended.")

print("final content of output.txt:")
file = open('output.txt',"r")
reading_file = file.read()
print(reading_file)
file.close()