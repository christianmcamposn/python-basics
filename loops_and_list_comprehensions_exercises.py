def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    number_flag = False
    for num in nums:
        print(num)
        if num % 7 == 0:
            number_flag = True
            print(number_flag)
            return number_flag
        else:
            pass
    number_flag = False
    print(number_flag)
    return number_flag

def has_lucky_numbers2(nums):
    return any([num % 7 == 0 for num in nums])

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return ([n>thresh for n in L])

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    boring_flag = False

    for cont in range(len(meals)-1):
        if meals[cont] == meals[cont+1]:
            print(meals[cont] + ' - ' + meals[cont+1])
            boring_flag = True
            return boring_flag
    return boring_flag

def estimate_average_slot_payout(n_runs):
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout
    
def main():
    #result = has_lucky_numbers2(list([1,2,3,4,0,5,6]))
    
    #result = elementwise_greater_than(list([-3, -2, -1, 0, 1, 2, 3, 4]), 0)
    
    meals = ['Pizza', 'Pork ribs' 'Pizza', 'Fried chicken', 'Fried chicken', 'Tacos al pastor', 'Salad and pasta', 'Salad and pasta', 'Tacos al pastor', 'Fajitas de pollo', 'Salad']
    #result = menu_is_boring(meals)
    
    print(result)



if __name__ == '__main__':
    main()