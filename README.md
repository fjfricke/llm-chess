# Chess AI

This project is a simple chess AI that uses the `chess` Python library and the `lmql` library to interact with the OpenAI GPT-3.5-turbo model. `lmql` is used to restrict the LLM's output to allowed moves only.

## Getting Started

To get a local copy up and running, you will need Python installed on your machine.

### Prerequisites

You need to install the following Python libraries:

- `chess`
- `random`
- `lmql`
- `asyncio`

This can be done using poetry. Fore more information, see the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Run the `main.py` script:

```bash
python main.py
```

The script will initialize a chess board and decide randomly if the AI or the human player starts the game. The game continues until a game over condition is met.

The AI uses the OpenAI GPT-3.5-turbo model to decide its moves. The AI's reasoning for each move is printed to the console.

The human player is asked to input their move. If the move is invalid, illegal, or ambiguous, the player is asked to input a new move. After each valid move, the AI provides feedback on the move.

## Authors

* **Felix Fricke** - *Initial work*

## License

This project is licensed under the MIT License.