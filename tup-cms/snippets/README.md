# TACC CMS Per-Site Resources - Example - Snippets

All snippet code specific to this project __must__ be placed in this directory. This allows us to version and source control snippet code. Failure to do so will result in snippet code loss upon data loss from database.

_This directory can alleviate danger #1 of [Why a Snippet Is Dangerous](#why-a-snippet-is-dangerous)._

## Important

1. The Core CMS __must not__ use any snippets. _They would be inaccessible to projects._
2. A CMS project __should not__ use any snippets. _They __may only__ be temporarily._

## Usage

In a CMS project:

1. Any snippet __must__ also be saved into this directory in its own file.
2. Any snippet file __must__ be kept up to date.[^1]

[^1]: For now, maintain snippet source code via internal team process.

## What a Snippet Is

A snippet is a __dangerous__ feature from the plugin [`djangocms-snippet`](https://github.com/divio/djangocms-snippet) which is installed in the CMS.

It allows an authorized CMS user to create a snippet of front-end web code (e.g. CSS, HTML, JS) in the database for use anywhere on the website.

## Why a Snippet Is Dangerous

1. The code is dependent on the (unsynced) database, because it is not under:
    - source/version control
2. The code is independent of any other code control:
    - security
    - dependency management
    - style guide
    - organization
    - linting

## Why a Snippet Is Allowed

1. Support time-sensitive changes to the CMS.[^2]
2. Support ad-hoc changes by designer who codes.[^2]

[^2] This is permitted with the expectation that the snippet code is soon appropriately integrated into the repository.
