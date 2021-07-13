def func(les, time):
    print(les+ time+" lesson")

func("1st", " 18:00")
func("2nd", " 19:00")

#n = list(str(input().split()))

def kid(*kids):
    print("the youngest child is "+ kids[-1])

kid("Azamat", "Sanzhar", "Adilet")

def kid(kid1, kid2, kid3):
    print("the youngest child is "+ kid3)

kid(kid1="Aruzhan", kid2 = "Asem", kid3="Asel")

def nums(x):
    return 5*x

def nums1(y):
    print(y * nums(5))

nums1(6)

def recur(k):
    if(k>0):
        result = k + recur(k-1)
        print(result)
    else:
        result = 0
    return result

recur(2)
