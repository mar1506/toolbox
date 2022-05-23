def find_it(seq):
    if len(seq)== 0:
        return None
    for num in seq:
        if seq.count(num) %2 != 0:
            return num

def duplicate_count(text):
    text = text.lower()
    duplicate_count=0
    for i in set(text):
        if text.count(i) >1:
            duplicate_count +=1

    return duplicate_count
