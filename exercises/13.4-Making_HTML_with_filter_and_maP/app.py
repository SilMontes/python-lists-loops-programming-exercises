all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(color):
    return color["sexy"]==True

def filter_colors(): 
    sexy_colors=list(filter(generate_li,all_colors))
    sexy_colors_list=list(map(lambda color: "<li>"+color["label"]+"</li>",sexy_colors))
    no_comas_color_li="".join(sexy_colors_list)
    return no_comas_color_li
print(filter_colors())