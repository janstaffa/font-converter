file = open("fonts.txt", "r")
for i in file:
    if i.find(','):
        sep = i.split(', ')
        name = sep[0]
    else:
        name = i
    converted = '<option style="font-family:'+i+';">'+name+'</option>'
    print(converted)
