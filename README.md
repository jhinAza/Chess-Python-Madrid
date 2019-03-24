# Chess MinMax simulator

The purpose of this project is to serve as a template for a MinMax demonstration using a Chess in a predefined state.

## How it works

## Establishing a predefined state

The state of the game is defined in the file state.yaml. This file it's divided in the keys `black` and `white`.

Each piece of the game needs to be defined if we want it to be there. If there is some piece missing it won't be added 
to the game. But if any type of piece has more pieces that the ones allowed by the rules the validator will raise a exception.

This means that each color can have at most:

1. One King. Not one more, not one less
2. One Queen at most
3. Two Bishops at most
4. Two Knights at most
5. Two Towers at most
6. Eight Pawns at most

## Installing the project

Installing this project is fairly simple. Just follow these steps.

1. Clone the repository

``` bash
    git clone ssh://git@github.com/repository
```

2. Install Python3 if isn't already installed. Go to [http://www.python.org] and download the last version. 

3. Create a virtualenv for this project

``` bash
    python3 -m venv venv
```

4. Install the requirements
``` bash
    source venv/bin/activate
    pip install -r requirements.txt
```

## Run the project

``` bash
    source venv/bin/activate
    python chess.py
```