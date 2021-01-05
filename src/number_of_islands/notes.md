# Notes

Clearly a BFS/DFS problem with some extra guards once you "fall" off an island.

I decided to store the visited islands coordinates in a tuple in a set. After looking at the solutions is probably better to
simply overwrite the islands as you go to prevent revisiting.
