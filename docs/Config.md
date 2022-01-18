# Config

## Structure

The configuration file is made up of the following properties:

-   `base`

    -   optional
    -   this property takes in a dictionary of schema names `schema` and integers `n`. The `schema` will then be generated `n` times

-   `generators`

    -   optional
    -   in this property you can define custom generators, based on their class name as the key and the file relativ to the configuration file as the value

-   `steps`
    -   optional
    -   here the sequence of steps for the user defined process can be defined. Each step has the property `generate`, which can be a schema name or a dictory of schema names and probabilities.
        Moreover, the property `next` signals, what step to take next.
-   `initial`
    -   optional
    -   this keyword signals sledo, which process step should be taken first
-   `amount`
    -   optional
    -   this keyword defines how many times the process should be executed
-   `schemas`
    -   required
    -   here all the referenced schemas can be defined. Schemas have a name and a list of `properties`. Each property has a `type` and can have different `options`. You can also reference other schemas, if they were generated beforehand, and their attributes (e.g. `$invoice.date`)
