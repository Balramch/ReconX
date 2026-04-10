import tempfile

def build(domain, base_words, mutated_words):
    words = set()

    words.update(base_words)
    words.update(mutated_words)

    # Extract prefixes from known subs
    for sub in mutated_words:
        words.add(sub.split(".")[0])

    # Write to temp file
    tmp = tempfile.NamedTemporaryFile(delete=False, mode='w')
    
    for word in words:
        tmp.write(word + "\n")

    tmp.close()
    return tmp.name