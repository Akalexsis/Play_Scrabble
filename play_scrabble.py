letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# use dict comprehension to create dict using var letters, points
letter_to_points = {key:value for key, value in zip(letters, points)}

# add 0 points if key is blank
letter_to_points[' '] = 0
print(letter_to_points)

# finds total points per word
def score_word(word):
  point_total = 0

  # adds points for each letter in word
  for w in word.upper():
    #use .get() method to add points if letter not in dict
    point_total += letter_to_points.get(w, 0)
  return point_total

# expected output: 15
brownie_points = print(score_word('brownie'))

player_to_words = { 
  'player1': ['blue', 'tennis', 'exit'], 'wordNerd': ['earth', 'eyes', 'machine'],
  'Lexi Con': ['eraser', 'belly', 'husky'],
  'Prof Reader': ['zap', 'coma', 'period'] }

# holds total points per player
player_to_points = {}

# creates dict with total points for each player
def player_points():
  # holds total points per player
  player_to_points = {}

  # finds total points per player
  for player, words in player_to_words.items():
    # clears point total for next player
    player_points = 0

    # finds the points for each word
    for w in words:
      player_points += score_word(w)
    
    # adds player and associated points to player_to_points
    player_to_points[player] = player_points

print(player_to_points)