import time

def main():
    for i in range(10, 0, -1):
        print(f"{i:3d}", end="\r")
        time.sleep(1)

if __name__=="__main__":
    main()
