def user(**kw):                     #Keyworded avariable argument function with no 
    #print(kw)                      #position argument
    for i,j in kw.items():
        print(i,j)
def main():
    user(name='avishek',age=24,mob=365412)

if __name__ == "__main__":
    main()