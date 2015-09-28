lines = []
with open('wordStat.txt') as f:
  for line in f:
    (word, count) = line[:-2].split(' ')
    lines.append(' ' * 10 + "'" + word + "': " + str(count))
with open('wordStat.out', 'w') as f:
  f.write(',\n'.join(lines))
