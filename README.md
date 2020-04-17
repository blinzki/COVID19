![Python application](https://github.com/blinzki/COVID19/workflows/Python%20application/badge.svg)

>Author        : Ing. Pablo Eduardo Romero Oestreicher

>Last Update   : 16/04/20

>Contact       : ing.pabloeromero@gmail.com

# Rosario COVID-19

Evolution of COVID 19 - Official reports

Rosario, Santa Fe, Argentina

![SEIR Model COVID-19](/img/seir-covid19-15-04-20.png)

## Data COVID-19

```

Rosario, Argentina
Country Code:AR
City Code   :2000

day Date         Confirmed    Suspected   R0_R    R_P  Prediction

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
 ----------------------------------------------------------------

```

You can find the official reports here: ![Official data COVID-19](/reports)

## Real data interpolation

It is very important to monitor the progress of the disease with confirmed cases to project the curve day by day and observe the behavior of the basic rate of reproduction.

For this, iterations are performed on the model for different values ​​of the Beta parameter. R0_0 is the real Basic Reproduction Rate for the interpolati  on. R0_P is the value of the projected Basic Reproduction Rate for the last known beta.

![SEIR Model COVID-19](/img/seir-interpolation-15-04-20.png)

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

![SEIR Model COVID-19](/img/seir-r0.png)

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
