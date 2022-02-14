#-indexing


```python
#make a string
a = "samosa pakora"
a
#count letter+space  is called index
```




    'samosa pakora'




```python
a
```




    'samosa pakora'




```python
#length of indeces
len(a)
```




    13




```python
a[0]
```




    's'




```python
a[1]
```




    'a'




```python
a[3]
```




    'o'




```python
a[12]
```




    'a'




```python
a[0:5] #dont use [0to5] it will give error dont use [0-5]
```




    'samos'




```python
a[0:6] #last index is exclusive
```




    'samosa'




```python
a[0:13] #to get 12 letters of samosa pakoda we will type 13 num
```




    'samosa pakora'




```python
a[-2]
```




    'r'




```python
a[-6]
```




    'p'




```python
a[-1]
```




    'a'




```python
a[-6:-1]
```




    'pakor'




```python
a[-6:-0] 
```




    ''




```python
a[-6:-1]
```




    'pakor'




```python
a[-6:13] #firstly determine length
```




    'pakora'




```python
food= "biryani"
food
```




    'biryani'



#string methods


```python
food
```


```python
len(food)
```




    7




```python
#capitalize every letter
food.capitalize()
```




    'Biryani'




```python
#upper case letters
food.upper()
```




    'BIRYANI'




```python
l#owercase letters
food.lower()
```




    'biryani'




```python
#replace
food.replace("b","sh")
```




    'shiryani'




```python
#counting a specific alphabet in string (bioinformatics)
name= "baba_aammar with aammar tufail"
name
```




    'baba_aammar with aammar tufail'




```python
name.count("a")
```




    9




```python
name.count("ba")
```




    2




```python
#case sensitive cap letter how many time?
name.count("A")
```




    0




```python
name.count("t")
```




    2



### -finding an index number in string



```python
name= "baba_aammar with aammar tufail"
name
```




    'baba_aammar with aammar tufail'




```python
name.find("t")
```




    14




```python
name.find("b")
```




    0




```python
name.find("aa")
```




    5




```python
#how to split astring
food = "i love samosa, pakora, raita, biryani and karahi"
food
```




    'i love samosa, pakora, raita, biryani and karahi'




```python
food.split(",")
```




    ['i love samosa', ' pakora', ' raita', ' biryani and karahi']




```python

```
