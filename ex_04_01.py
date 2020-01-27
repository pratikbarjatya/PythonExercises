def computepay(h,r):
    if h > 40:
        pay = (40 * r) + (h - 40)*r*1.5
    else:
        pay = h * r
    return pay
hrs = input("Enter Hrs: ")
h = float(hrs)
rph = input('Enter rate per hour: ')
r = float(rph)
p = computepay(h,r)
print(p)
