import string

class PunctuationRem:

	def read_article():
		with open('article.txt','r') as f:
			text = f.read()
		words = text.split()
		table =  str.maketrans('', '', string.punctuation)
		stripped = [w.translate(table) for w in words]
		return stripped
	




