Five Words, 25 Letters
---

This is an attempt to solve Matt Parker's problem from [this Youtube Video](https://www.youtube.com/watch?v=_-AfhLQfb6w).

Briefly; how many sets of 5 valid English words can you find that contain 25 distinct letters.

I don't think this solution is particularly clever; it just uses a dictionary to prune words from the candidate list which contain an already-used letter.


Wordlist (dict.txt) comes from https://github.com/tabatkins/wordle-list, and is available under the MIT license.