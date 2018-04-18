
# coding: utf-8

# In[1]:

print 'Hello Ric'


# In[2]:

a=3
b=7
#this does the summation 
result = a+b
print result


# In[9]:

#multi line statement 
a= (1+2+3+4+
       5+6+7)
    
print a


# In[14]:

#multi line statement using ()[] and{}
colors=['red',
       'blue',
       'green']


# In[15]:

#multiple statements in a single line using semi colons
a=1;b=4;c=6
#output C to confirm the code is working 
print b


# In[16]:

#case construts indentation 
if True:
    print 'Hello'
    a=5


# In[18]:

# DocString ---documentation string  eg
'''Multi line comments are put under three
quotes at all times.'''

def double(num):
    return 2*num


# In[19]:

#constants. Usually declared and assigned on a module
#Declaring and assigning values to constants. 

PI=3.143
GRAVITY=9.8

print GRAVITY


# In[24]:

#literals in python 

a=0b1010 #binary literal
b=100 #decimal literal
c=0o310 #Octal literal
d=0x12c #Hexadecimal

#float literals

float_1=10.5
float_2=1.5e2

#complex literals
x=3.14j

print a, b, c, d
print float_1, float_2
print x, x.imag, x.real


# In[25]:

#how to use string literals in python 
strings='This is a String'
char='S'
multiline_str='''This is a multiline string which is very 
important to learn and understand how it works'''
unicode=u'\u00dcnic\u00f6de'
raw_str=r'raw \n string'

print strings
print char
print multiline_str
print unicode
print raw_str


# In[29]:

#boolean literals in python 
x=(1==True)
y=(1==False)
a=True+4
b=False+10

print 'x is', x
print 'y is', y
print 'a:', a
print 'b:', b

#Tre represents 1 and false is a 0 The value of x is true becasue 1 is true and that of y is false becasue 1 is not equal to false '''


# In[31]:

#special literals in python 
#we define the menu in this program 

#the menu has the following 
drink='Available'
food=None

def menu(x):
    if x==drink:
        print drink
    else:
        print food
        
        #if the value of x is drink the program prints available since the menu has only drinks that aee available 
menu(drink)
menu(food)


# In[ ]:



