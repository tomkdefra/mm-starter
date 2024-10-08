---
title: "
"
permalink: /learning-and-development/pathways/reproducible-analytical-pipelines/intro-r/
sidebar:
  nav: "reproducible-analytical-pipelines"
---


# Introduction to R

What you'll have learned by the end of the chapter: reading and writing,
exploring (and optionally visualising) data.

## Reading in data with R

Your first job is to actually get the following datasets into an R session.

First install the `{rio}` package (if you don't have it already), then download
the following datasets:

- [mtcars.csv](https://raw.githubusercontent.com/b-rodrigues/modern_R/master/datasets/mtcars.csv)
- [mtcars.dta](https://github.com/b-rodrigues/modern_R/raw/master/datasets/mtcars.dta)
- [mtcars.sas7bdat](https://github.com/b-rodrigues/modern_R/raw/master/datasets/mtcars.sas7bdat)
- [multi.xlsx](https://github.com/b-rodrigues/modern_R/raw/master/datasets/multi.xlsx)

Also download the following 4 `csv` files and put them in a directory called
`unemployment`:

- [unemp_2013.csv](https://raw.githubusercontent.com/b-rodrigues/modern_R/master/datasets/unemployment/unemp_2013.csv)
- [unemp_2014.csv](https://raw.githubusercontent.com/b-rodrigues/modern_R/master/datasets/unemployment/unemp_2014.csv)
- [unemp_2015.csv](https://raw.githubusercontent.com/b-rodrigues/modern_R/master/datasets/unemployment/unemp_2015.csv)
- [unemp_2016.csv](https://raw.githubusercontent.com/b-rodrigues/modern_R/master/datasets/unemployment/unemp_2016.csv)

Finally, download this one as well, but put it in a folder called `problem`:

- [mtcars.csv](https://raw.githubusercontent.com/b-rodrigues/modern_R/master/datasets/problems/mtcars.csv)

and take a look at chapter 3 of my other book, [Modern R with the
{tidyverse}](https://b-rodrigues.github.io/modern_R/reading-and-writing-data.html)
and follow along. This will teach you to import and export data.

`{rio}` is some kind of wrapper around many packages. You can keep using
`{rio}`, but it is also a good idea to know which packages are used under the
hood by `{rio}`. For this, you can take a look at this
[vignette](https://cran.r-project.org/web/packages/rio/vignettes/rio.html).

If you need to import very large datasets (potentially several GBs), you might
want to look at packages like `{vroom}` ([this
benchmark](https://vroom.r-lib.org/articles/benchmarks.html#reading-delimited-files)
shows a 1.5G csv file getting imported in seconds by `{vroom}`. For even larger
files, take a look at `{arrow}` [here](https://arrow.apache.org/docs/r/). This
package is able to efficiently read very large files (`csv`, `json`, `parquet`
and `feather` formats).

## A little aside on pipes

Since R version 4.1, a forward pipe `|>` is included in the standard library of
the language. It allows to do this:

```{webr-r}

4 |>
  sqrt()

```

Before R version 4.1, there was already a forward pipe, introduced with the
`{magrittr}` package (and automatically loaded by many other packages from the
*tidyverse*, like `{dplyr}`):

```{webr-r}
library(dplyr)

4 %>%
  sqrt()

```

Both expressions above are equivalent to `sqrt(4)`. You will see why this is
useful very soon. For now, just know this exists and try to get used to it.

## Exploring and cleaning data with R

Take a look at [chapter
4](https://b-rodrigues.github.io/modern_R/descriptive-statistics-and-data-manipulation.html#a-first-taste-of-data-manipulation-with-dplyr)
of my other book, ideally you should study the entirety of the chapter, but for
our purposes you should really focus on sections 4.3, 4.4, 4.5.3, 4.5.4,
(optionally 4.7) and 4.8.

You should be able to read and understand expressions like the one below after having read the chapters above.

```{webr-r}
starwars %>%
  group_by(sex) %>%
  summarise(mean_height = mean(height, na.rm = TRUE))
```

While optional, the concept of list-columns is quite powerful and I wanted to say a few words about it. Take a look at the types of columns
of the `starwars` dataset:

```{webr-r}
str(head(starwars, 9))
```

Each of the elements of the column `films` is a list. For example:

```{webr-r}
starwars %>% 
  filter(name == "Luke Skywalker") %>%  
  .$films
```

Because lists are very flexible and can contain any data type, it is possible to have a list-column of data frames. 
This is extremely useful to operate on groups without having to use loops:

```{webr-r}
starwars %>% 
  group_nest(sex) 
```

It is now possible to apply any function that takes a data frame as an input to each data frame from the `data` list-column:

```{webr-r}
starwars %>% 
  group_nest(sex) %>%
  mutate(regression = lapply(data, \(x)(lm(height ~ mass, data = x))),
         summary = lapply(regression, summary)) 
```

## Data visualization

We're not going to focus on visualization due to lack of time. If you need to
create graphs, read [chapter
5](https://b-rodrigues.github.io/modern_R/graphs.html).

## Further reading

[R for Data Science](https://r4ds.had.co.nz/)
