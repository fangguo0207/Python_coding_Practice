message='Nik is the German company.'
count={}
for character in message:
	count.setdefault(character,0)
	count[character]=count[character]+1
print(count)


message='Nik is the German company.'
for character in message:
	print(character)