def histogram(l):
    s = set(l)
    histogram = {}
    for term in s:
        histogram[term] = 0
    
    for word in l:
        histogram[word] += 1

    return histogram
    
def clean(text):
    ignore_chars = [' ','\n', ',', '.', ':']
    for digit in range(10):
        ignore_chars.append(str(digit))

    text = text.lower() 
    newtxt = ''
    for c in text:
        if c not in ignore_chars:
            newtxt = newtxt + c
        else:
            newtxt = newtxt + ' '

    return newtxt

#main

with open('text.txt', 'r') as f:
    rawtext = f.read()
text = clean(rawtext)
words = text.split()

hist = histogram(words)

# Now we have our data. Next, visualize.

ranking = sorted(hist, key=lambda word: hist[word], reverse=True)

for i in range(10):
    print(ranking[i] + ': ' +  str(hist[ranking[i]]))


