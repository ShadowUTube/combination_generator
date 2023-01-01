# Create an empty array to store each permutation
permutations = []

# Function to permutate a given array
def permutate(array):
  # If array only has one element, return it
  if len(array) == 1:
    return array

  # Initialize empty array of permutations
  permutations = []

  # Iterate over each element in the array
  for i in range(len(array)):
    # Create a shallow copy of the array
    remainder = array[:]
    # Splice out the current element from the copy
    current = remainder.pop(i)
    # Create a deeper copy of the remainder array
    recursiveArray = remainder[:]
    # Use recursion to iterate over sub-arrays
    for permutation in permutate(recursiveArray):
      # Push the current element and each permutation of the sub-array into the empty array
      permutations.append([current] + list(permutation))
  # Return the permutations array
  return permutations


# Function to read a text file
def readTextFile(file):
  # Create a new instance of the File System Object
  fso = open(file, 'r')
  # Read the contents of the file
  contents = fso.read()
  # Close the file
  fso.close()
  # Return the response
  return contents

# Function to write a text file
def writeTextFile(filename, text):
  # Create a new instance of the File System Object
  fso = open(filename, 'w')
  # Write the text to the file
  fso.write(text)
  # Close the file
  fso.close()

# Read the input text file
input = readTextFile("input.txt")
# Split the input text into an array
inputArray = input.split("\n")
# Create an array of permutations
permutationsArray = permutate(inputArray)
# Initialize an empty string to store the output
output = ""
# Iterate over each permutation in the permutations array
for permutation in permutationsArray:
  # Iterate over each element in the current permutation
  for element in permutation:
    # Add the element to the output string
    output += element + "\n"
  # Add a new line after each permutation
  output += "\n"
# Write the output to a text file
writeTextFile("output.txt", output)
