
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

Example uses brackets "`[ ]`", parens "`( )`", pipes "`|`" and ellipsis
"`...`" to
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

Program can have several patterns listed with various elements used to
describe the pattern:

    Usage:
      the_program command --option <argument>
      the_program [<optional-argument>]
      the_program --another-option=<with-argument>
      the_program (--either-that-option | <or-this-argument>)
      the_program <repeating-argument> <repeating-argument>...

Each of the elements and syntactic constructs is described below.

### -o --option

Words starting with one or two dashes ("`-`", "`--`") are interpreted as
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

Elements (options, arguments, commands) enclosed with square brackets "`[ ]`"
are marked to be *optional*.  It does not matter if elements are enclosed
in same or different brackets, for example:

    Usage: the_program [command --option <argument>]

is equivalent to:

    Usage: the_program [command] [--option] [<argument>]

### (required elements)

*All elements are required by default*, if not included in brackets "`[ ]`".
However, sometimes it is necessary to mark elements as required explicitly
with parens "`( )`".
For example, when you need to group mutually-exclussive elements (see next
section for details on them):

    Usage: the_program (--either-this <and-that> | <or-this>)

Another use-case, is when you need to specify that *if one element is present,
then another one is required*, which you can achieve as:

    Usage: the_program [(<one-argument> <another-argument>)]

In this case, a valid program invocation could be with either no arguments,
or with 2 arguments.

### element|another

Mutually exclusive elements can be separated with pipe "`|`" as follows:

    Usage: the_program go (--up | --down | --left | --right)

Use parens "`( )`" to group elements when *one* of the mutually exclussive
cases is required.  Use brackets "`[ ]`" to group elements when *none* of the
mutually exclussive cases is required:

    Usage: the_program go [--up | --down | --left | --right]

Note, that specifying several patterns works exactly like pipe "`|`", that is:

    Usage: the_program run [--fast]
           the_program jump [--high]

is equivalent to:

    Usage: the_program (run [--fast] | jump [--high])

### element...

Use ellipsis "`...`" to specify that argument (or group of arguments)
to the left could be repeated 1 or more times:

    Usage: the_program open <file>...
           the_program move (<from> <to>)...

You can flexibly specify number of arguments that are required.
Here are 3 (redundant) ways of requiring zero or more arguments:

    Usage: the_program [<file>...]
           the_program [<file>]...
           the_program [<file> [<file> ...]]

One or more arguments:

    Usage: the_program <file>...

Two or more arguments (and so on):

    Usage: the_program <file> <file>...

### [options]

"`[options]`" is a shortcut that allows to avoid listing all options
in a pattern.  For example:

    Usage: the_program [options] <path>

    --all             List everything.
    --long            Long output.
    --human-readable  Display in human-readable format.

is equivalent to:

    Usage: the_program [--all --long --human-readable] <path>

    --all             List everything.
    --long            Long output.
    --human-readable  Display in human-readable format.

This can be usefull, if you have many options, and all of them are applicable
to one of patterns. Alternatively, if you have both short and long
versions of options (specified in option description part),
you can list either of them in a pattern:

    Usage: the_program [-alh] <path>

    -a, --all             List everything.
    -l, --long            Long output.
    -h, --human-readable  Display in human-readable format.

### [--]

Double dash "`--`", when not part of an option, is used (by convention)
to separate options and positional arguments, to handle cases when
e.g. file names could be mistaken for options.  `docopt`-based command-line
arguments parsers support this convention.  Thus you are recommended
to include "`[--]`" into your patterns before positional arguments in order
to inform your users that it is supported.  For example:

    Usage: the_program [options] [--] <file>...

Option descriptions
-------------------------------------------------------------------------------

Implementations
-------------------------------------------------------------------------------

`docopt`-based command-line arguments parsers are developed on
[github](https://github.com/docopt):

- Python (reference) implementation.
- Ruby implementation.
- CoffeeScript/JavaScript implementation.
- Lua implementation.

<br>
