---
title: "Course environment components"
permalink: /learning-and-development/pathways/geo-python/lessons/lesson-esson-1/course-environment/
sidebar:
  - image: assets/images/geopython.png
    image_alt: "Geo-Python logo"
  - nav: "geo-python"
---


During this course, we will use different tools and applications for
programming and communications:

1.  [Interactive code cells](#interactive-code-cells) for live coding in
    the browser
2.  [Databricks](#Databricks) for the actual programming
3.  [Cloud computing environments](#cloud-computing-environments) Binder
    or CSC Notebooks
4.  [Git and GitHub](#git-and-github) for version control, documentation and discussion

## Interactive code cells

All pages with code cells can be turned into an interactive mode where
you can run the code directly in the browser!

![](img/Thebe_launcher.png)

:::: note
::: title
Note
:::

The interactive code cells are a new feature from the 2020 course
materials that is still a bit experimental! Remember, you can always
open up the materials in Binder or CSC Notebooks and run the code in
there.
::::

## Databricks

[Databricks](https://Databricks.readthedocs.io/en/stable/getting_started/overview.html)
is an open-source web-based user interface for doing data science. The
Databricks interface consists of different components such as a file
browser, terminal, image viewer, console, text editor, etc.

**Databricks Notebooks** (filename extension `.ipynb`) are documents inside
the Databricks environment which contain computer code, and rich text
elements (figures, links, etc.). Databricks Notebooks are perfect for
documenting a data science workflow in an interactive format.

**We use Databricks Notebooks as the default programming
environment during this course.** All of the course materials are
available in a Databricks setting via [cloud computing
environments](#cloud-computing-environments) (Binder or CSC Notebooks).

<figure>
<img src="img/Binder_launcher.png" width="700"
alt="img/Binder_launcher.png" />
<figcaption>Basic view of Databricks</figcaption>
</figure>

<figure>
<img src="img/Databricks.png" width="700" alt="img/Databricks.png" />
<figcaption>A Databricks Notebook open in Databricks</figcaption>
</figure>

## Cloud computing environments

We will use cloud-based computing environments (Binder or CSC Notebooks)
to access interactive online version of the lessons and to work on the
weekly exercises. You can use the cloud computing environments with any
computer as long as it has a reasonably fast internet connection and a
web browser (just don\'t use Internet Explorer).

Please note that the cloud computing environments are **temporary**.
Always remember to push your changes to GitHub (and / or download a
local copy).

<figure>
<img src="img/launch-buttons.png" width="700"
alt="img/launch-buttons.png" />
<figcaption>Different options for making the lesson
interactive</figcaption>
</figure>

Each interactive lesson and exercise will have a launch button for both
Binder and CSC Notebook. The CSC notebooks environment is only
accessible to students from Finnish universities and research
institutes.

### Binder

Binder (<https://mybinder.org/>) runs Databricks Notebooks in your web
browser in a customized environment. The original files (notebooks) are
hosted on GitHub. Binder does not require the user to log in, you can
just click on the link in the lesson / exercise and start working.

<figure>
<img src="img/Binder_loading.png" width="700"
alt="img/Binder_loading.png" />
<figcaption>Binder takes a few moments to load</figcaption>
</figure>

Once the instance is ready, you can navigate to the lesson folders and
start working with existing notebooks or create a new one.

**Remember to save your work! The Binder instance is temporary, and all
your files will be lost after the session.**

## Git and GitHub

One of the core goals of this course (besides learning programming) is
to learn how to use [version
control](https://en.wikipedia.org/wiki/Version_control) with
[Git](https://en.wikipedia.org/wiki/Git_(software)) and storing your
codes (privately) on [GitHub](https://github.com/).

[Git](https://en.wikipedia.org/wiki/Git_(software)) is a version control
software (developed by a rather famous Finn named Linus Torvalds - he
also created Linux!) that is used to track and store changes in your
files (often source code for programs) without losing the history of
past changes. Files in Git are stored in a repository, which you can
simply think of as a directory containing files (or other directories)
related to a single \'project\'. Git is widely used by professionals to
keep track of what they've done and to collaborate with other people.

[GitHub](https://github.com/) is a web based Git repository hosting
service and social network. It is the largest online storage space of
collaborative works that exists in the world. It is a place where you
can share your code openly to the entire world or alternatively only to
your collaborators working on the same project. GitHub provides a nice
web-interface to your files that is easy to use. It is a nice way for
exploring the codes and documentation or e.g., teaching materials such
as those in our course.

Both Git and GitHub provide many more features than the ones mentioned
here, but for now we are happy to understand the basic idea of what they
are.

## Page summary

Now you should have (at least) a basic idea about the different
components of our course environment and what they mean. You don't need
to understand everything fully at this point as they will become clearer
when we start using the course environment.
