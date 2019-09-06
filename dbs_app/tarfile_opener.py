# ============================================================================= 
""" Extracts JSON File from .tar file in Local Storage  """
# =============================================================================

import tarfile
import json

def tarfile_open(name) :
	print("Initiated Opening tar file...")
	tar=tarfile.open(name, mode='r', fileobj=None)
	tar.list();
	tar.extractall()

	label = ""
	with open('predictions.jsonl') as f:
		for line in f:
	            data = json.loads(line)
	            label = data['Classes'][0]['Name']
	print('\n')
	return label

# =============================================================================