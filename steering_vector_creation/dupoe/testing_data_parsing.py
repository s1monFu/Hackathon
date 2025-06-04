import json

with open('vector_steering_samples_full_balanced.json') as f: data = json.load(f)
positive_forward   = [r['forward_prompt']  for r in data['pos']]
positive_backward  = [r['backward_prompt'] for r in data['pos']]
negative_forward   = [r['forward_prompt']  for r in data['neg']]
negative_backward  = [r['backward_prompt'] for r in data['neg']]


print(f'Positive forward prompts: {len(positive_forward)}')
print(f'Positive backward prompts: {len(positive_backward)}')
print(f'Negative forward prompts: {len(negative_forward)}')
print(f'Negative backward prompts: {len(negative_backward)}')

print(f' First positive forward prompt: {positive_forward[0]}')
print(f' First positive backward prompt: {positive_backward[0]}')

print(f' First negative forward prompt: {negative_forward[0]}')
print(f' First negative backward prompt: {negative_backward[0]}')