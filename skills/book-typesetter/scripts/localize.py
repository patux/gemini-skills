import re
import sys

def localize_text(text):
    # Slang replacements (with word boundaries and case awareness)
    replacements = [
        (r'\bvale\b', 'está bien'),
        (r'\bVale\b', 'Está bien'),
        (r'\bVALE\b', 'ESTÁ BIEN'),
        
        (r'\bcapullo\b', 'idiota'),
        (r'\bCapullo\b', 'Idiota'),
        (r'\bCAPULLO\b', 'IDIOTA'),
        
        (r'\bflipas\b', 'alucinas'),
        (r'\bFlipas\b', 'Alucinas'),
        
        (r'\bjoder\b', 'maldición'),
        (r'\bJoder\b', 'Maldición'),
        (r'\bJODER\b', 'MALDICIÓN'),
        
        (r'\bcoche\b', 'carro'),
        (r'\bCoche\b', 'Carro'),
        (r'\bCOCHE\b', 'CARRO'),
        
        (r'\bordenador\b', 'computadora'),
        (r'\bOrdenador\b', 'Computadora'),
        (r'\bORDENADOR\b', 'COMPUTADORA'),
        
        # Vosotros pronouns
        (r'\bvosotros\b', 'ustedes'),
        (r'\bVosotros\b', 'Ustedes'),
        (r'\bVOSOTROS\b', 'USTEDES'),
        
        (r'\bvuestro\b', 'su'),
        (r'\bVuestro\b', 'Su'),
        (r'\bvuestra\b', 'su'),
        (r'\bVuestra\b', 'Su'),
        (r'\bvuestros\b', 'sus'),
        (r'\bVuestros\b', 'Sus'),
        (r'\bvuestras\b', 'sus'),
        (r'\bVuestras\b', 'Sus'),
    ]

    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)

    # Specific common vosotros verbs
    verbs = [
        (r'\bsois\b', 'son'), (r'\bSois\b', 'Son'), (r'\bSOIS\b', 'SON'),
        (r'\bhabéis\b', 'han'), (r'\bHabéis\b', 'Han'), (r'\bHABÉIS\b', 'HAN'),
        (r'\btenéis\b', 'tienen'), (r'\bTenéis\b', 'Tienen'), (r'\bTENÉIS\b', 'TIENEN'),
        (r'\bpodéis\b', 'pueden'), (r'\bPodéis\b', 'Pueden'), (r'\bPODÉIS\b', 'PUEDEN'),
        (r'\bqueréis\b', 'quieren'), (r'\bQueréis\b', 'Quieren'), (r'\bQUERÉIS\b', 'QUIEREN'),
        (r'\bvais\b', 'van'), (r'\bVais\b', 'Van'), (r'\bVAIS\b', 'VAN'),
        (r'\bhacéis\b', 'hacen'), (r'\bHacéis\b', 'Hacen'),
        (r'\bdecís\b', 'dicen'), (r'\bDecís\b', 'Dicen'),
        (r'\bdormís\b', 'duermen'), (r'\bDormís\b', 'Duermen'),
        (r'\bvenís\b', 'vienen'), (r'\bVenís\b', 'Vienen'),
        (r'\bsabéis\b', 'saben'), (r'\bSabéis\b', 'Saben'),
        (r'\bcreéis\b', 'creen'), (r'\bCreéis\b', 'Creen'),
        (r'\bqueríais\b', 'querían'), (r'\bQueríais\b', 'Querían'),
        (r'\bpodíais\b', 'podían'), (r'\bPodíais\b', 'Podían'),
        (r'\bibais\b', 'iban'), (r'\bIbais\b', 'Iban'),
        (r'\beraís\b', 'eran'), (r'\bEraís\b', 'Eran'),
    ]

    for pattern, replacement in verbs:
        text = re.sub(pattern, replacement, text)

    # Reflexive 'os' + verb (e.g. 'os calmáis' -> 'se calman')
    # This is a bit broad, but let's try to capture 'os' followed by common 'áis/éis/ís' verbs
    text = re.sub(r'\bos\s+([a-z]+)áis\b', r'se \1an', text)
    text = re.sub(r'\bos\s+([a-z]+)éis\b', r'se \1en', text)
    text = re.sub(r'\bos\s+([a-z]+)ís\b', r'se \1en', text)
    
    # Capitalized version
    text = re.sub(r'\bOs\s+([a-z]+)áis\b', r'Se \1an', text)
    text = re.sub(r'\bOs\s+([a-z]+)éis\b', r'Se \1en', text)
    text = re.sub(r'\bOs\s+([a-z]+)ís\b', r'Se \1en', text)

    # Object 'os' -> 'les' or 'los'
    # 'os' as indirect object is common.
    # We will use 'les' as a safe general plural replacement for 'os' when it's not handled by the reflexive rule above.
    # Note: 'los' might be more accurate for direct object, but 'les' is often used. 
    # Let's try to be a bit smarter or just pick one. The user said 'les/los'.
    # I'll use 'les' for 'os' as it's very common in LatAm to use 'les' for 'ustedes'.
    
    # But wait, 'os dije' -> 'les dije' is correct.
    # 'os llamaré' -> 'los llamaré' is direct object.
    # Without full parsing it's hard. 'les' is generally acceptable in many regions (leísmo for 'ustedes' is very common).
    # Actually, in most of LatAm, for 'ustedes' (plural), the direct object is 'los/las' and indirect is 'les'.
    
    # Let's use 'les' for now as a general fallback for 'os'.
    text = re.sub(r'\bos\b', 'les', text)
    text = re.sub(r'\bOs\b', 'Les', text)
    text = re.sub(r'\bOS\b', 'LES', text)

    # General 'áis', 'éis', 'ís' verb endings (remaining ones)
    # Be careful not to match words like 'país', 'maíz', 'crisis', etc.
    # We only want verbs. Usually these have 3+ letters before the ending.
    text = re.sub(r'\b([a-z]{2,})áis\b', r'\1an', text)
    text = re.sub(r'\b([a-z]{2,})éis\b', r'\1en', text)
    # For 'ís', it's harder because of 'país'. 
    # Verbs usually have more context or specific endings.
    # Let's avoid general 'ís' for now and only do it if preceded by 'os' (already done) or known verbs.
    # Or common ones:
    text = re.sub(r'\b(ven|dec|dorm|segu|part|re|sal)ís\b', r'\1en', text)

    return text

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        # Only process lines that are not timestamps or numbers
        if re.match(r'^\d+$', line.strip()) or '-->' in line:
            processed_lines.append(line)
        else:
            processed_lines.append(localize_text(line))

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_file(sys.argv[1])
    else:
        print("Usage: python localize.py <file_path>")
