![Python application](https://github.com/blinzki/COVID19/workflows/Python%20application/badge.svg)

>Author        : Ing. Pablo Eduardo Romero Oestreicher

>Last Update   : 2020-05-19

# Rosario COVID-19

Evolution of COVID 19 - Official reports

Rosario, Santa Fe, Argentina

![SEIR Model COVID-19](/img/seir-covid19-2020-05-19.png)

## Data COVID-19

```

Rosario, Argentina
Country Code:AR
City Code   :2000

day       Date   Confirmed    Suspected   R0_R    R_P  Prediction
 00 2020-03-14           0            0      -      -           -
 01 2020-03-15           1            0      -      -           -
 02 2020-03-16           1            0      -      -           -
 03 2020-03-17           1           12      -      -           -
 04 2020-03-18           1           22      -      -           -
 05 2020-03-19           2           15      -      -           -
 06 2020-03-20           2           14      -      -           -
 07 2020-03-21           2           25      -      -           -
 08 2020-03-22           2           23      -      -           -
 09 2020-03-23           3           19      -      -           -
 10 2020-03-24           8           26      -      -           -
 11 2020-03-25           8           24      -      -           -
 12 2020-03-26          12           24      -      -           -
 13 2020-03-27          20           23      -      -           -
 14 2020-03-28          23           24      -      -           -
 15 2020-03-29          33           28      -      -           -
 16 2020-03-30          44           29      -      -           -
 17 2020-03-31          51           35      -      -           -
 18 2020-04-01          56           61      -      -           -
 19 2020-04-02          58           70      -      -           -
 20 2020-04-03          65           69      -      -           - 
 21 2020-04-04          68           59      -      -           - 
 22 2020-04-05          73           21      -      -           - 
 23 2020-04-06          76           66      -      -           - 
 24 2020-04-07          77           97      -      -           - 
 25 2020-04-08          79           49      -      -           - 
 26 2020-04-09          79           88      -      -           - 
 27 2020-04-10          80           40      -      -           - 
 28 2020-04-11          81           51      -      -           - 
 29 2020-04-12          84           36      -      -           - 
 30 2020-04-13          85           33      -      -           - 
 31 2020-04-14          85           40      -      -           - 
 32 2020-04-15          86           32      -      -           -
 33 2020-04-16          88           50      -      -           -
 34 2020-04-17          94           53      -      -           -
 35 2020-04-18          95           64      -      -           -
 36 2020-04-19          96           78      -      -           -
 37 2020-04-20          96           60      -      -           -
 38 2020-04-21          96           48      -      -           -
 39 2020-04-22          97           26      -      -           -
 40 2020-04-23          97           41      -      -           -
 41 2020-04-24          97           60      -      -           -
 42 2020-04-25          98           95      -      -           -
 43 2020-04-26          98           30      -      -           -
 44 2020-04-27          98          104      -      -           -
 45 2020-04-28          98           68      -      -           -
 46 2020-04-29          98           54      -      -           -
 47 2020-04-30          98           53      -      -           -
 48 2020-05-01          98          100      -      -           -
 49 2020-05-02          98           47      -      -           -
 50 2020-05-03          98           80      -      -           -
 51 2020-05-04          98           59      -      -           -
 52 2020-05-05          98           65      -      -           -
 53 2020-05-06          98           37      -      -           -
 54 2020-05-07          98           57      -      -           -
 55 2020-05-08          98           49      -      -           -
 56 2020-05-09          98           40      -      -           -
 57 2020-05-10          98          106      -      -           -
 58 2020-05-11          98           62      -      -           -
 59 2020-05-12          98           54      -      -           -
 60 2020-05-13          98           57      -      -           -
 61 2020-05-14          98           79      -      -           -
 62 2020-05-15          98           55      -      -           -
 63 2020-05-16          99           93      -      -           -
 64 2020-05-17          99          126      -      -           -
 65 2020-05-18         103           72      -      -           -
 66 2020-05-19         103           77      -      -           -
 ----------------------------------------------------------------

```

You can find the official reports here: ![Official data COVID-19](/reports)

## Real data interpolation

It is very important to monitor the progress of the disease with confirmed cases to project the curve day by day and observe the behavior of the basic rate of reproduction.

For this, iterations are performed on the model for different values ​​of the Beta parameter. R0_0 is the real Basic Reproduction Rate for the interpolati  on. R0_P is the value of the projected Basic Reproduction Rate for the last known beta.

![SEIR Model COVID-19](/img/seir-interpolation-2020-05-19.png)

## About SEIR model for COVID 19

SEIR is a deterministic mathematical model for epidemics. It is currently used to analyze the behavior of the COVID-19 pandemic.

Four types of population stages are modeled: Those that are susceptible to contracting the disease S(t), those that acquired it and are in an asymptomatic incubation period E(t), the confirmed infected I(t), and the recovered or dead population R(t).

![SEIR Model COVID-19](/img/seir-blocks.png)

The following differential equations model the behavior of the disease over time.

![SEIR Model COVID-19](/img/seir-diffeq.png)

There are three important parameters of the model:

**Beta:**  Transmission rate.

**Gamma:** Recovery rate.

**Sigma:** The rate at which an exposed person becomes infective.  

The most important indicator is the Basic Reproduction Rate (R0), which represents the number of new infected produced by a single infected if the entire population is susceptible.

The initial conditions for the model to the model of the city of Rosario are:

According to the yearbook of population and vital statistics, the projected population for 2020 of the city of Rosario is 999,323 inhabitants.

```
N        = 992323
E(0)     = 0
I(0)     = 1
R(0)     = 0
S(0)     = N - I0 - R0 - E0
Beta     = 1.30
Gamma    = 1./5
Sigma    = 1./7
R0       = Beta / Gamma = 6.50
```
