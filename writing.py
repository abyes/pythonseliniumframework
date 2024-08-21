with open("readandwrite.txt","r") as reader:
    read =reader.readlines()
    reversed(read)
    with open("readandwrite.txt", "w") as writer:

        for line in reversed(read):

            writer.write(line)











