male_str = ["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man","msle", "mail", "malr","cis man", "Cis Male", "cis male"]
trans_str = ["trans-female", "something kinda male?", "queer/she/they", "non-binary","nah", "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous", "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer", "ostensibly male, unsure what that really means"]           
female_str = ["cis female", "f", "female", "woman",  "femake", "female ","cis-female/femme", "female (cis)", "femail"]


gender_mapping = {
    "male": "male",
    "m": "male",
    "make": "male",
    "cis male": "male",
    "man": "male",
    "male leaning androgynous": "trans",
    "msle": "male",
    "mail": "male",
    "malr": "male",
    "cis man": "male",
    "male (cis)": "male",
    "male-ish": "male",
    "maile": "male",
    "mal": "male",

    "female": "female",
    "f": "female",
    "woman": "female",
    "cis-female/femme": "female",
    "femail": "female",
    "cis female": "female",
    "femake": "female",
    "female (cis)": "female",
    

    "trans": "trans",
    "trans woman": "trans",
    "neuter": "trans",
    "queer": "trans",
    # "a little about you": "trans",
    # "p": "trans",
    "fluid": "trans",
    "androgyne": "trans",
    "non-binary": "trans",
    "nah": "trans",
    "all": "trans",
    "enby": "trans",
    "genderqueer": "trans",
    "ostensibly male, unsure what that really means": "trans",
    "trans-female": "trans",
    "guy (-ish) ^_^": "trans",
    "female (trans)": "trans",
    "queer/she/they": "trans",
    "something kinda male?": "trans",
    "agender": "trans",
}

mc = 0
fc = 0
tc = 0

print(len(male_str),len(female_str),len(trans_str))

for (k, v) in gender_mapping.items():
    if v == 'male':
        mc += 1
        if k in male_str:
            male_str.remove(k)
    
    if v == 'female':
        fc += 1
        if k in female_str:
            female_str.remove(k)
    
    if v == 'trans':
        tc += 1
        if k in trans_str:
            trans_str.remove(k)

print(mc,fc,tc)



print((male_str),(female_str),(trans_str))
    
