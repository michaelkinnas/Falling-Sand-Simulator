# Cellular Automata Simulations

A collection of visualizations of classic cellular automata and grid-based simulations.

## How to run and prerequisites

You will need **Python 3** and **PyGame** to run the projects in this repository.  

- Install Python 3: [https://www.python.org/](https://www.python.org/)  
- Install requirements: ```pip install -r requirements.txt```


Then you can run each simulation by going into each sub-directory and running

```bash
python3 main.py
```

## Implemented Projects

### Falling sands simulation

This project is a grid-based falling sands simulation where particles interact according to simple physics rules. Each update step applies local rules to cells, creating emergent behavior that mimics natural flowing and piling effects.

#### Instructions: 

- Left click: spawn particles
- Watch them fall, flow, and pile up

### Conway's game of life

This is a cellular automaton where simple rules applied to a grid of cells determine whether they live, die, or reproduce. Despite its simplicity, the system produces complex and often surprising patterns over time.

#### Instructions: 
- Left click: create cell. 
- Right click: remove cell. 
- Spacebar: Pause or resume simulation. 
- R: spawn random cells.