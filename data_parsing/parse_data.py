import os
import json

# 1. Determine the directory where this script lives, then build the JSON path
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, 'vector_steering_samples_full_balanced.json')

# 2. Load the JSON file
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

def rekey_and_clean(entries):
    """
    Given a list of entries (each entry should be a dict with a 'key' field),
    produce a new dict mapping entry['key'] -> {all other fields except
    'forward_prompt' and 'backward_prompt'}.

    If an entry is not a dict (e.g. a bare string), skip it.
    """
    cleaned = {}
    for entry in entries:
        if not isinstance(entry, dict):
            # If this entry is not a dict, skip it entirely.
            continue

        sample_key = entry.get('key')
        if sample_key is None:
            # If there's no 'key' field, skip as well.
            continue

        # Copy every (k,v) except 'forward_prompt' and 'backward_prompt'
        filtered = {
            k: v
            for k, v in entry.items()
            if k not in ('forward_prompt', 'backward_prompt')
        }
        cleaned[sample_key] = filtered
    return cleaned

# 3. Process 'pos' and 'neg' sections (or use empty list if missing)
pos_list = data.get('pos', [])
neg_list = data.get('neg', [])

pos_clean = rekey_and_clean(pos_list)
neg_clean = rekey_and_clean(neg_list)

# 4. Write out two separate JSON files in the same directory as this script
output_pos = os.path.join(script_dir, 'vector_steering_pos_clean.json')
output_neg = os.path.join(script_dir, 'vector_steering_neg_clean.json')

with open(output_pos, 'w', encoding='utf-8') as f_pos:
    json.dump(pos_clean, f_pos, indent=2)

with open(output_neg, 'w', encoding='utf-8') as f_neg:
    json.dump(neg_clean, f_neg, indent=2)

print(f"Created:\n  {output_pos}\n  {output_neg}")
