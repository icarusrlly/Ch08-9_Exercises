import re
import urllib.request

def count_pale_variants(url):
    pattern = r'\b(pale|pales|paled|paleness|pallor)\b'
    count = 0
    response = urllib.request.urlopen(url)
    for line in response:
        line_text = line.decode('utf-8')
        if re.search(pattern, line_text, re.IGNORECASE):
            count += 1
    return count

book_url = "https://www.gutenberg.org/ebooks/1184.txt.utf-8"

try:
    result = count_pale_variants(book_url)
    print(f"Number of lines containing 'pale' variants: {result}")
except Exception as e:
    print(f"Could not retrieve the book: {e}")
