# Maintenance Calculator

A simple Python tool to calculate key maintenance reliability metrics:

- **MTBF** (Mean Time Between Failures)
- **MTTR** (Mean Time To Repair)
- **Availability** (%)

## How it works

The program asks for three inputs:

1. Total running time (hours)
2. Number of failures
3. Total repair time (hours)

## Formulas

- MTBF = Total running time / Number of failures
- MTTR = Total repair time / Number of failures
- Availability = MTBF / (MTBF + MTTR) x 100

## How to run

```
python calculator.py
```

## Example

```
Total running time (hours): 1000
Number of failures: 5
Total repair time (hours): 25

MTBF: 200.0 hours
MTTR: 5.0 hours
Availability: 97.56 %
```

## Author

Md Hridoy Hossen