'''
Write a function `countScores(people)` that takes in an array of score
objects (people) as its input. A score object has two key-value pairs:
a name (string) and a score (number). `countScores(people)` should
return an object that has key-value pairs where each name is a key and
the value is their total score.

# Example 1

ppl = [ 
    {'name': "Pete", 'score': 10},
    {'name': "Mike", 'score' : 10},
    {'name': "Pete", 'score': -8},
    {'name': "Dexter", 'score': 12}
]

count_ppl = count_scores(ppl)
print(count_ppl); # => { Pete: 2, Mike: 10, Dexter: 12 }

# Example 2

peeps = [
  {'name': "Pete", 'score': 2},
  {'name': "Dexter", 'score': 2},
  {'name': "Mike", 'score': 2},
  {'name': "Dexter", 'score': 2},
  {'name': "Mike", 'score': 2},
  {'name': "Pete", 'score': 2},
  {'name': "Dexter", 'score': 2}
]
print(count_scores(peeps)); # => { Pete: 4, Mike: 4, Dexter: 6 }
'''


def count_scores(people):
    result = {}
    for person in people:
        name = person.get('name')
        score = person.get('score')
        print(name)
        if(not result.get(name)):
            result[name] = score
        else:
            result[name] += score
    return result


# Example 1

ppl = [
    {'name': "Pete", 'score': 10},
    {'name': "Mike", 'score': 10},
    {'name': "Pete", 'score': -8},
    {'name': "Dexter", 'score': 12}
]

count_ppl = count_scores(ppl)
print(count_ppl)  # => { Pete: 2, Mike: 10, Dexter: 12 }

# Example 2

peeps = [
    {'name': "Pete", 'score': 2},
    {'name': "Dexter", 'score': 2},
    {'name': "Mike", 'score': 2},
    {'name': "Dexter", 'score': 2},
    {'name': "Mike", 'score': 2},
    {'name': "Pete", 'score': 2},
    {'name': "Dexter", 'score': 2}
]
print(count_scores(peeps))  # => { Pete: 4, Mike: 4, Dexter: 6 }
