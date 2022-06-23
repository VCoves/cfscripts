#!/usr/bin/env python3

from os import system, chdir
from pathlib import Path
from textwrap import wrap, dedent
from sys import exit

path = Path(__file__).parent.resolve()
chdir(path)

system("tree -a ./dailyacs")

me="by William Bille Meyling (cf: WillTheBill, github: willthbill)"

# name
# command
# description
# credit
scripts = [
        (
            "Daily ACs",
            "./dailyacs",
            """
            Finds problems solved on each day along with their rating.
            """,
            me,
        ),
        (
            "Comulative AC count",
            "pipenv run comuaccount",
            """
            Count how many problems solved since a spefific date.
            """,
            me,
        ),
        (
            "Range rank",
            "pipenv run rangerank",
            """
            In an official contest, where did you rank among the contestants within a given rating range around your rating (the rating at the time of participating).
            """,
            me,
        ),
        (
            "Virtual Performance",
            "pipenv run virtualperformance",
            "Calculate rank/delta/performance of virtual/unofficial/offical contests.",
            me
        ),
        (
            "Unsolved Contest Problems",
            "pipenv run unsolvedcontestproblems",
            """
            Find unsolved problems from contests with at least one submission. Why? Because you don't want to spoil nice unsolved virtuals. Handles div1/div2 contests where a problem occurs in both.
            """,
            me
        ),
        (
            "What if?",
            "pipenv run whatif",
            """
What If Codeforces virtual contests / unofficial participations were official? Calculates new ratings using deltas and simulates the past n contests.
            """,
            me
        ),
]

def main():

    print("Welcome to cftools - a collection of scripts using the CodeForces API")
    print("- created and maintained by", me)
    print()

    print("Choose a script")
    for i in range(len(scripts)):
        print("{}: {}".format(i + 1, scripts[i][0]))
    choice = int(input("Script number (1-{}): ".format(len(scripts))))
    assert(1 <= choice <= len(scripts))
    choice -= 1

    def print_script_info(script):
        firstline="============={}=============".format(script[0])
        print(firstline)
        print(*wrap(dedent(script[2]).strip(), 80), sep="\n")
        print("--------------")
        print(*wrap(dedent(script[3]).strip(), 80), sep="\n")
        print("=" * len(firstline))

    print()
    print_script_info(scripts[choice])
    print()

    system(scripts[choice][1])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit(1)
    exit(0)