#!/usr/bin/python  
# -*- coding: utf-8 -*-
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
#from chatterbot.trainers import ChatterBotCorpusTrainer



bot=ChatBot('carter-one')
conv = open('chatlist.txt','r', encoding = 'utf-8').readlines()

#bot.set_trainer(ListTrainer,ChatterBotCorpusTrainer)
bot.set_trainer(ListTrainer)
bot.train(conv)
#bot.train("chatterbot.corpus.chinese") 


while True:
	request=input('you: ')
	response= bot.get_response(request)
	print('carter-one:', response)