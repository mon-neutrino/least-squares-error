import math


a= #A value
b= #B value
c= #C value


x_list=[0.373,0.655,0.959,1.253,1.542,1.812,2.100,2.411,2.697,2.980,3.255,3.530,3.794,4.075,4.342]
y_list=[-0.120,0.204,-0.227,0.193,-0.192,0.220,-0.257,0.234,-0.196,0.183,-0.184,0.145,-0.131,0.143,-0.209]
results=[] #a list to keep track of predicted y values
h_list=[] #a list to keep track of the squared differences between each actual and predicted y value


for i in range(15):
    y=a*math.sin(b*(x_list[i]+c)) #sine root equation excluding d variable (vertical shift)
    results.append(y)


for i in range(14): #taking the ith term of the y (actual) and result list, then subtract
    y_=y_list[i]
    r_=results[i]
    h=y_-r_
    h_list.append(h**2) #squaring the difference to remove any negative values


s=sum(h_list) #taking the sum of all the squares of differences
print('least squares result =', s)
