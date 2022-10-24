import people_info as peop

c = input('Enter mans ID for searhing: ')
if c in peop.people_card['ID']:
    index = peop.people_card['ID'].index(c)
    print(f" One of the top 10 - {peop.people_card['Name'][index]}\n Years of life - {peop.people_card['Years of life'][index]}\n {peop.people_card['Type of activity'][index]} ")

    exit()
else:
        print('another one')
exit()


