# Importing necessary library
import math
import re
from collections import Counter

# Regex to match alphanumeric characters and underscore with 1 or more repetitions.
word = re.compile(r'\w+')

def textToVector(text):
    """Function to convert text to vector
    Args: text (str): Text to be converted to vector
    Returns: Dict """
    words = word.findall(text)
    return Counter(words)

def cosineDistance(vec_1, vec_2):
    """Function to calculate cosine distance
    Args: vec_1 (dict): Vector 1
    Args: vec_2 (dict): Vector 2
    Returns: float """
    intersection = set(vec_1.keys()) & set(vec_2.keys())
    numerator = sum([vec_1[x] * vec_2[x] for x in intersection])

    sum1 = sum([vec_1[x]**2 for x in vec_1.keys()])
    sum2 = sum([vec_2[x]**2 for x in vec_2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def readFile(file_name):
    """Function to read file
    Args: file_name (str): File name
    Returns: str """
    return open("data/" + file_name, 'r').read() 

text1 = readFile("doc1.txt")
text2 = readFile("doc2.txt")

vector1 = textToVector(text1)
vector2 = textToVector(text2)

print("Cosine distance between the two vectors is: ", cosineDistance(vector1, vector2))
