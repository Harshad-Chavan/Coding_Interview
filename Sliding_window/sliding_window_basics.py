def fixed_window(temp, size):
    left = right = 0
    while right < len(temp):

        # 2) once window size is reached..start sliding i.e expand and shrink
        if right - left + 1 == size:
            print(temp[left : right + 1])
            left += 1
        # 1) this right first allows to reach the window size
        right += 1


if __name__ == "__main__":
    temp_list = list(range(7))
    print("temp_lsit =", temp_list)
    fixed_window(temp_list, 3)
