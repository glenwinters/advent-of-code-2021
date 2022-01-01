#!/usr/bin/env python3

from collections import defaultdict

NUMBER_BY_SEGS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def get_input():
    return open("./input.txt", "r").read().splitlines()


def translate(code, mapping):
    return "".join(sorted([mapping[letter] for letter in code]))


def ab():
    lines = get_input()

    answer_a = 0
    answer_b = 0
    for line in lines:
        chunks = line.split("|")
        segments = chunks[0].split()
        output = chunks[1].split()

        mapping = {}

        segbylen = defaultdict(list)
        for segment in segments:
            segbylen[len(segment)].append(segment)

        one = segbylen[2][0]
        four = segbylen[4][0]
        seven = segbylen[3][0]

        # Solve 'a'
        a_set = set(seven) - set(one)
        a = list(a_set)[0]
        mapping[a] = "a"

        # Get 'b' and 'd' possibilities
        bd_set = set(four) - set(one)

        # Identify 5
        five = next(filter(lambda seg: len(set(seg) - bd_set) == 3, segbylen[5]))
        five_set = set(five)

        # Identify 'c'
        c_set = set(one) - five_set
        c = list(c_set)[0]
        mapping[c] = "c"

        # Identify 'f'
        f_set = set(one) - c_set
        f = list(f_set)[0]
        mapping[f] = "f"

        # Identify 'g'
        g_set = five_set - bd_set - set(one) - a_set
        g = list(g_set)[0]
        mapping[g] = "g"

        # Identify 'd'
        # copy pasta to get where bd aren't both there - could be simpler
        other_five = next(filter(lambda seg: len(set(seg) - bd_set) == 4, segbylen[5]))
        d_set = bd_set & set(other_five)
        d = list(d_set)[0]
        mapping[d] = "d"

        # Identify 'b'
        b_set = bd_set - d_set
        b = list(b_set)[0]
        mapping[b] = "b"

        # Identify 'e'
        e_set = set("abcdefg") - set(mapping.keys())
        e = list(e_set)[0]
        mapping[e] = "e"

        translated_output = [translate(code, mapping) for code in output]

        numeric_output = [NUMBER_BY_SEGS[s] for s in translated_output]

        for num in numeric_output:
            if num in [1, 4, 7, 8]:
                answer_a += 1
        answer_b += (
            numeric_output[0] * 1000
            + numeric_output[1] * 100
            + numeric_output[2] * 10
            + numeric_output[3]
        )
    print(answer_a)
    print(answer_b)


# 7 seg has 7 segments, abcdefg
# 0 - 6 segs
# 1 - 2 segs
# 2 - 5 segs
# 3 - 5 segs
# 4 - 4 segs
# 5 - 5 segs
# 6 - 6 segs
# 7 - 3 segs
# 8 - 7 segs
# 9 - 6 segs

# 1. 1 is 2 segs (e.g. da)
# 2. 7 (3 segs) - 1 (2 segs) solves top (e.g. eda - da = e)
# 3. 4 (4 segs) - 1 (2 segs) narrows left (e.g. dcga - da = cg for top left and middle)
# 4. 5 segs (5) with both top left and middle is 5 solves bottom (gecba - cg - da - e = b)
#    and bottom right/top right (da intersect gecba = a which leaves top right = d)
# 5. Other 5 segs (2, 3)  don't have top left, solving middle/top left (cbfde only has c out of cg, so middle = c, top left = g)
# 6. Last remaining letter, is bottom left: f
#
# mapping:
# a is e
# b is g
# c is d
# d is c
# e is f
# f is a
# g is b
#
# Now take output code:
# bgefdac bdace ad agcd
#
# translate:
# gbaecfd gcfda fc fbdc
#
# sort
# abcdefg acdfg cf bcdf

# match number mappings
#
# 1 cf
# 2 acdeg
# 3 acdfg
# 4 bcdf
# 5 abdfg
# 6 abdefg
# 7 acf
# 8 abcdefg
# 9 abcdfg
# solution: 8 3 1 4

ab()
