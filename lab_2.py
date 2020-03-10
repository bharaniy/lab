a = {'mohit': 99, 'bharani': 90}
b = {'aneesh': 80, 'srujan': 70}
b.update(a)
res= sorted(b.items(), key=lambda x: x[1])
print(res)