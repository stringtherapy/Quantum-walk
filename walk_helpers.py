# function to map to music

def map_to_music(one_d_walk_output,scale,starting_note):

    index = scale.index(starting_note)
    played = scale[index] + ','
    length = len(one_d_walk_output)
    scale_range = len(scale)

    for i in range(length):
        
        if one_d_walk_output[i] == '0':
            if (index - 1) != scale_range + 1 :   
                next_note = scale[index - 1]         # Shift one note DOWN
            else:
                next_note = scale[scale_range - 1]   # Transpose if out of scale
        else:
            if (index + 1) != scale_range :
                next_note = scale[index + 1]         # Shift one note UP
            else:
                next_note = scale[0]                 # Transpose if out of scale

        if i != (length-1):        
            played += next_note + ','
        else:
            played += next_note
            
        index = scale.index(next_note)

    return played


# function to outputs notes progression

def output_flow(notes_played,outputs):
    list1 = notes_played.split(',')
    list2 = ['←' if x == '0' else '→' for x in outputs]
    result = [None]*(len(list1)+len(list2))
    result[::2] = list1
    result[1::2] = list2
    return ' '.join(result)

# Generate plot

def generate_static_plot(index):
    xaxis = np.linspace(0, len(index), len(index))
    yaxis = np.array(index)
    
    fig, ax = plt.subplots()
    
    plt.step(xaxis, yaxis)
    plt.title("1D walkers")
    plt.xlabel("Length")
    plt.ylabel("Position")
    
    return ax