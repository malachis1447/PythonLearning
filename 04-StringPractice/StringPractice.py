# StringPractice.py 
# Kain M. Snyder
# Thu Aug 10th 2023 0337 MDT

def StringPracticeMain():
    global CompanyName
    CompanyName = str("Malachi Technologies")
    print(CompanyName)
StringPracticeMain()

def StringLengthCaseCheck():
    print(len(CompanyName))
    print(CompanyName.isupper)
StringLengthCaseCheck()

def StringIndexTest():
    print(CompanyName.index("Malachi"))
StringIndexTest()

def StringReplaceTest():
    print(CompanyName.replace("Technologies", "Microsystems"))
StringReplaceTest()