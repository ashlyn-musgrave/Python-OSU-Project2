# Name:Ashlyn Musgrave
# Course: CS261 - Data Structures
# Assignment:Assignment 2: Dynamic Array and ADT Implementation
# Due Date:Oct. 30, 2023
# Description: This assignment completes the implementation of a Dynamic Array


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method changes the underlying storage capacity for the elements in the dynamic array.
        """
        if new_capacity <= 0:
            return  # Do nothing if new_capacity is not a positive integer

        if new_capacity < self._size:
            return  # Do nothing if new_capacity is smaller than the current size

        # Create a new StaticArray with the new capacity
        new_data = StaticArray(new_capacity)

        # Copy the existing elements to the new StaticArray
        for i in range(self._size):
            new_data[i] = self._data[i]

        # Update the dynamic array's capacity and data reference
        self._capacity = new_capacity
        self._data = new_data

    def append(self, value: object) -> None:
        """
        Add a new element to the end of the array
        """

        # Check if the current size of the dynamic array is equal to the capacity
        # If equal, internal storage is full and needs to be doubled
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
            # Call resize method with new capacity value to ensure dynamic array can accommodate the new value
            self.resize(new_capacity)

        # Add the new value at the end of the array
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index in the dynamic array
        """

        # Checks if the index is within the valid range [O,N], raises an exception if it's not
        if index < 0 or index > self._size:
            raise DynamicArrayException

        # Check if the current size of the dynamic array is equal to the capacity
        # If equal, internal storage is full and needs to be doubled
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
            # Call resize method with new capacity value to ensure dynamic array can accommodate the new value
            self.resize(new_capacity)

        # Shift elements to the right to make space for the new value
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        # Insert the new value at the specified index
        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the element at the specified index in the dynamic array
        """

        # Checks if the index is within the valid range [O,N-1], raises an exception if it's not
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Invalid index")

        # Check if capacity reduction is needed
        if self._capacity > 10 and self._size < (self._capacity // 4):
            new_capacity = max(2 * self._size, 10)
            self.resize(new_capacity)

        # Remove the element at the specified index and shift it to the left to overwrite the element at the specified index
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size - 1] = None
        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        This method returns a new DynamicArray object that contains the requested number of elements
        from the original array, starting with the element located at the requested start index
        """

        # Checks if the start index is within the valid range [O,N-1], raises an exception if it's not
        if start_index < 0 or start_index >= self._size:
            raise DynamicArrayException("Invalid start_index")

        if size < 0:
            raise DynamicArrayException("Invalid size")

        if start_index + size > self._size:
            raise DynamicArrayException("Slice size exceeds available elements")

        # Create a new DynamicArray to store the extracted slice of elements
        sliced_array = DynamicArray()

        # Populate the new DynamicArray with the slice of elements
        # For each iteration it appends an element to the original array
        for i in range(start_index, start_index + size):
            sliced_array.append(self._data[i])

        return sliced_array

    def merge(self, second_da: "DynamicArray") -> None:
        """
        This method takes another DynamicArray object as a parameter, and appends all elements from this array
        onto the current one, in the same order in which they are stored in the input array
        """

        # Iterate through the second DynamicArray and append its elements to the current one
        for value in second_da:
            self.append(value)

    def map(self, map_func) -> "DynamicArray":
        """
        This method creates a new dynamic array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array.
        """
        # Create a new DynamicArray to store the mapped elements
        mapped_array = DynamicArray()

        # Apply map_func to each element in the original array and append the result to the new array
        for value in self:
            mapped_value = map_func(value)
            mapped_array.append(mapped_value)

        return mapped_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        This method creates a new dynamic array populated only with those elements from the
        original array for which filter_func returns True.
        """

        # Create a new DynamicArray to store the filtered elements
        filtered_array = DynamicArray()

        # Iterate through the original array and add elements to the filtered array if filter_func returns True
        for value in self:
            if filter_func(value):
                filtered_array.append(value)

        return filtered_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the dynamic array and returns the
        resulting value
        """

        # Iterate through all elements in the dynamic array and apply the reduction function
        result = initializer
        for i in range(self._size):
            if result is None:
                result = self._data[i]
            else:
                result = reduce_func(result, self._data[i])
        return result

def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    This method returns a tuple containing a dynamic array comprising the mode, value's of the array,
    and an integer that represents the highest frequency
    """

    # Checks if the input dynamic array is empty or has no elements
    # If empty, return a tuple containing an empty dynamic array and 0
    if not arr:
        return DynamicArray(), 0

    mode = DynamicArray() # Initialize an empty dynamic array
    max_frequency = 1
    current_frequency = 1
    current_value = arr[0]

    for i in range(1, arr.length()):
        # Checks current element at index [i] is equal to the current value and if so, increments the current_frequency
        if arr[i] == current_value:
            current_frequency += 1
        else:
            if current_frequency > max_frequency:
                mode = DynamicArray()
                mode.append(current_value)
                max_frequency = current_frequency
            elif current_frequency == max_frequency:
                mode.append(current_value)

            current_value = arr[i]
            current_frequency = 1

    # Check for cases where the mode is the last element in the array
    if current_frequency > max_frequency:
        mode = DynamicArray()
        mode.append(current_value)
    elif current_frequency == max_frequency:
        mode.append(current_value)

    return mode, max_frequency


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
