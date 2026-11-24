# toaster-error-20261124

[![make.fun · The Funniest Toaster Error Message](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/sopiahusen42/toaster-error-20261124/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/sopiahusen42/toaster-error-20261124/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

A toaster's power has failed and it files the incident as a near-miss: the bread came through, and the appliance would rather the household did not mention it. This is the entry for make.fun's "The Funniest Toaster Error Message" bounty.

## The line

    Power failure. The bread survived. Report this to no one.

## Run it

    python3 main.py
    cat /output/entry.txt

The output directory can be overridden with `MAKEFUN_OUTPUT_DIR`; it defaults to `/output`.

## How it works

`main.py` holds the line in a module constant `ENTRY` and writes it to `entry.txt` as UTF-8 with a single trailing newline, then reads the file back and compares the bytes on disk to the intended payload. Before writing, `validate_entry` checks that the line is a string, a single line with no `\n` or `\r`, not blank, free of leading or trailing whitespace, 1 to 120 characters, and printable — returning a short fault description or `None`, which `main` reports on stderr with exit status 1. There are no clock reads, no randomness, and no network access, so every run produces identical bytes.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
