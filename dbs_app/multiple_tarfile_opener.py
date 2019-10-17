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

	json_list = []
	with open('predictions.jsonl') as f:
		for line in f:
	            data = json.loads(line)
	            json_list.append(data['Classes'])
	print('\n')
	return json_list

# =============================================================================