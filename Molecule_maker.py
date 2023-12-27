import requests

# Get user input for the molecule name
nameinput = input('What is the name of the molecule?')

# PubChem API endpoints and parameters
pugrest = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'
pugoper = 'property/CanonicalSMILES,MolecularWeight,MolecularFormula'
pugout = 'csv'
pugin = 'compound/name/' + nameinput
url = '/'.join([pugrest, pugin, pugoper, pugout])

# Make a request to PubChem API
res = requests.get(url)

# Print the request URL for reference
print("\nRequest URL:", url)

# Check if the request was successful (status code 200)
if res.status_code == 200:
    # Split the response into lines
    data_lines = res.text.strip().split('\n')
    
    # Check if there is data in the response
    if len(data_lines) > 1:
        # Split the data into fields
        data = data_lines[1].split(',')
        
        # Extract information from the data
        smiles = data[1].strip('"')
        mw = data[2].strip('"')
        formula = data[3].strip('"')
        
    
        # Print the information in a readable format
        print(f"\nMolecule: {nameinput}")
        print(f"Canonical SMILES: {smiles}")
        print(f"Molecular Weight: {mw} g/mol")
        print(f"Molecular Formula: {formula}")
    else:
        # Print a message if no information is found
        print(f"\nNo information found for the molecule: {nameinput}")
else:
    # Print an error message if the request fails
    print(f"\nFailed to retrieve information. Status Code: {res.status_code}")
