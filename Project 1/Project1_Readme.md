# Project 1: A study of the effects of Median Household income on ACT/SAT results in US States.

### Problem Statement
It is often said that wealth inequality is a barrier to education and social mobility. As a data scientist, I am keen to find out if that is true. To approach this, I will study if there is a correlation between the Median Houshold Income of each state with their average SAT/ACT scores.

And if there is a correlation found between wealth and educational attainment, we will discuss what can be done to bridge that gap, possibly in the form of monetary grants or tuition help.

Inspiration: https://www.urban.org/sites/default/files/publication/89976/wealth_and_education_4.pdf 
---
### Datasets
#### Provided Data
ACT Scores
* [`act_2017.csv`](./data/act_2017.csv): 2017 ACT Scores by State
* [`act_2018.csv`](./data/act_2018.csv): 2018 ACT Scores by State
* [`act_2019.csv`](./data/act_2019.csv): 2019 ACT Scores by State

SAT Scores
* [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT Scores by State
* [`sat_2018.csv`](./data/sat_2018.csv): 2018 SAT Scores by State
* [`sat_2019.csv`](./data/sat_2019.csv): 2019 SAT Scores by State
#### External Research
Median Personal Income by States [External Source]
* [2017_median_pers_income.csv](./data/2017_median_pers_income.csv): Median Personal Income by States 2017
* [2018_median_pers_income.csv](./data/2018_median_pers_income.csv): Median Personal Income by States 2018
* [2019_median_pers_income.csv](./data/2019_median_pers_income.csv): Median Personal Income by States 2019

Source: https://fred.stlouisfed.org/release/tables?rid=249&eid=259515&od=2019-01-01#

---

### Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---| 
|2017 SAT Total|float|SAT 2017|The average total score by state in the 2017 SAT. Highest possible score is 1600.|
|2018 SAT Total|float|SAT 2018|The average total score by state in the 2018 SAT. Highest possible score is 1600.|
|2019 SAT Total|float|SAT 2019|The average total score by state in the 2019 SAT. Highest possible score is 1600.|
|2017 ACT Composite|float|ACT 2017|The average composite score by state in the 2017 ACT. Highest possible composite score is 36.|
|2018 ACT Composite|float|ACT 2018|The average composite score by state in the 2018 ACT. Highest possible composite score is 36.|
|2019 ACT Composite|float|ACT 2019|The average composite score by state in the 2019 ACT. Highest possible composite score is 36.|
|2017 Median Income|int|2017 Median Income by State|2017 Median Annual Income by State. In USD.|
|2018 Median Income|int|2018 Median Income by State|2018 Median Annual Income by State. In USD.|
|2019 Median Income|int|2019 Median Income by State|2019 Median Annual Income by State. In USD.|

ACT Source: https://www.princetonreview.com/college-advice/good-act-scores#:~:text=The%20ACT%20is%20scored%20on,of%20your%204%20section%20scores.

SAT Source: https://satsuite.collegeboard.org/media/pdf/understanding-sat-scores.pdf 

Median Personal Income By States (https://fred.stlouisfed.org/release/tables?rid=249&eid=259515&od=2017-01-01#)
---

### Observations
**Median Income against ACT Scores**
|Dependent Variable|Independent Variable|Correlation Coefficient|
|---|---|---|
|2017 Median Income|2017 ACT Composite|49.7%|
|2018 Median Income|2018 ACT Composite|55.1%|
|2019 Median Income|2019 ACT Composite|53.0%|

**Median Income against SAT Scores**
|Dependent Variable|Independent Variable|Correlation Coefficient|
|---|---|---|
|2017 Median Income|2017 SAT Total|-16.5%|
|2018 Median Income|2018 SAT Total|-17.2%|
|2019 Median Income|2019 SAT Total|-8.8%|

There appears to be a weak negative correlation (0 to 0.3) between Median Household income and the SAT Total Scores.

There also appears to be a strong positive correlation (0.5 to 1.0) between the median income and the ACT composite scores.

**Correlation between ACT Scores and Household Income**

There appears to be a strong positive correlation (0.5 to 1.0) between the median income and the ACT composite scores.

From the boxplots, we can see that the states with highest ACT composite scores have above average Median Household Incomes, whilst the states with lowest ACT composite scores have below average Median Household Incomes.

This has been studied and I cite a [study by University of Pennsylvania](https://budgetmodel.wharton.upenn.edu/issues/2021/9/28/is-income-implicit-in-measures-of-student-ability#:~:text=The%20ACT%20composite%20score%20has,school%20GPA%20or%20class%20rank.) titled "Is Income Implicit in Measures of Student Ability?"

We can conclude that there is an effect with regards to ACT scores.

---
**Correlation between SAT Scores and Household Income**

There appears to be a (very) weak negative correlation between median income and SAT Total Scores.

Based on the boxplots, there is no observable trend between the highest/lowest scoring states with median household income.

We thus cannot conclude that there is or is not an effect with regards to SAT scores.

---
*What can the college board do about these findings?*

Financial grants can be given to households to help aid students from households with lower income.

---


### Conclusion

The college board can look into providing grants to students from households with average or below average median household income, to help boost the grades of these students sitting for entrance examinations.

---