import copy

punctuation_marks = (".,!?;:\"\'")

def my_cache_decorator(func):
    cache = {}  
    
    def wrapper(sentence, keywords):
        cache_key = (sentence, tuple(keywords))
        
        if cache_key in cache:
            print("The result was returned from the cache!")
            return copy.deepcopy(cache[cache_key])
        else:
            print("New calculation done...")
            result = func(sentence, keywords)
            cache[cache_key] = copy.deepcopy(result)
            return copy.deepcopy(result)
    
    return wrapper

def Remove_punctuation_marks(sentence):
    cleaned_sentence = ""
    for char in sentence:
        if char not in punctuation_marks:
            cleaned_sentence += char
    return cleaned_sentence

@my_cache_decorator
def Counting_words_in_a_sentence(sentence, keywords):
    
    cleaned_sentence = Remove_punctuation_marks(sentence)

    sentence1 = cleaned_sentence.split()
    sentence1_clean = []  
    
    for word in sentence1:
        lower_word = word.lower()  
        sentence1_clean.append(lower_word)
    keywords_lower = [keyword.lower() for keyword in keywords]
    
    result = {}
    for keyword in keywords_lower:
        count = sentence1_clean.count(keyword)
        result[keyword] = count
    
    return result


outcome = Counting_words_in_a_sentence("Apple is tasty. I like apple pie!", ["apple", "pie", "banana"])
print("outcome:", outcome)

outcome2 = Counting_words_in_a_sentence("Apple is tasty. I like apple pie!", ["apple", "pie", "banana"])
print("outcome2:", outcome2)