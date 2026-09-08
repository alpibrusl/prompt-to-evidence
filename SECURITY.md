# Security policy

This repository is a manuscript and its build configuration. It ships no
service, runs no server, and processes no user data.

## Reporting

Anything security-relevant in the build tooling belongs against
[content-kit](https://github.com/alpibrusl/content-kit/security), which is
where that code lives, or against
[cohort-kit](https://github.com/alpibrusl/cohort-kit/security) for the cohort
renderer. For anything in this repository, email **alfonso@alpibru.com** or open an
issue.

## The fixture generates data, it does not ship it

`cohort/fixture/` holds a generator, not a dataset. Every figure the bootcamp
and the book's appendices use is produced by running it, and its output is
gitignored. Nothing in it is real: the company, its customers and its numbers
are invented, and the seed is fixed so the same invented numbers come back
every time.
