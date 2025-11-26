def reverse_words(sentence):
    end = start = len(sentence) - 1
    response = ""
    separator = ""
    
    while end >= 0:
        while end >= 0 and sentence[end] == " ":
            end -= 1
        start = end
        while start >= 0 and sentence[start] != " ":
            start -= 1
        if len(response) > 0:
            separator = " "
        if end > start:
            response = response + separator + sentence[start+1:end+1]
        end = start
        
    return response
