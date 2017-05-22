import sys
current_word = None
current_count = 0
word = None
for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()
    # convert count (currently a string) to int
    try:
	# parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word
if current_word == word:
    #print '%s\t%s' % (current_word, current_count)
     classificacao=sorted(current_word, reverse=True)
     for current_word in classificacao[:1500]:
        print '%s\t%s' % (current_word, current_count)
