from orangevaluehack import orangebookvalue
from apiCall import getReg

def main():
    vno=input("Enter the vehicle number: ")
    details=getReg(vno)
    print(details)
    orangebookvalue(details)


if __name__=="__main__":
    main()