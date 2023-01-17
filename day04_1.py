# tuple

# a='harry',  # tuple
# b=('harry',)  # tuple
# c=()  # empty tuple
# d='harry','ron'  # tuple(packing)
# e=('hermione')  # just str
# f=('harry','ron')  # tuple(packing)
# g=('hermione',)  # tuple
#
# print(f[1])
# x,y=f  # unpakcing
# print(x)
# print(y)
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#
# a=(1,2)
# b=(3,4)
# print(type(a+b))  # tuple
#
# a=a+b
# print(a)  # a=(1,2,3,4) (tuple)


# list

# list 함수로 튜플 변환 가능. 튜플을 바꾸려면 list(변수)로 list화 -> 변경 후 tuple(변수)로 tuple화.

# scores=('B+','A+','C+')
# temp=list(scores)
# print(temp)
# temp[1]='C+'
# temp[2]='A+'
# scores=tuple(temp)
# print(scores[1],scores[2])
# print(scores)


big_bang=['GD','태양','탑','대성','승리']


# big_bang.append('인하')
# print(big_bang)
#
big_bang.insert(1,'인하')  # 리스트.insert(삽입 뒤에 인덱스, 삽입변수)
# print(big_bang)
#
# print(big_bang*3)
#
exo=['백현','첸']
#exo.extend(big_bang)  # exo = exo + big_bang
# print(exo)

# exo.append(big_bang)
# print(exo)  #리스트 안에 리스트
# print(exo[2][2])  #두 번째 리스트의 두 번째 원소(태양). exo[-1][-4]도 가능.
#
# print(exo[2].pop())  #두 번째 리스트의 승리 제거
# print(exo)
#
# print(exo[2].pop(-2))  #두 번째 리스트의 탑 제거
# print(exo)
#
# del exo[2][-1]  # 두 번재 리스트의 대성 제거
# print(exo)
#
# #  remove(변수) 함수: 맨 앞에 있는 해당변수 제거.
# exo[2].remove('인하') #[2] 안 쓰면 big_bang 리스트를 하나의 원소로 간주해서 삭제 불가.
# print(exo)
#
#리스트.clear(변수)는 리스트의 모든 해당 변수 삭제

# exo.index('백현')
#
# exo.count('백현')

# sorted는 원본 안 바꾸고 정렬한 값만 보여주고 / sort는 원본도 바꿈.
# 변수.sort()

# primes=[2,12,3.0,5,7,11]
# primes_sorted=sorted(primes)
# print(primes)
# print(primes_sorted)

# primes=[2,12,3.0,5,7,11]
# primes.sort()
# print(primes)
#
# mixed=[6,4,5,'A',7,'마마무']
# mixed.sort()
# print(mixed) # 문자와 숫자 같이 있어서 에러남.

# mixed=['6','4','5','A','7','마마무']  # 전부 문자로 만들면 정렬 가능. 사전순: 숫자>알파벳(대문자 우선)>한글
# mixed.sort()
# print(mixed)
#
# mixed.sort(reverse=True)
# print(mixed)


# numbers=[2,1,4,0,3]
# numbers.sort(reverse=True)
# print(numbers)


# primes=[2,12,3.0,5,7,11]
# primes_copy=primes
# print(primes_copy)  # =primes
# primes[-1]='lunch time'
#
# print(primes_copy)  # primes_copy 값도 같이 바뀜
#
# primes[0]='morning coffee'
# print(primes)
# print(primes_copy)  # 같이 바뀜.


# a=[1,2,3]
# b=a.copy()
# c=list(a)
# d=a[:]
# a[2]='sw'     # immutable
# print(a,b,c,d)  # [1, 2, 'sw'] [1, 2, 3] [1, 2, 3] [1, 2, 3]

#a=[1,2,[5,-9]]
#b=a.copy()
# c=list(a)
#a[1]=-77           # immutable
# d=a[:]
# a[2][1]=7       #mutable, b/c/d 영향
# print(a,b,c,d)  #immutable할 때만 완전한 복제[1, 2, [5, 7]] [1, 2, [5, 7]] [1, 2, [5, 7]] [1, 2, [5, 7]]


# import copy
# a=[1,2,[5,-9]]
# b=copy.deepcopy(a)  # 별도의 메모리 공간 할당(복제본 따로 분리)
# c=list(a)
# d=a[:]
# a[2][1]=7       # mutable, deepcopy
# print(a,b,c,d)  # [1, 2, [5, 7]] [1, 2, [5, -9]] [1, 2, [5, 7]] [1, 2, [5, 7]]


# zip 함수: 다중 시퀀수 형태를 엮어서 튜플로 만듬
# list(zip(,)), dict(zip(,))


# number_list=[number for number in range(1,6)]
# number_list=[number-1 for number in range(1,6)]

# a_list=[number for number in range(1,6) if number%2==1]
# print(a_list)

# <list comprehension, generator>

# for i in range(1,11):
#     if i%2==1:
#         odd_lists.append(i)
# print(odd_lists)

# odd_lists=[i for i in range(1,11) if i%2==1]
# print(odd_lists, type(odd_lists))
#
# odd_tuples=(i for i in range(1,11) if i%2==1)
# print(odd_tuples) # <generator object <genexpr> at 0x0000017627AF9A80>: tuple comprehension 존재X


# generator: 단순발생 성질 때문에 메모리 공간을 먹지 않음. ex) 1에서 100까지 만들고 버림.

# ex 7-4, 7-5,7-6, 7-7
# things=['mozzarealla','cinderella','salmonella']
#
# things[-2]=(things[-2].title()
# print(things)
#
# things[0]=things[0].upper()
# print(things)
#
# things[2]=
# print(f]'{Delte the things.pop()} from things, get Nobel Prize')
# pring(things)


# alcohol_foods={
# '맥주':'치킨',
# '소주':'골뱅이소면',
# '와인':'치즈',
# '고량주':'짬뽕'
# }
# alcohol_list=list(alcohol_foods)  # 키값만 추출. 딕셔너리를 list화하면 키값만 가져와서 리스트 만듬.
# print(alcohol_list)  # ['맥주', '소주', '와인', '고량주']
#
# while True:
#     alcohol=input(f'술을 선택하시오 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4){alcohol_list[3]} 5)아무거나 6)계산 ')
#     if alcohol=='6':
#         break
#         print('다음에 또 봐요')
#     elif alcohol=='1':
#         print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다')
#     elif alcohol == '2':
#         print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다')
#     elif alcohol == '3':
#         print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다')
#     elif alcohol == '4':
#         print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다')
#     elif alcohol == '5':
          print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)}입니다')
#     else:
#         print('메뉴에서 골라주세요.')


# alcohol_foods={
# '맥주':'치킨',
# '소주':'골뱅이소면',
# '와인':'치즈',
# '고량주':'짬뽕'
# }
# alcohol_list=list(alcohol_foods)
# foods_list=[food for food in alcohol_foods.value()] # extract values and append list
# print(alcohol_list, food_list)


# import random
#
# alcohol_foods=dict('맥주'='치킨','소주'='골뱅이 소면',와인='치즈',고량주='짬뽕')
# alcohol_list
#
# for i in range(len(food_list)):
#     print(food_list[i])
#
# for food in enumberate(food_list):  #tuple return
#     print(food[1])



# dictionary

# students= {'name':'kim inha','age':23,'eyes':[0.9,1.1]}
# for k in students.keys():
#     print(k)
# for k in students.values():
#     print(k)

# for k,v in students.items():
#  #  print(k)
#     print(f'{k}:{v}')
# print(f'이름은 {students["name"]},나이는 {students["age"]}세', end=' ')
# print(f'시력은 좌: {students["eyes"][0]}, 우:{students["eyes"][1]}')





