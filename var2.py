lst_of_files=['1.txt', '2.txt', '3.txt']
lst=[]
for file in lst_of_files:
    with open(file, encoding="UTF-8", mode='r') as f:
        name=file
        length_file=len(f.readlines())
        lst.append([name,length_file])


lst.sort(key=lambda x: x[1])

for item in lst:
    name=item[0]
    count_of_str=str(item[1])
    with open(name, encoding="UTF-8", mode='r') as f, open(file='out.txt', encoding="UTF-8", mode='a') as fw:
        fw.write(f'{name}\n{count_of_str}\n')
        for line in f:
            fw.writelines(line)
        fw.write('\n')
print(lst)


