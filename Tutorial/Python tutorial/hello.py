# def lesser_of_two_even(a,b):
#     if a%2==0 and b%2==0:
#         print('Both no is Even')
#         print(min(a,b))
#     else:
#         print(max(a,b))
#         print('One or Both no is odd')


# lesser_of_two_even(2,4)

# def animal_crackers(text):
#     wordlist = text.lower().split()
#     return print(wordlist[0][0]==wordlist[1][0])

# animal_crackers('Levelheaded Llama')
# animal_crackers('Crazy Kangaroo')

# def old_macdonald(name):
#     first_letter = name[0].upper()
#     fourth_letter = name[3].upper()

#     print(first_letter+name[1:3]+fourth_letter+name[4:])

# old_macdonald('macdonald')

# def master_yoda(text):
#     lst =text.split()

#     x= (lst[::-1])
#     print(' '.join(x))

# master_yoda('i am home')
# master_yoda('we are ready')


def makes_twenty(n1,n2):
    return print((n1 == 20) or (n2==20)) or (n1+n2)==0

makes_twenty(2,1)
