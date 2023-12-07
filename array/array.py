def main():
    array = [1, 2, 3, 4, 5]
    print("All elements: ", array)
    array.pop()
    print("Removed last element: ", array)
    array.pop(0)
    print("Removed first element: ", array)
    array.append(5)
    print("Inserted at last element: ", array)
    array.insert(2,10)
    print("Inserted at position 2: ", array)
    print("found 10 at index", array.index(10))
    print("array is size:", len(array))




if __name__ == "__main__":
    main()