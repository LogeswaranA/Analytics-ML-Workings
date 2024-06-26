sentence = "The quick brown fox jumps over the lazy dog"
first_letters = {word[0] for word in sentence.split() if len(word) > 3}
print(first_letters)


#Bring sorted chars
sentence = "The quick brown fox jumps over the lazy dog"
first_letters = sorted(list({word[2] for word in sentence.split() if len(word) > 3}))
print(first_letters)

#Print square value for each integer from 0 to 9
squares = sorted({x**2 for x in range(10)})
print(squares)

# Flatten a list of lists, but only include even numbers
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenmy_odds = [(num, 'even' if num % 2 ==0 else 'odd')   for sublist in nested_list for num in sublist]
flattened_evens = [num for sublist in nested_list for num in sublist if num % 2 == 0]
print(flattenmy_odds)
print(flattened_evens)
