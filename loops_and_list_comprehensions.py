def main():
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    for planet in planets:
        print(planet, end=' ')

def main2():
    multiplicands = (2, 2, 2, 3, 3, 5)
    product = 1
    for mult in multiplicands:
        product = product * mult
        print('product = ' + str(product))

def main3():
    s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
    msg = ''
    #print all the uppercase letters in s, one at a time
    for char in s:
        if char.isupper():
            print(char, end=' ')

def main4():
    for i in range(5):
        print("Doing important work. i = ", i)

def main5():
    i = 0
    while i < 10:
        print(i, end = ' ')
        i += 1 #increase de value of i by 1

def main6():
    squares = [n**2 for n in range(10)]
    print(squares) 

def main7():
    squares = []
    for n in range(10):
        squares.append(n**2)
        print(squares)
    #print(squares)

def main8():
     planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
     short_planets = [planet for planet in planets if len(planet) < 6]
     print(short_planets)

     loud_short_planets = [planet.upper() + "!" for planet in planets if len(planet) < 6]
     print(loud_short_planets)
     
     planets_32 = [32 for planet in planets]
     print(planets_32)

def count_negatives(nums):
    """Return the number of negative numbers in the given list
    
    >>> count_regresives([5, -1, -2, 0, 3])
    """ 
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative += 1 
    return n_negative

def count_negatives2(nums):
    return len([num for num in nums if num <0])

def count_negatives3(nums):
    return sum([num<0 for num in nums])

if __name__ == '__main__':
    #main()
    #main2()
    #main3()
    #main4()
    #main5()
    #main6()
    #main7()
    #main8()
    print("1st solution: " + str(count_negatives ([-5, -4, 0, 1, 3, -8.9, -22.33])))
    print("2nd solution: " + str(count_negatives2([-5, -4, 0, 1, 3, -8.9, -22.33])))
    print("3rd solution: " + str(count_negatives3([-5, -4, 0, 1, 3, -8.9, -22.33])))