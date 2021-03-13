import re

f=open("weather.txt", mode="r", encoding="utf8")
content=f.read()
f.close()

#Ερώτημα 1
#pattern=re.compile("[0-9]")  # <-- Εδώ βάζουμε το RE

#Ερώτημα 2
#pattern=re.compile("-?[0-9]+\.?[0-9]*")  # <-- Εδώ βάζουμε το RE

#Ερώτημα 3
#pattern=re.compile("-?[0-9]+\.?[0-9]* mm")  # <-- Εδώ βάζουμε το RE

#Ερώτημα 4
#pattern=re.compile("\([^)]+\)")  # <-- Εδώ βάζουμε το RE

#Ερώτημα 5
#pattern=re.compile("[0-9]+\/[0-9]+\/[0-9]+")  # <-- Εδώ βάζουμε το RE

#Ερώτημα 6
#pattern=re.compile("[^ ]+ [0-9]+\/[0-9]+\/[0-9]+")  # <-- Εδώ βάζουμε το RE

#Ερώτημα 7
#pattern=re.compile("[^( :\(\)\.)]*[άέόίήύώΆΈΌΊΉΎΏ][^( :\(\)\.)]*")  # <-- Εδώ βάζουμε το RE

#Ερώτημα 8
pattern=re.compile("[(Α-Ω)(Ά-Ώ)][(α-ω)(ά-ώ)][(α-ω)(ά-ώ)]+")  # <-- Εδώ βάζουμε το RE


result=pattern.findall(content)
print(result)
print(len(result))

