def lyrics_generator(list_numbers):
    song=[]
    counter=0
    for number in list_numbers:
        if number == 0:
            song.append("Boom")
        else:
            if number==1:
                song.append("Drop the base")
                counter=counter+1
                if counter  == 3:
                    song.append("!!!Break the base!!!") 
    new_song=" ".join(song)                
    return new_song
            

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))