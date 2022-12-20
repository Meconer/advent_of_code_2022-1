from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from helpers import adjacent, chunks, chunks_with_overlap, columns, custsort, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, positives, rays, rays_from_inside


class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


def solve(lines):
    first = None
    back = None
    nodes = []
    key = 1#811589153

    for line in lines:
        val = int(line) * key
        node = Node(val)

        if back:
            back.next = node
            node.prev = back
        else:
            first = node

        back = node
        nodes.append(node)

    first.prev = node
    node.next = first

    def printstartwith(n):
        for node in nodes:
            if node.val == n:
                vals = [node.val]
                moving = node
                for _ in range(len(nodes)-1):
                    moving = moving.next
                    vals.append(moving.val)
                print(vals)

    for i in range(1):
        print(i)
        for node in nodes:
            steps = abs(node.val) + len(nodes) #% len(nodes)
            forward = node.val > 0
            print(0)
            printstartwith(1)
            
            for x in range(steps):
                next = node.next
                nextnext = node.next.next
                prev = node.prev
                prevprev = node.prev.prev

                if forward:
                    node.next = nextnext
                    node.prev = next
                    next.next = node
                    next.prev = prev
                    nextnext.prev = node
                    prev.next = next
                else:
                    node.next = prev
                    node.prev = prevprev
                    next.prev = prev
                    prev.next = next
                    prev.prev = node
                    prevprev.next = node

                print(x+1)
                printstartwith(1)

            # for _ in range(steps-1):
            #     if forward:
            #         node = node.next
            #     else:
            #         node = node.prev

            #     next = node.next
            #     nextnext = node.next.next
            #     prev = node.prev
            #     prevprev = node.prev.prev

            #     if forward:
            #         node.next = nextnext
            #         node.prev = next
            #         next.next = node
            #         next.prev = prev
            #         nextnext.prev = node
            #         prev.next = next
            #     else:
            #         node.next = prev
            #         node.prev = prevprev
            #         next.prev = prev
            #         prev.next = next
            #         prev.prev = node
            #         prevprev.next = node

        # printstartwith(0)
        
    s = 0
    
    for node in nodes:
        if node.val == 0:
            moving = node

            for x in range(3000):
                moving = moving.next

                if x % 1000 == 999:
                    s += moving.val
                    print(x, moving.val)


    return s
                


def main():
    lines = []

    with open('20.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
