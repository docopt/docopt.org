SITE UNDER CONSTRUCTION
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

Text occuring between keyword `usage:` (case-*in*sensitive) and a *visibly*
empty line is interpreted as list of usage patterns.  First word after
`usage:` is interpreted as program's name.  Here is a minimum example for
program that takes no command-line arguments:

    Usage: the_program

### -o --option

Words starting with one or two underscores (`-`, `--`) are interpreted as
short (one-letter) or long options, respectively.

- Short options can be "stacked" meaning that `-abc` is equivalent to
  `-a -b -c`.
- Long options can have arguments specified after space or equal `=` sign:<br>
  `--input=ARG` is equivalent to `--input ARG`.
- Short options can have arguments specified after *optional* space:<br>
  `-f FILE` is equivalent to `-fFILE`.


### &lt;argument> ARGUMENT

Words starting with "`<`", ending with "`>`" or upper-case words are
interpreted as positional arguments.

### command

All other words (that do *not* follow the above conventions of `--options` or
`<arguments>`) are interpreted as (sub)commands.

### [optional elements]

Elements (options, arguments, commands)

### (required elements)
### element|another
### element...
### [options]
### [--]

Option descriptions
-------------------------------------------------------------------------------

Implementations
-------------------------------------------------------------------------------
