with open('input.txt') as f:
    buffer, interval = f.readline(), int(input('Please enter the range: '))
    for i in range(len(buffer) - interval + 1):
        if len(set(buffer[i:i + interval])) == interval:
            print(i + interval)
            break
    