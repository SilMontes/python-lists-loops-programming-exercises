import itertools
chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    # option 1:  return merging_lists
    #merging_lists=list1+list2  

    #option 2:  return merging:lists
    #merging_lists= [name_1 for name_2 in [list1, list2] for name_1 in name_2]

    #option 3:  return merging:lists
    #merging_lists=[*list1,*list2]

    #option 4:
    merging_lists=list(itertools.chain(list1,list2))

    #merging_lists=list1
    #for names in list2:
    #    merging_lists.append(names)
        
    return merging_lists
print(merge_list(chunk_one, chunk_two))
