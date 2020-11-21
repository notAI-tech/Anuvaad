import os

# import nltk
try:
    nltk.download("punkt")
except:
    pass

import pydload
from transformers import T5Tokenizer, T5ForConditionalGeneration

MODEL_URLS = {
    "en-te": "",
    "en-ta": "",
    "en-kn": "",
    "en-ml": "",
    "en-mr": "",
    "en-hi": {
        "en_hi-pytorch_model.bin": "https://zenodo.org/record/4283362/files/en_hi-pytorch_model.bin?download=1",
        "en_hi-config.json": "https://zenodo.org/record/4283362/files/en_hi-config.json?download=1",
        "en_hi-special_tokens_map.json": "https://zenodo.org/record/4283362/files/en_hi-special_tokens_map.json?download=1",
        "en_hi-spiece.model": "https://zenodo.org/record/4283362/files/en_hi-spiece.model?download=1",
        "en_hi-tokenizer_config.json": "https://zenodo.org/record/4283362/files/en_hi-tokenizer_config.json?download=1",
    },
}

LANGUAGE_ALISASES = {
    "telugu": "te",
    "english": "en",
    "hindi": "hi",
    "kannada": "kn",
    "malayalam": "ml",
    "marathi": "mr",
}

_LANGUAGE_ALISASES = {v: k for v, k in LANGUAGE_ALISASES.items()}


class Anuvaad:
    tokenizer = None
    model = None
    source_lang = None
    target_lang = None

    def __init__(self, model_name):
        model_name = model_name.lower()
        for x, y in LANGUAGE_ALISASES.items():
            model_name = model_name.replace(x, y)

        if model_name not in MODEL_URLS:
            print(f"model_name should be one of {list(MODEL_URLS.keys())}")
            return None

        self.souece_lang, self.target_lang = model_name.split("-")

        home = os.path.expanduser("~")
        lang_path = os.path.join(home, ".Anuvaad_" + model_name)
        for file_name, url in MODEL_URLS[model_name]:
            file_path = os.path.join(lang_path, file_name)
            if os.path.exists(file_path):
                continue
            print(f"Downloading {file_name}")
            pydload.dload(url=url, save_to_path=file_path, max_time=None)

        self.tokenizer = T5Tokenizer.from_pretrained(lang_path)
        self.model = T5ForConditionalGeneration.from_pretrained(
            lang_path, return_dict=True
        )

        return True

    def anuvaad(
        sentence, source_lang=None, target_lang=None, beam_size=8, max_len=None
    ):
        if not source_lang:
            source_lang = self.source_lang.capitalize()
        if not target_lang:
            target_lang = self.target_lang.capitalize()

        input_ids = tokenizer(
            f"translate {source_lang} to {target_lang}: {sentence}", return_tensors="pt"
        ).input_ids
        print(input_ids)
        # print(tokenizer.decode(model.generate(input_ids, num_beams=beam_size, max_length=)[0]))
