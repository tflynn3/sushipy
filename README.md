# sushipy
Python Implementation of Sushi Go

<h2>Simulating a Game</h2>
To run, initialize a game with a number of players between 2 and 5. You can simulate random choices with the simulate method.

```python
my_game = Game()
my_game.simulate(print_rounds=True)
```

This will run a simulation and output round and final statistics.

```
----------------------------------------------------------------------------------------------------
Round 1
----------------------------------------------------------------------------------------------------
Player 1 Played Hand
[Pudding, Salmon Nigiri, Maki 1, Sashimi, Wasabi, Sashimi, Tempura, Salmon Nigiri, Tempura, Sashimi]
Player 1 Score: 26
Player 2 Played Hand
[Maki 2, Tempura, Salmon Nigiri, Pudding, Sashimi, Pudding, Dumpling, Egg Nigiri, Maki 2, Tempura]
Player 2 Score: 15
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
Round 2
----------------------------------------------------------------------------------------------------
Player 1 Played Hand
[Maki 3, Sashimi, Maki 2, Tempura, Tempura, Tempura, Salmon Nigiri, Maki 3, Salmon Nigiri, Maki 2]
Player 1 Score: 44
Player 2 Played Hand
[Egg Nigiri, Chopsticks, Sashimi, Dumpling, Squid Nigiri, Maki 1, Squid Nigiri, Salmon Nigiri, Chopsticks, Salmon Nigiri]
Player 2 Score: 27
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
Round 3
----------------------------------------------------------------------------------------------------
Player 1 Played Hand
[Maki 3, Sashimi, Tempura, Pudding, Wasabi, Maki 1, Maki 3, Chopsticks, Pudding, Sashimi]
Player 1 Score: 53
Player 2 Played Hand
[Tempura, Sashimi, Dumpling, Tempura, Maki 2, Wasabi, Salmon Nigiri, Maki 2, Dumpling, Sashimi]
Player 2 Score: 41
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
Final Score
----------------------------------------------------------------------------------------------------
Player 1 Number of Puddings: 3
Player 1 Final Score: 59
Player 2 Number of Puddings: 2
Player 2 Final Score: 35
----------------------------------------------------------------------------------------------------
```