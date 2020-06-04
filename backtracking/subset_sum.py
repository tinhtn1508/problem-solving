count = 0

def subset_sum(s, t, s_size, t_size, sum, ite, target):
    global count
    count += 1
    if target == sum:
        print(t[0:t_size])
        if ite + 1 < s_size:
            subset_sum(s, t, s_size, t_size - 1, sum - s[ite], ite+1, target)
        return
    else:
            for i in range(ite, s_size):
                t[t_size] = s[i]
                if sum + s[i] <= target:
                    subset_sum(s, t, s_size, t_size+1, sum + s[i], i+1, target)

def generate_subset(s, size, target):
    t = [0 for _ in range(size)]
    subset_sum(s, t, size, 0, 0, 0, target)

if __name__ == "__main__":
    weight = [10, 7, 5, 18, 12, 20, 15]
    generate_subset(weight, len(weight), 35)
    print(count)