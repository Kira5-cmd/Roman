<pre>
#Roman 
This is roman no library

#syntax
from roman import Roman
a = Roman(90) #here you can give only int as argument if you give other datatype then it causes <b style="color:red">"NotIntegerError"</b>
b = Roman(90)

print(a) #it will return you XC
sum = a + b #it will return Roman(180) -> CLXXX
diff = a - b # it will give erorr <b style="color:red">ZeroNotInRoman<b> 
true_div = a/b # Error: <b style="color:red">NotIntegerError</b>
  
#Errors
"ZeroNotInRoman": Error means zero can't be written as roman because roman numbersystem doesnot have 0. 
"NotIntegerError": This error means you can only give integer as argument

</pre>
