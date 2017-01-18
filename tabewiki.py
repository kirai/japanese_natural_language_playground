import wikipedia

wikipedia.set_lang("ja")

search_term = "代官山"
search_term = "アップル"

#print(wikipedia.search(search_term))

try:
	result = wikipedia.search(search_term)
	print(result.title)
except:
	print("Recommendation may refer to: ")
	print(result[1])

# 	for i, r in enumerate(result):
#		print i, r
#	choice = int(raw_input("Enter a choice: "))
#	assert choice in xrange(len(topics))
#	print wikipedia.summary(topics[choice])

#print(sushi.title)
#print(sushi.url)
#print(sushi.content)
#print(sushi.links[0])

#print(wikipedia.summary(search_term, sentences=1))
