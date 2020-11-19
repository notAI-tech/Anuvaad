import os
import pydload

MODEL_URLS = {
	"en-multi": "",
	"en-te": "",
	"en-ta": "",
	"en-kn": "",
	"en-ml": "",
	"en-mr": "",
}

LANGUAGE_ALISASES = {
	"telugu": "te",
	"english": "en",
	"hindi": "hi",
	"kannada": "kn",
	"malayalam": "ml",
	"marathi": "mr"
}

class Anuvada:
	tokenizer = None
	model = None
	
	def __init__(self, model_name):
		model_name = model_name.lower()
		for x, y in LANGUAGE_ALISASES.items():
			model_name = model_name.replace(x, y)
		
		if model_name not in MODEL_URLS:
			print(f"model_name should be one of {list(MODEL_URLS.keys())}")
			return None
		
		
		
