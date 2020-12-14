class SmileChecker(): 
	def __init__(self): 
		self.text = ''

	def append_smile(self, value): 
		self.text += value
	
	def check_correct(self):
		a = self.text 
		
		while ':-(:-)' in a or ':-[:-]' in a or ':-{:-}' in a or ':-<:->' in a:
			a = a.replace(':-(:-)', '')
			a = a.replace(':-[:-]', '')
			a = a.replace(':-{:-}', '')
			a = a.replace(':-<:->', '')
		
		return not a


	