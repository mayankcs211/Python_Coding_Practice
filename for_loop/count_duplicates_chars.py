sample_str = 'This is is Python'

sample_str_list = sample_str.split()
print(sample_str_list)

no_dups = []
for i in sample_str_list:
    if i not in no_dups:
        no_dups.append(i)

print(no_dups)
print(' '.join(no_dups))

