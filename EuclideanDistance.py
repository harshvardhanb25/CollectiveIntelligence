from math import sqrt
from recommendations import critics

def euclid(critics:dict, critic1:str, critic2:str, movie1:str, movie2:str):
    '''Calculates the Euclidean Distance Score for two critics in
    the critic dictionary. The calculation is done for any two movies provided
    as the 4th and 5th args.
    '''
    try:
        s1c1=critics[critic1][movie1]
        s1c2=critics[critic1][movie2]
        s2c1=critics[critic2][movie1]
        s2c2=critics[critic2][movie2]
        dist = sqrt((s1c1 - s2c1)**2 + (s1c2 - s2c2)**2)
        score = 1/(dist+1);
        return dist
    except KeyError:
        print("Invalid Critic-Movie combination")
        exit(1)


def main():
    '''Tests the euclid function by running for Mick LaSalle and Toby for
    movies "Snakes on a Plane" and "You, Me and Dupree"'''
    score = euclid(critics, 'Toby', 'Mick LaSalle', 'Snakes on a Plane', 'You, Me and Dupree')
    print(score)

if __name__=="__main__":
    main()