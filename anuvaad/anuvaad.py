import os
import torch
import pydload
from transformers import T5Tokenizer, T5ForConditionalGeneration

MODEL_URLS = {
    "en-te": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_te-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_te-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_te-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_te-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_te-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_te-tokenizer_config.json",
    },
    "en-ta": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ta-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ta-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ta-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ta-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ta-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ta-tokenizer_config.json",
    },
    "en-kn": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_kn-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_kn-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_kn-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_kn-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_kn-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_kn-tokenizer_config.json",
    },
    "en-ml": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ml-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ml-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ml-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ml-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ml-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_ml-tokenizer_config.json",
    },
    "en-mr": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_mr-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_mr-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_mr-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_mr-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_mr-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_mr-tokenizer_config.json",
    },
    "en-hi": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_hi-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_hi-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_hi-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_hi-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_hi-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_hi-tokenizer_config.json",
    },
    "en-bn": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_bn-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_bn-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_bn-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_bn-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_bn-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_bn-tokenizer_config.json",
    },
    "en-gu": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_gu-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_gu-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_gu-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_gu-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_gu-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_gu-tokenizer_config.json",
    },
    "en-pa": {
        "pytorch_model.bin": [
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_pa-pytorch_model.bin.xaa",
            "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_pa-pytorch_model.bin.xab",
        ],
        "config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_pa-config.json",
        "special_tokens_map.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_pa-special_tokens_map.json",
        "spiece.model": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_pa-spiece.model",
        "tokenizer_config.json": "https://github.com/notAI-tech/Anuvaad/releases/download/v1-checkpoints/en_pa-tokenizer_config.json",
    },
}

LANGUAGE_ALISASES = {
    "telugu": "te",
    "tamil": "ta",
    "english": "en",
    "hindi": "hi",
    "kannada": "kn",
    "malayalam": "ml",
    "marathi": "mr",
    "punjabi": "pa",
    "gujarati": "gu",
    "bengali": "bn",
}

_LANGUAGE_ALISASES = {v: k for k, v in LANGUAGE_ALISASES.items()}


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

        self.source_lang, self.target_lang = model_name.split("-")
        self.source_lang = _LANGUAGE_ALISASES[self.source_lang]
        self.target_lang = _LANGUAGE_ALISASES[self.target_lang]

        home = os.path.expanduser("~")
        lang_path = os.path.join(home, ".Anuvaad_" + model_name)
        if not os.path.exists(lang_path):
            os.mkdir(lang_path)

        for file_name, url in MODEL_URLS[model_name].items():
            file_path = os.path.join(lang_path, file_name)
            if os.path.exists(file_path):
                continue
            print(f"Downloading {file_name}")
            pydload.dload(url=url, save_to_path=file_path, max_time=None)

        self.tokenizer = T5Tokenizer.from_pretrained(lang_path)
        self.model = T5ForConditionalGeneration.from_pretrained(
            lang_path, return_dict=True
        )

        if torch.cuda.is_available():
            print(f"Using GPU")
            self.model = self.model.cuda()

    def anuvaad(
        self, sentences, source_lang=None, target_lang=None, beam_size=4, max_len=None
    ):
        return_single = True
        if isinstance(sentences, list):
            return_single = False
        else:
            sentences = [sentences]

        if not source_lang:
            source_lang = self.source_lang.capitalize()
        if not target_lang:
            target_lang = self.target_lang.capitalize()
        if not max_len:
            max_len = 512

        input_ids = self.tokenizer(
            [
                f"translate {source_lang} to {target_lang}: {sentence}"
                for sentence in sentences
            ],
            return_tensors="pt",
            padding=True,
        ).input_ids

        if torch.cuda.is_available():
            input_ids = input_ids.to("cuda")

        output_ids = self.model.generate(
            input_ids, num_beams=beam_size, max_length=max_len
        )

        outputs = [
            self.tokenizer.decode(output_id, skip_special_tokens=True)
            for output_id in output_ids
        ]

        if return_single:
            outputs = outputs[0]

        return outputs
