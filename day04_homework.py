# 7-1
years_list=[1980,1981,1982,1983,1984,1985]

# 7-2
third_birth=years_list[2]
print(third_birth)

# 7-3
oldest=years_list[-1]
print(oldest)

# 7-8
suprise=['Groucho','Chico','Harpo']
print(suprise)

# 7-9
lower=suprise[-1].lower()
print(lower)
name = "harpo"
reverse_name = ''
for c in name:
    reverse_name = c + reverse_name

print(f'name    : {name}')
print(f'reverse : {reverse_name}')
lower_2=reverse_name.capitalize()
print(lower_2)

# 7-10
even_number=[number for number in range(10) if number%2==0 and number!=0]
print(even_number)


# 8-1
e2f={'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)

# 8-2
dic_eng=e2f['walrus']
print(dic_eng)

# 8-3
f2e=e2f.items()
dict_f2e=dict(f2e)
print(dict_f2e)

# 8-4
dic_french=[k for k, v in e2f.items() if v == 'chien']
print(dic_french)

# 8-5
key_eng=e2f.keys()
print(key_eng)

# 8-6
# 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}
life={'animals':{'cats':'Henri','octopi':'Grumpy','emus':'Lucy'},'plants':{},'others':{}}
print(life)

# 8-7
greatest_keys=life.keys()
print(greatest_keys)

# 8-8
# 딕셔너리[키][키]
# 딕셔너리[키][키] = 값

print(life)
greatest_keys=life.keys()

x=life.get('animals')
print(x)
genenral_keys=x.keys()
print(genenral_keys)

every_keys=list(greatest_keys)+list(genenral_keys)
print(every_keys)


# 8-9
every_values=life['animals']['cats']
print(every_values)


# 8-10
squares={i:i**2 for i in range(10)}
print(squares)

# 8-11
odd_number_set={i for i in range(10) if i%2!=1 and i!=0}
print(odd_number_set)





