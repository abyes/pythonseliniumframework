items=3
assert(items == 3)

#when u think some specific code will fail so u will wrap this on try block and send control back to catch block
#in python instead of catch we use except

try:
    with open("thelog.txt") as reader:
        reader.read()

except Exception as b:
    print(b)
#there is one more finally block which is user to clear records or cookies finally will run even thr try condition is
#true

# so it gives an error what python think

