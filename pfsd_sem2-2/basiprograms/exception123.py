while True:
    try:
        n = int(input("Please enter an integer:"))
        m = int(input("please enter an integer:"))
        z = n/m
        print(z)
        break
    except Exception as e:
        print("Not an integer!please again 123")
        print(e)
    except ValueError:
        print("Not an integer! please again 456")
    finally:
        print("You successfully entered an integer!")