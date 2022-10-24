import pandas as pd


print('Top 10')

people_card = {
        'Name': ['Muhammad', 'Isaac Newton', 'Jesus',	'Gautama Buddha', 'Confucius', 'Paul the Apostle', 'Cai Lun', 'Johannes Gutenberg', 'Christopher Columbus', 'Albert Einstein'],
        'Years of life' : ['c. 570–632','1643–1727','4 BC–33 AD','563–483 BC','551–479 BC','5–67 AD','50–121 AD','1398–1468','1451–1506','1879–1955',],
        'Type of activity': ['Spiritual and political Leader','Scientist','Spiritual leader','Spiritual leader','Philosopher','Christian apostle','Inventor of paper','Inventor of the printing press','Explorer','Scientist'],
        'ID' : ['1','2','3','4','5','6','7','8','9','10']
}
    
df = pd.DataFrame(people_card)

with open('list.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{df}')
        cl.write('\n')
    
print(df)