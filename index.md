UNDER CONSTRUCTION
-------------------------------------------------------------------------------

docopt
===============================================================================

Command-line interface description language
-------------------------------------------------------------------------------

`docopt` helps you:

 - define interface for your command-line app, and
 - automatically generate parser for it.

`docopt` is based on conventions that are used for decades in help-messages and
man-pages for program interface description.  Interface description
in `docopt` *is* such a help-message, but formalized.  Here is an example:

    Naval Fate.

    Usage:
      naval_fate ship new <name>...
      naval_fate ship [<name>] move <x> <y> [--speed=<kn>]
      naval_fate ship shoot <x> <y>
      naval_fate mine (set|remove) <x> <y> [--moored|--drifting]
      naval_fate -h | --help
      naval_fate --version

    Options:
      -h --help     Show this screen.
      --version     Show version.
      --speed=<kn>  Speed in knots [default: 10].
      --moored      Moored (anchored) mine.
      --drifting    Drifting mine.

The example describes interface of executable `naval_fate`, which can be
invoked with different combinations of *commands* (`ship`, `new`, `move`,
etc.), *options* (`-h`, `--help`, `--speed=<kn>`, etc.)  and positional
arguments (`<name>`, `<x>`, `<y>`).

Example uses brackets `[ ]`, parens `( )`, pipes `|` and ellipsis `...` to
describe *optional*, *required*, *mutually exclusive*, and *repeating*
elements.  Together, these elements form valid *usage patterns*, each starting
with program's name `naval_fate`.

Below the usage patterns, there is a list with option descriptions.
It describes whether an option has short/long forms (`-h`, `--help`), whether
an option has an argument (`--speed=<kn>`), and whether that argument has a
default value (`[default: 10]`).

`docopt` implementation will extract all that information and generate a
command-line arguments parser, with text of the example above being the
help-message, which is shown to a user when the program is invoked with
`-h` or `--help` options.

Usage patterns
-------------------------------------------------------------------------------

### -o --option
### <argument> ARGUMENT
### command

### [optional elements]
### (required elements)
### element|another
### element...
### [options]
### [--]

Option descriptions
-------------------------------------------------------------------------------

Implementations
-------------------------------------------------------------------------------
