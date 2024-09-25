
list_cv= [{'user': 'john', 'jobs': ['analyst', 'engineer']},
       {'user': 'jane', 'jobs': ['finance', 'software']},{'user': 'ari', 'jobs': ['finance', 'software']}]

#4. Has_experience_as function
def has_experience_as(list_cv, job_title):
    list=[]
    for i in list_cv:
        if job_title in i['jobs']:

            list.append(i['user'])
    return list
            
#(5) auxiliary function. get distinct jobs in dict

def get_distinct_jobs(dict, list):
    
    for element in dict['jobs']:
            list.append(element)
    return list

#5. Job counts function

def job_counts(list_cv):
    dict={}
    list =[]
    for element in list_cv:
        #apply get distinct jobs previous function
        get_distinct_jobs(element,list)
    print(list)
    for element in list:
        if element not in dict.keys():
             dict.update({element: 1})
        else:
             dict[element]=dict[element]+1
    print(dict)
    return dict
        
 #6. Most popular job function   
        
def most_popular_job(list_cv):
    # Get the job counts
    counts = job_counts(list_cv)
    
    # Find the most popular job
    most_popular = max(counts, key=counts.get)  
    return (most_popular, counts[most_popular])

