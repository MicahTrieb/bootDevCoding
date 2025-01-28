#Lesson Link: https://www.boot.dev/lessons/6a98194e-36d3-4808-80ed-dee39e2269e8

def get_estimated_spread(audiences_followers):
    if audiences_followers:
        return ((sum(audiences_followers)/len(audiences_followers)) * len(audiences_followers) ** 1.2)
    else: 
        return 0
        
