import random
import string
from encoder import coder

c = coder()

def randomString(stringLength=100):
    """Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))

slist = [randomString() for x in range(10000)]
slist.append('''!@#$%&*()-_'"/?.,''')
false_count = 0
failed = []
for s in slist:
    original = s
    encoded = c.encode(original)
    decoded = c.decode(encoded)
    if not decoded == original:
        false_count += 1
        failed.append(original)

print(f'False count: {false_count}')
