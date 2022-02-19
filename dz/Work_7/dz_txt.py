f = open ('text', 'w')
f.write ('Follow the music')

f = open ('text', 'r')

while True:
    line = f.readline()
    if not line:
        break

    print(line.strip())
