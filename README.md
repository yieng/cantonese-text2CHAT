# README
Converts Cantonese Chinese characters into Jyutping romanization. Works for most characters.

[PyCantonese](http://pycantonese.org)  
[Python學習07 利用Python程式轉換語音成文字(Transform Voice to Text by Python SpeechRecognition)](https://www.youtube.com/watch?v=3LLksqP2aXE)  
[Ekho](https://www.eguidedog.net/ekho.php)

## Instructions (for Windows 10 machines):  

1) Install [Python 3.7 or above](https://www.python.org/downloads/).  
2) Install the [PyCantonese](http://pycantonese.org) and NLTK (Natural Language Toolkit) dependencies: Start > Run > input ```cmd``` > input the following in the console:  
```
py -3 -m pip install -U pycantonese nltk
```
3) Download the "Raw" version of the ```ChineseCharacter2Jyutping.py``` file.  
4) Using Notepad, save all the Chinese text you need to analyze in a file ```sample.txt``` (or any other name, always with ".txt" as suffix) with ```UTF-8``` encoding (rather than the default ANSI) -- this encoding option is available in the "Save As" dialog box in Notepad, next to the ```Save``` button.    
5) Run the following command:  
```
py -3 ChineseCharacter2Jyutping.py
```
5) Input ```sample``` (or your designated file name) when prompted by the program.  
6) The program will generate the Jyutping corresponding to the words in the file.
