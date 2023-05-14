import sys
sys.setrecursionlimit(10**6)


def generate_path(row,col,output,i,j):
        if i > (row) or j  > (col):
            return


        if i==(row) and j==(col):
            print(output)
            return
        #horizontal
        generate_path(row,col,output+"h",i,j+1)
        
        #vertical
        generate_path(row,col,output+"v",i+1,j)


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    inputs=input().strip()
    a=inputs.split(" ")
    row=int(a[0])
    col=int(a[1])
    generate_path(row,col,"",1,1)
    

    return 0

if __name__ == '__main__':
    main()