from Load import LoadJson #this way you can import specipic class

def main():
    lc=LoadJson()
    print(lc.getStepTimers('Crock'))

if __name__ == '__main__':
    main()

