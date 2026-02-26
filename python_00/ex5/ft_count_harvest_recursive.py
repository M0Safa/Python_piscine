def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def ft_recursive(day):
        if day > days:
            print("Harvest time!")
            return
        print("Day ", day)
        ft_recursive(day + 1)
    ft_recursive(1)
