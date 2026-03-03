# Thoughtful

This is a submission for Thoughtful.

## Code

The `package.py` file consists of a `sort` function that identifies the stack the package belongs to, based on its dimensions and mass.

The packages are sorted based on the following criteria.

- A package is **bulky** if its volume (length * width * height) is greater than or equal to 1,000,000 cm^3 or any of its dimensions is at least 150 cm.
- A package is **heavy** if its mass is at least 20 kg.

The packages are then sorted into one of the stacks based on the following:

- **Rejected**: The package is heavy and bulky.
- **Special**: The package is heavy or bulky, but not both.
- **Standard**: The package is neither heavy nor bulky.

## Testing

To run the tests, run `python3 -m unittest`. This should automatically run the tests in `test_package.py`.