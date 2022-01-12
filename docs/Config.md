# Config

## Structure
The configuration file is setup in _amount, initial, steps and schemas_:
- __amount__ defines how many times the total process should take place
- __initial__ defines the first step within the process
- __steps__ within steps the sequence of steps are defined. Outlining what step comes after the current and the margin of error that can occur
- __schemas__ defines the data which will be created within the defined steps. These also define the frame of reference that the data will be created in


## Options
In the .yaml file you are able to define the sequence of steps by altering the values in __initial__ and __next__. In addition to this you can change the values within __schemas__ to change the frame in which the data will be created and also the generated types. In total you are able to change everything in the file, as long as the code supports it.

## Required Values
For the code to work, you must provide the values which are used within the code. In this case you must enter:
- The __amount__ of iterations the code must go through
- The __initial__ step with which the process starts (i.e. create_order)
- The __steps__ must be defined, with their __next__ steps as well as the values they are supposed to __generate__ in the given step (i.e. create_order, generate:Order, next: create_invoice). These reference the values in __schemas__.
- The __schemas__ must be defined, which define the frame in which the data will be generated in __min__ and __max__ values (i.e. min:2, max:4). These values must also have their __type__ defined, which allows the code to recognize what generator it should use
