#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity would be O(n). The number of inputs directly impacts how long the while loop runs.


b) Runtime complexity would be O(n^2). The number of inputs impacts both for loops. The second loop is nested inside and therefore the runtimes of both loops is O(n) and they are multiplied together resulting in a runtime of O(n^2).


c) Runtime complexity would be O(n). The function could also be written iteratively which will help illustrate the runtime:

    ```python

        def bunnyEars(bunnies):
            # keep track of the number of bunny ears
            count = 0

            # check each bunny passed in
            for i in range(bunnies):

                # for each bunny add 2 to the count of ears
                count += 2
      
            # return the total count of ears
            return count
    ```
    We can see easily in the iterative solution that the number of inputs impacts the runtime in linear time.

## Exercise II
    The runtime of this proposed solution would be O(log(n))

    ```python

    # we are given an n-story building and need to figure out
    # which floor we can drop and egg and it will not break
        # egg breaks if dropped >= f floor
        # egg doesn't break if dropped < f floor
    # we need to minimize dropped or broken eggs
    def find_floor(num_floors):
        # find the midpoint of the number of floors in the building
        mid = num_floors // 2

        # one base case
        # we find the floor when there is no more left in the searching list
        if len(num_floors) == 1:
            return mid

        # drop an egg and check if it breaks
        if mid >= 'broken egg':
            # if it breaks repeat this again on the lower half
            return find_floor(num_floors[:mid])
        # otherwise the egg didn't break and we need to check higher on the building
        else:
            return find_floor(num_floors[mid + 1:])

    ```
