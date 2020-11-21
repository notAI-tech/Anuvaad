from anuvaad import Anuvaad

import os
import logging

anu = Anuvaad(os.getenv("MODEL_NAME", "english-telugu"))

MAX_INPUT_LENGTH = int(os.getenv("MAX_INPUT_LENGTH", "200"))

def predictor(in_sents=[], batch_size=1):
    results = []
    in_sents = [in_sent[:MAX_INPUT_LENGTH] for in_sent in in_sents]

    while in_sents:
        try:
            batch = in_sents[:batch_size]
            in_sents = in_sents[batch_size:]
            result = anu.anuvaad(batch)
        except Exception as ex:
            logging.exception(ex, exc_info=True)
            result = [in_sent for in_sent in batch]

        results += result

    return seg.segment(in_texts)

