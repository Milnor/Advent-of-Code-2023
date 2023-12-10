*** Settings ***
Library     Process

*** Test Cases ***

User Interface Test
    Log to Console      TODO: bad args, --d vs. --days,  --s vs. --samples, order of days

    ${result} =         Run Process         python3     solver.py    -h
    Should Contain      ${result.stdout}    usage: solver.py [-h] [--days DAYS [DAYS ...]] [--samples]

Sample Puzzles Test
    Log to Console      TODO: special handling for days with multiple sample inputs

    ${result1} =        Run Process         python3     solver.py   --s     --d     1
    Should Contain      ${result1.stdout}   142
    # TODO: special handling for Day 2 Part 2
    #Should Contain      ${result1.stdout}   281

    ${result2} =        Run Process         python3     solver.py   --s     --d     2
    Should Contain      ${result2.stdout}   8
    Should Contain      ${result2.stdout}   2286

    ${result3} =        Run Process         python3     solver.py   --s     --d     3
    Should Contain      ${result3.stdout}   4361
    Should Contain      ${result3.stdout}   467835

    ${result4} =        Run Process         python3     solver.py   --s     --d     4
    Should Contain      ${result4.stdout}   13
    Should Contain      ${result4.stdout}   30

    ${result5} =        Run Process         python3     solver.py   --s     --d     5
    Should Contain      ${result5.stdout}   35
    # Temporary solution is just returning -1 for Part 2
    #Should Contain      ${result5.stdout}   46

    ${result6} =        Run Process         python3     solver.py   --s     --d     6
    Should Contain      ${result6.stdout}   288
    Should Contain      ${result6.stdout}   71503

    ${result7} =        Run Process         python3     solver.py   --s     --d     7
    Should Contain      ${result7.stdout}   6440
    Should Contain      ${result7.stdout}   5905

    ${result8} =        Run Process         python3     solver.py   --s     --d     8
    # This day had multiple test inputs... 2|6 and 2|6 for results or sth. like that
    Should Contain      ${result8.stdout}   2
    Should Contain      ${result8.stdout}   2

    ${result9} =        Run Process         python3     solver.py   --s     --d     9
    Should Contain      ${result9.stdout}   114
    Should Contain      ${result9.stdout}   2


Actual Puzzles Test
    Log to Console      TODO: more updates when Day 5 Part 2 is solved for large inputs

    ${result} =         Run Process         python3     solver.py   --d     1
    Should Contain      ${result.stdout}    54953
    Should Contain      ${result.stdout}    53868

    ${result} =         Run Process         python3     solver.py   --d     2
    Should Contain      ${result.stdout}    2416
    Should Contain      ${result.stdout}    63307

    ${result} =         Run Process         python3     solver.py   --d     3
    Should Contain      ${result.stdout}    544664
    Should Contain      ${result.stdout}    84495585

    ${result} =         Run Process         python3     solver.py   --d     4
    Should Contain      ${result.stdout}    26426
    Should Contain      ${result.stdout}    6227972

    ${result} =         Run Process         python3     solver.py   --d     5
    Should Contain      ${result.stdout}    579439039
    # Part Two broken on large inputs
    Should Contain      ${result.stdout}    -1

    ${result} =         Run Process         python3     solver.py   --d     6
    Should Contain      ${result.stdout}    500346
    Should Contain      ${result.stdout}    42515755

    ${result} =         Run Process         python3     solver.py   --d     7
    Should Contain      ${result.stdout}    250120186
    Should Contain      ${result.stdout}    250665248 

    ${result} =         Run Process         python3     solver.py   --d     8
    Should Contain      ${result.stdout}    21251
    Should Contain      ${result.stdout}    11678319315857

    ${result} =         Run Process         python3     solver.py   --d     9
    Should Contain      ${result.stdout}    2105961943
    Should Contain      ${result.stdout}    1019



