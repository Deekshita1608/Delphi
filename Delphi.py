#list of imported modules

import subprocess
import webbrowser
import speech_recognition as sr
import wikipedia
import datetime
from gtts import gTTS
from playsound import playsound
import os
import wolframalpha
import random


#Introductory speech of assistant

mytext='Hello, I am Delphi, your personal assistant. How may I help you?'
language='en'
announce=gTTS(text=mytext, lang=language, slow=False)
announce.save('welcome.mp3')
playsound('welcome.mp3')

#record audio from user and convert it to text
while True:

        r=sr.Recognizer()
        with sr.Microphone() as source:
                                playsound('beep.mp3')
                                print('I am listening...')
                                audio=r.record(source, duration=6)
        try:
            
                text=r.recognize_google(audio)
                print('You said :', text)

                #Gives current time
                
                if 'time' in text:
                            now=datetime.datetime.now()
                            x=now.strftime('%H:%M:%S')
                            timestr='The time right now is'+x
                            time=gTTS(text=timestr,lang=language,slow=False)
                            time.save('time.mp3')
                            playsound('time.mp3')

                # Searches for files in Desktop, Confirms choice from user and opens it
                

                elif 'open' in text:
                    li=text.split()
                    directory1=[]
                    files=[]
                    count=0
                    filename=' '.join(li[1:])
                    path='C:\\Users\\91987\\Desktop'
                    for entry in os.scandir(path):
                            
                            #to search through first set of folders
                            
                            if entry.is_file():
                                  if filename in str(entry) or filename in str(entry).upper() or filename in str(entry).lower() or filename in str(entry).capitalize() or filename in str(entry).title():
                                        file=str(entry)[11:(len(str(entry))-2)]
                                        count+=1
                                        print(count,file)
                                        directory=path+'\\'+str(entry)[11:(len(str(entry))-2)]
                                        directory1.append(directory)
                                        files.append(str(entry)[11:(len(str(entry))-2)])
                            if entry.is_dir():
                                  if filename in str(entry) or filename in str(entry).upper() or filename in str(entry).lower() or filename in str(entry).capitalize() or filename in str(entry).title():
                                        file=str(entry)[11:(len(str(entry))-2)]
                                        count+=1
                                        print(count,file)
                                        directory=path+'\\'+str(entry)[11:(len(str(entry))-2)]
                                        directory1.append(directory)
                                        files.append(str(entry)[11:(len(str(entry))-2)])
                                        
                                  #updated path
                                        
                                  path1=path+'\\'+str(entry)[11:(len(str(entry))-2)]

                                  #to search through second set of folders
                                  
                                  for entry in os.scandir(path1):
                                          if entry.is_file():
                                              if filename in str(entry) or filename in str(entry).upper() or filename in str(entry).lower() or filename in str(entry).capitalize() or filename in str(entry).title():
                                                 file=str(entry)[11:(len(str(entry))-2)]
                                                 count+=1
                                                 print(count,file)
                                                 directory=path1+'\\'+str(entry)[11:(len(str(entry))-2)]
                                                 directory1.append(directory)
                                                 files.append(str(entry)[11:(len(str(entry))-2)])
                                          if entry.is_dir():
                                                        if filename in str(entry) or filename in str(entry).upper() or filename in str(entry).lower() or filename in str(entry).capitalize() or filename in str(entry).title():
                                                               file=str(entry)[11:(len(str(entry))-2)]
                                                               count+=1
                                                               print(count,file)
                                                               directory=path1+'\\'+str(entry)[11:(len(str(entry))-2)]
                                                               directory1.append(directory)
                                                               files.append(str(entry)[11:(len(str(entry))-2)])
                                                        path2=path1+'\\'+str(entry)[11:(len(str(entry))-2)]

                                                        #to search through third set of folders
                                                        
                                                        for entry in os.scandir(path2):
                                                                if entry.is_file():
                                                                       if filename in str(entry) or filename in str(entry).upper() or filename in str(entry).lower() or filename in str(entry).capitalize() or filename in str(entry).title():
                                                                           file=str(entry)[11:(len(str(entry))-2)]
                                                                           count+=1
                                                                           print(count,file)
                                                                           directory=path2+'\\'+str(entry)[11:(len(str(entry))-2)]
                                                                           directory1.append(directory)
                                                                           files.append(str(entry)[11:(len(str(entry))-2)])
                                                                if entry.is_dir():
                                                                   if filename in str(entry) or filename in str(entry).upper() or filename in str(entry).lower() or filename in str(entry).capitalize() or filename in str(entry).title():
                                                                         file=str(entry)[11:(len(str(entry))-2)]
                                                                         count+=1
                                                                         print(count,file)
                                                                         directory=path2+'\\'+str(entry)[11:(len(str(entry))-2)]
                                                                         directory1.append(directory)
                                                                         files.append(str(entry)[11:(len(str(entry))-2)])
                                                                   path3=path2+'\\'+str(entry)[11:(len(str(entry))-2)]

                                                                   #to search through fourth set of folders
                                                                   
                                                                   for entry in os.scandir(path3):
                                                                        if entry.is_file():
                                                                            if filename in str(entry) or filename in str(entry).upper() or filename in str(entry).lower() or filename in str(entry).capitalize() or filename in str(entry).title():
                                                                                     file=str(entry)[11:(len(str(entry))-2)]
                                                                                     count+=1
                                                                                     print(count,file)
                                                                                     directory=path3+'\\'+str(entry)[11:(len(str(entry))-2)]
                                                                                     directory1.append(directory)
                                                                                     files.append(str(entry)[11:(len(str(entry))-2)])
                    # to ask for filename confirmation
                    else:
                      if count!=0:
                            choosestr='State the serial number of the file you wish to open'
                            choose=gTTS(text=choosestr, lang=language, slow=False)
                            choose.save('choice.mp3')
                            playsound('choice.mp3')
                            with sr.Microphone() as source:
                                 playsound('beep.mp3')
                                 print('I am listening...')
                                 filerec=r.record(source, duration=5)
                                 filestr=r.recognize_google(filerec)

                    #to correct errors in speech to text.( She often hears '2' as 'Tu' and '3' as 'Tree')
                    
                            if 'tu' in filestr or 'Tu' in filestr or 'too' in filestr or 'to' in filestr:
                                           filestr='2'
                            if 'tree' in filestr or 'free' in filestr:
                                           filestr='3'
                            directoryfinal=str(directory1[int(filestr)-1])

                    #to open file
                    
                            os.startfile(directoryfinal)
                      else:
                            choosestr='File not found'
                            choose=gTTS(text=choosestr, lang=language, slow=False)
                            choose.save('notfound.mp3')
                            playsound('notfound.mp3')  

                #gives current date of computer

                elif 'date' in text:
                            now=datetime.datetime.now()
                            x=now.strftime('%d/%m/%Y')
                            timestr='Today\'s date is'+x
                            time=gTTS(text=timestr,lang=language,slow=False)
                            time.save('date.mp3')
                            playsound('date.mp3')

                #gives weather of place in query. If no place mentioned, gives weather based on device location.

                elif 'weather' in text or 'climate' in text:
                            api='VEL7AU-KEQT69L5QK'
                            client=wolframalpha.Client(api)
                            res=client.query(text)
                            weather=next(res.results).text
                            print(weather)
                            weather1=gTTS(text=weather, lang=language,slow=False)
                            weather1.save('weather.mp3')
                            playsound('weather.mp3')

                #to search for personalities on wikipedia
                            
                elif 'who is' in text or 'who was' in text :
                            li=text.split()
                            searchfor=str(li[2:])
                            result=wikipedia.summary(searchfor, sentences=2)
                            print(result)
                            resultannounce=gTTS(text=result, lang=language,slow=False)
                            resultannounce.save('wikiresult.mp3')
                            playsound('wikiresult.mp3')

                #to search for places on wikipedia
                            
                elif 'where is' in text or 'where was' in text :
                            li=text.split()
                            searchfor=str(li[2:])
                            result=wikipedia.summary(searchfor, sentences=2)
                            print(result)
                            resultannounce=gTTS(text=result, lang=language,slow=False)
                            resultannounce.save('wikiresult.mp3')
                            playsound('wikiresult.mp3')

                #to search for events or objects on wikipedia and also do calculations
                            
                elif 'what is' in text or 'what was' in text :
                        operators=['plus', 'minus','into','multiplied by','divided by','upon','raise to','square root','cube root','+','-','*','/','**','^','calculate']

                        #to figure out if user wants calculations or wikipedia search. If any elements of operators list present in user text, then end the checking and proceed to calculations.
                        
                        for element in range(0,len(operators)):
                                if str(operators[element]) in text:
                                       do='calculations'
                                       break
                                else:
                                        do='wikipedia'
                                        
                        if do=='wikipedia':
                                       li=text.split()
                                       searchfor=str(li[2:])
                                       result=wikipedia.summary(searchfor, sentences=2)
                                       print(result)
                                       resultannounce=gTTS(text=result, lang=language,slow=False)
                                       resultannounce.save('wikiresult.mp3')
                                       playsound('wikiresult.mp3')

                        #various operations
                                       
                        elif do=='calculations':
                                       li=text.split()
                                       if 'plus' in text or '+' in text:
                                          no1=int(li[2])
                                          no2=int(li[4])
                                          ans=no1+no2
                                       elif'minus' in text or '-' in text:
                                          no1=int(li[2])
                                          no2=int(li[4])
                                          ans=no1-no2
                                       elif 'into' in text or '*' in text:
                                          no1=int(li[2])
                                          no2=int(li[4])
                                          ans=no1*no2
                                       elif 'multiplied by' in text:
                                          no1=int(li[2])
                                          no2=int(li[5])
                                          ans=no1*no2
                                       elif '/' in text:
                                          no1=int(li[2])
                                          no2=int(li[4])
                                          ans=no1/no2
                                       elif'divided by' in text:
                                          no1=int(li[2])
                                          no2=int(li[5])
                                          ans=no1/no2
                                       elif 'raise to' in text:
                                          no1=int(li[2])
                                          no2=int(li[5])
                                          ans=no1**no2
                                       elif '**' in text or '^' in text:
                                          no1=int(li[2])
                                          no2=int(li[4])
                                          ans=no1**no2
                                       elif 'square root of ' in text:
                                          no1=int(li[-1])
                                          ans=no1**(0.5)
                                       elif 'cube root' in text:
                                          no1=int(li[-1])
                                          ans=no1**(1/3)
                                       answerstr='Your answer is : ' + str(ans)
                                       answer=gTTS(text=answerstr, lang=language, slow=False)
                                       answer.save('calculations.mp3')
                                       playsound('calculations.mp3')

                #to search on web

                elif 'search for' in text:
                            li=text.split()
                            search=' '.join(li[2:])
                            print(search)
                            announce2='Search results for your query are:'
                            announcegtts=gTTS(text=announce2, lang=language, slow=False)
                            announcegtts.save('searchresults.mp3')
                            playsound('searchresults.mp3')
                            webbrowser.open('https://www.google.com/search?q='+search, new=1)
                #to play videos from youtube
                            
                elif 'play' in text:
                            li=text.split()
                            search=' '.join(li[1:])
                            webbrowser.open('www.youtube.com/results?search_query=' + search,new=1)

                #reply to various forms of greeting
                            
                elif 'hello' in text or 'hi' in text:
                            list=['Hello','Hi! how are you?', 'hey!! How are you?','hii! How are you doing?']
                            greetingstr=random.choice(list)
                            greeting=gTTS(text=greetingstr, lang=language, slow=False)
                            greeting.save('greeting.mp3')
                            playsound('greeting.mp3')
                elif 'how are you' in text or 'how do you do' in text or 'what are you doing' in text:
                            list=['Never been better', 'Having fun!Its always a pleasure to be with you']
                            greeting1str=random.choice(list)
                            greeting1=gTTS(text=greeting1str, lang=language, slow=False)
                            greeting1.save('greeting1.mp3')
                            playsound('greeting1.mp3')
                elif 'exit' in text:
                        break

        #Message to be displayed in case of an error

        except:
                errorstr='Sorry, something went wrong. Please try again'
                error=gTTS(text=errorstr, lang=language, slow=False)
                error.save('error.mp3')
                playsound('error.mp3')
