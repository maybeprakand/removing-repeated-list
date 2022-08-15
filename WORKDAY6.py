#write a function that takes a list as a parameter  returns a list after removing all repeating elements
#2vat is 13 % of amount total sum is of amount and VAT write a function othat takes total and calculates amount and VAT




list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "+ str(list))

res = []
for i in list:
	if i not in res:
		res.append(i)


print ("The list after removing duplicates : "+ str(res))
