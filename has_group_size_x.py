from collections import Counter
class Sol:
    def has_group_size_x(self,arr):
        counts=[count for word,count in Counter(arr).items()]
        return max(counts)==min(counts)


if __name__ == '__main__':
    p = Sol()
    print(p.has_group_size_x(arr=[1,1,1,2,2,2,3,3,3]))
