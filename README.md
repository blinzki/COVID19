# COVID19

Evolution of COVID 19 - Official reports
Rosario, Santa Fe, Argentina

![SEIR Model COVID-19](/img/seir-covid19.png)

```
COVID 19
Rosario, Argentina
Country Code:AR
City Code   :2000

day Date        Confirmed     Suspected
 01 2020-03-14           1            0       
 02 2020-03-15           1            0
 03 2020-03-16           1            0
 04 2020-03-17           1           12
 05 2020-03-18           1           22
 06 2020-03-19           2           15
 07 2020-03-20           2           14
 08 2020-03-21           2           25
 09 2020-03-22           2           23
 10 2020-03-23           8           19
 11 2020-03-24           8           26
 12 2020-03-25          11           24
 13 2020-03-26          13           24
 14 2020-03-27          21           23
 15 2020-03-28          24           24
 16 2020-03-29          33           28
 17 2020-03-30          48           29
 18 2020-03-31          55           35
 19 2020-04-01          62           61
 20 2020-04-01          65           70
```
## About SEIR Model for COVID 19
SEIR is a deterministic mathematical model for epidemics. It is currently used to analyze the behavior of the COVID-19 pandemic.

Four types of population stages are modeled: Those that are susceptible to contracting the disease (S), those that acquired it and are in an asymptomatic incubation period (E), the confirmed infected (I), and the recovered or dead population.

![SEIR Model COVID-19](/img/seir-blocks.png)

The following differential equations model the behavior of the disease over time.

![SEIR Model COVID-19](/img/seir-diffeq.png)

