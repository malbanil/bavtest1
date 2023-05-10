import os
  

def main():
    file_object = open('sample.txt', 'a')
    ouput = "message: Test"
    file_object.write('hello'+ '\n')
    file_object.close() 
    print(ouput)

"""
main ...........................................................................
"""
if __name__ == '__main__':
    main();
