import random

words_file = "10k.txt"
words = []

def load_words():
    global words
    with open(words_file,'r') as f:
        text=f.read()
    lines=text.split("\n")
    print(f"Read {len(lines)} lines")
    for l in lines:
        if not l.startswith("#"):
            words.append(l)
    print(f"Loaded {len(words)} words")

def is_word(word):
    for w in words:
        if w==word:
            return True

    return False

def shift_word(word,n):
    new_word=""
    for i in range(len(word)):
        new_i=(i-n)%len(word)
        new_word+=(word[new_i])
    return new_word

def demo_word_shift():
    for i in range(10):
        word = random.choice(words)
        shift_amount = random.randint(-1*len(word),1*len(word))
        shifted = shift_word(word,shift_amount)
        print(f"'{word}' >> {shift_amount} = '{shifted}'")

def analyze(word_length:int):
    # statistics
    stat_words=0
    stat_shifted_words=0
    stat_successful_words=0
    idx=0
    for w in words:
        if idx%600==0 and False:
            print(f"{idx}/{len(words)} = {int(idx/len(words)*1000)/10}")
        idx+=1
        if len(w)!=word_length:
            continue
        for i in range(1,len(w)):
            nw = shift_word(w,i)
            if is_word(nw):
                print(f"'{w}' >> {i} = '{nw}'")
                stat_successful_words+=1
            stat_shifted_words+=1
        #print(w)
        stat_words+=1
    print(f"Analyzed {stat_words} words")
    print(f"Analyzed {stat_shifted_words} shifted words")
    print(f"{stat_successful_words} words worked")

def main():
    global words
    load_words()
    for i in range(6,40):
        print(f"{i} letters")
        analyze(i)

if __name__=="__main__":
    main()
