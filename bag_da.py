# Name: Ashlyn Musgrave
# Course: CS261 - Data Structures
# Assignment:Assignment 2: Dynamic Array and ADT Implementation
# Due Date:Oct. 30, 2023
# Description: This assignment completes the implementation of a Bag ADT


from dynamic_array import DynamicArray


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method adds a new element to the bag
        """

        # Add the value to the end of the array
        self._da.append(value)
        return

    def remove(self, value: object) -> bool:
        """
        This method removes any one element from the bag that matches the provided value object
        """

        for i in range(self._da.length()):
            # If the element at the current index [i] is equal to the value, remove the element at index [i]
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True

        return False

    def count(self, value: object) -> int:
        """
        This method returns the number of elements in the bag that match the provided value object
        """

        count = 0
        for i in range(self._da.length()):
            # If the element at the current index [i] is equal to the value, increment the count variable by 1
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        This method clears the contents of the bag.
        """

        # Assign a new empty dynamic array object to the instance variable, self._da (replaces all old bag contents)
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        This method compares the contents of a bag with the contents of a second bag provided as a parameter
        """

        # Compare sizes of the two bags by checking if the size of the first bag is not equal to the size of the second bag
        if self._da.length() != second_bag._da.length():
            return False

        # Iterate through the elements in the first bag
        for i in range(self._da.length()):
            element = self._da.get_at_index(i)

            # Check if the counts of the current element in both bags are the same
            if self.count(element) != second_bag.count(element):
                return False

        # If both size and elements match, return True
        return True

    def __iter__(self):
        """
        This method enables the Bag to iterate across itself
        """
        return BagIterator(self._da)

    def __next__(self):
        """
        This method will return the next item in the Bag, based on the current location of the iterator
        """
        return BagIterator(self._da)

# Create a separate class responsible for iterating over the contents of the bag
class BagIterator:

    def __init__(self, dynamic_array):
        self.dynamic_array = dynamic_array
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.dynamic_array.length():
            raise StopIteration

        value = self.dynamic_array.get_at_index(self.index)

        self.index = self.index + 1
        return value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
