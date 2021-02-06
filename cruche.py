
def verser(s, i, j, capacities):
  maximum = capacities[j] - s[j]
  aVerser = min(maximum,s[i])
  restant = s[i]-aVerser

  l = list(s[:3])
  l[i] = restant
  l[j] = s[j] + aVerser
  return l

def nextStates(state, states,capacities):
  l = []

  for i in range(3):
    for j in range(3):
      if i!=j:
        a = tuple(verser(state,i,j,capacities))  + state[:3]
        if not a[:3] in states:
          l.append(a)
          states.add(a[:3])
  return l

def reconstruire(path, final):
  l = [final]
  for a in path[::-1]:
    if a[:3] == l[-1]:
      l.append(a[3:])
  return l[::-1][1:]

states = {(8,0,0)}
capacities = [8,5,3]
current = (8,0,0)
final = (4,4,0)
stack = [current]
path = [current]

while current != final:
  stack.extend(nextStates(current, states, capacities))
  if not stack:break
  current = stack.pop(0)
  path.append(current)

solution = reconstruire(path, final)
print("la suite des actions effectuees est :\n", solution, "\nLe nombre d'etape est ", len(solution)-1)
