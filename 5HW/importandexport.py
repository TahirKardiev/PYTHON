import csv
from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import InputPhoneContact
# api_id = '0'
# api_hash = '0'
# client = TelegramClient('myname', api_id, api_hash)
# contacts_book = []
# with open('list.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         contacts_book.append(InputPhoneContact(client_id=0, phone='+' + line[0], first_name=line[1], last_name=line[2]))
# result = client(GetContactsRequest(contacts_book))
# encoding='cp1251'
# x = open('list.csv','r')
# x.readline(1)
# print(x)

# import csv

# with open("list.csv", "r") as f:
#     reader = csv.reader(f, delimiter="\t")
#     for i, line in enumerate(reader):
#         print (line)

import pandas as pd

data = pd.read_csv("list.csv", nrows=1)
print(data)

data.to_csv("list.csv", sep='\t')