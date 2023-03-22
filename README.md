# AKC Dog Breeds Dashboard

> Author: Elena Ganacheva
>
> Project completed in accordance with DSCI 532 for the UBC MDS Program 2022-23

## About

For information on the intention, research questions, as well as a more detailed description of the data, please read the [proposal](docs/proposal.md) instead.

The objective of this dashboard is to enable users to compare different dog breeds described by the [American Kennel Club (AKC)](https://www.akc.org/) to make informed decisions about which dog breed is right for their family.

The landing page presents the user with options on the left side to select their top three priorities in a new dog using dropdowns. They can also click on radio buttons underneath each drop down to indicate whether they want low or high expression of the trait. By default, no traits are selected for the user.

These selected options dynamically update the table on the right with the top 10 dog breeds that meet their priorities with the three traits and the level of the traits from 1 to 5. The sorting priority is based on the order of the selection provided by the user

The dashboard also includes a second page where users can learn more about all the breeds in the AKC dataset with a bar chart of all the traits ordered from highest expression to lowest expression, an image of the dog breed, and a link to more information about the breed on the AKC website. 

A final tab provides information about the 16 traits included in the dataset to help users better understand what the traits mean.

## Usage

The latest version of the dashboard is [deployed on `Render`](https://dash-hound.onrender.com/).

On it, you can explore the [Tidy Tuesday Dog Breeds Dataset](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-02-01) to find the right dog for you.

## Running Locally

The project is implemented in Python using [Dash](https://pypi.org/project/dash/).

The application can be started by:

```bash
python src/app.py
```

You can then access the application at the displayed URL.

Interesting in helping out? Read the [`CONTRIBUTING.md`](CONTRIBUTING.md) for more information!

## License

`dash-hound` was created by Elena Ganacheva

The [Tidy Tuesday Dog Breeds Dataset](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-02-01) which comes from the [American Kennel Club (AKC)](https://www.akc.org/) is licensed under the [Creative Commons Zero v1.0 Universal License](https://github.com/rfordatascience/tidytuesday/blob/master/LICENSE).

Unless otherwise specified, the materials in this repository are covered under this copyright statement:

Copyright (c) 2023 Elena Ganacheva

The software and associated documentation files are licensed under the MIT License. You may find a copy of the license at [`LICENSE`](LICENSE).
