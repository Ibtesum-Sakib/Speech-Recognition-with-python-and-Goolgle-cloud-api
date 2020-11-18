from difflib import SequenceMatcher #importing sequencematcher from difflib library
#using read() to take all string from the text
text1 = open(r"D:\asr_bengali\data\13782.txt",encoding="utf-8").read()  #translated text
text2 = open(r"D:\asr_bengali\data\main1.txt",encoding="utf-8").read()  #actual text
m = SequenceMatcher(None, text1, text2)     #passing text1&2 to the method
diffr=m.real_quick_ratio()*100          #calculate the accuracy and use real_quick_accuracy to find the optimal accuracy
diffr=str(round(diffr,5))       #taking as a string and round this to 5 floating point after dot
print(diffr+f" percent accuracy") #concatening the result to print accuracy
