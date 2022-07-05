vowels_list = ['a','e','i','o','u','A', 'E', 'I', 'O', 'U']

word = input('Enter word : ')

for i in word:
    if i in vowels_list:
        print(f'{i} is a vowel')
    else:
        print(f'{i} Not a Vowel')

