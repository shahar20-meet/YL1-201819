
list = [1,2,6,3,2,2,7,8,12,26]
def fun1 (a):
	b=[]
	b.append(a[0])
	b.append(a[-1])
	print(b)
fun1(list)

a = [1, 1, 2, 3, 5, 8, 16, 21, 34, 55, 99]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


a = [1, 1, 2, 3, 5, 8, 23, 21, 34, 57, 89]
d =[]
for num in a:
        if(num<5):
                print(num)
                d.append(num)
                print(d)


ay = [1, 2, 3, 1, 4, 67, 44, 65, 19]
by = [2, 4, 5, 6, 7, 23, 47, 68, 96]
cy = []
for i in a:
        if i in by and i not in cy:
                cy.append(i)
                print(cy)

 

def la (a):
         for i in range(2,a/2):
                 if a%i==0:
                 return false
         return true
print(la(input()))
