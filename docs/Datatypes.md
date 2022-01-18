# Datatypes

## Date

### id: `date`

### Description

This is used to generate random dates between the `min` and `max` values. The date that is generated is in the [ISO_8601](https://www.iso.org/iso-8601-date-and-time-format.html) format (YYYY-MM-DD).

### Options

-   `min`
    -   required: `true`
    -   can be a reference
    -   format: `YYYY-MM-DD`
-   `max`
    -   required
    -   can be a reference
    -   format: `YYYY-MM-DD`
-   `delta`

    -   optional
    -   format: `int >= 0`
    -   the number of days to add to the calculated date. Can not be used
        together with `delta_min` or `delta_max`

-   `delta_min`
    -   optional
    -   format: `int >= 0`
    -   the minimum number of days to add to the calculated date. Can not be used
        together with `delta`
-   `delta_max`
    -   optional
    -   format: `int >= 0`
    -   the minimum number of days to add to the calculated date. Can not be used
        together with `delta`

### Examples

`2021-12-02`

`2022-01-27`

## Number

### id: `number`

### Description

This is used to generate integers or floating point numbers, within the `min` and `max` range.

### Options

-   `min`
    -   required: `true`
    -   can be a reference
    -   format: float or integer
-   `max`
    -   required
    -   can be a reference
    -   format: float or integer
-   `digits`

    -   optional
    -   format: `int >= 0`
    -   the number of digits that should be shown after the comma.

### Examples

`8`

`13.954`

`19.29`

## Country

### id: `country`

### Description

Returns the name of a random country.

### Examples

`Gabon`

`Vatican City`

`Mexico`

## Name

### id: `name`

### Description

Returns a random name of a person.

### Examples

`Christine`

`Daniel`

`Michelle`
