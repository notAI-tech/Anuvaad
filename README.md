# Anuvaad
State of the art translation models for Indic languages.


# Installation

```bash
# CPU pytorch will be installed if torch is not installed
pip install --upgrade anuvaad
```

# Usage

```python
from anuvaad import Anuvaad
anu = Anuvaad("english-telugu")

# Single sentence translation
# beam_size is optional and defaults to 4
anu.anuvaad("YS Jagan is the chief minister of Andhra Pradesh.")
# "వైఎస్ జగన్ ఆంధ్రప్రదేశ్ ముఖ్యమంత్రి."

# Batch translation
anu.anuvaad(["YS Jagan is the chief minister of Andhra Pradesh.",
            "Nara Lokesh suffered a humuliating defeat in Mangalagiri."])
# ['వైఎస్ జగన్ ఆంధ్రప్రదేశ్ ముఖ్యమంత్రి.', 'మంగళగిరిలో నారా లోకేష్కు ఘోర పరాజయం ఎదురైంది.']

```


|Available Models   | 
|--------|
|english-telugu | 
|english-tamil | 
|english-malayalam | 
|english-kannada | 
|english-marathi | 
|english-hindi | 
