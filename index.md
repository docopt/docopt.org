
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

Below the usage patterns, there is a list of options with descriptions.
They describe whether an option has short/long forms (`-h`, `--help`), whether
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
There, the word "*word*" describes a sequence of characters delimited
by either whitespace, one of "`[]()|`" characters, or "`...`".

### &lt;argument> ARGUMENT

Words starting with "`<`", ending with "`>`" or upper-case words are
interpreted as positional arguments.

    Usage: the_program <host> <port>

### -o --option

Words starting with one or two dashes (with exception of "`-`", "`--`"
by themselves) are interpreted as short (one-letter) or long options,
respectively.

- Short options can be "stacked" meaning that `-abc` is equivalent to
  `-a -b -c`.
- Long options can have arguments specified after space or equal "`=`" sign:<br>
  `--input=ARG` is equivalent to `--input ARG`.
- Short options can have arguments specified after *optional* space:<br>
  `-f FILE` is equivalent to `-fFILE`.

Note, writing `--input ARG` (opposed to `--input=ARG`) is ambiguous, meaning
it is not possibe to tell whether `ARG` is option's argument or positional
argument.  In usage patterns this will be interpreted as option with argument
*only* if [option's description](#) for that option is provided.  Otherwise
it will be interpreted as separate option and positional argument.

Same ambiguity is with `-f FILE` and `-fFILE` notation. Although in the latter
case it is not possible to tell whether it is a number of stacked short
options, or an option with argument.  These notations will be interpreted as
option with argument *only* if option's description is provided.


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
(from list of options with descriptions) in a pattern.  For example:

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

More details on how to write options' descriptions will follow below.

### [--]

Double dash "`--`", when not part of an option, is often used by convention
to separate options and positional arguments, in order to handle cases when
e.g. file names could be mistaken for options.  In order to support this
convention, add "`[--]`" into your patterns before positional arguments.

    Usage: the_program [options] [--] <file>...

Apart from this special meaning, "`--`" is just a normal command, so you can
apply any previously-described operations, for example make it required
(by dropping brackets "`[ ]`")

### [-]

Single dash "`-`", when not part of an option, is often used by convention
to signify that a program should process `stdin`, as opposed to a file.
If you want to follow this convention add "`[-]`" to your pattern.
"`-`" by itself is just a normal command, which you can use with any meaning.

Option descriptions
-------------------------------------------------------------------------------

Option descriptions consist of a list of options that you put below your
ussage-patterns.  It is optional to specify them if there is no ambiguity
in usage-patterns (described in [`--option` section](#)).

Option's description allows to specify:

- that a short and a long options are synonymous,
- that an option has an argument,
- default value for option's argument.

The rules are as follows:

Every line that starts with "`-`" or "`--`" (not counting spaces)
is treated as an option description, e.g.:

    Options:
      --verbose   # GOOD
      -o FILE     # GOOD
    Other: --bad  # BAD, line does not start with dash "-"

To specify that option has an argument, put a word describing that
argument after space (or equals "`=`" sign) as shown below. Follow
either `<angular-brackets>` or `UPPER-CASE` convention for options' arguments.
You can use comma if you want to separate options. In the example below, both
lines are valid, however you are recommended to stick to a single style.

    -o FILE --output=FILE       # without comma, with "=" sign
    -i <file>, --input <file>   # with comma, wihtout "=" sing

Use two spaces to separate options with their informal description.

    --verbose MORE text.    # BAD, will be treated as if verbose
                            # option had an argument MORE, so use
                            # 2 spaces instead
    -q        Quit.         # GOOD
    -o FILE   Output file.  # GOOD
    --stdout  Use stdout.   # GOOD, 2 spaces

If you want to set a default value for an option with an argument, put it
into the option-description, in form `[default: <the-default-value>]`.

    --coefficient=K  The K coefficient [default: 2.95]
    --output=FILE    Output file [default: test.txt]
    --directory=DIR  Some directory [default: ./]


Implementations
-------------------------------------------------------------------------------

`docopt`-based command-line arguments parsers are developed on
[github](https://github.com/docopt):

- Python (reference) implementation.
- Ruby implementation.
- CoffeeScript/JavaScript implementation.
- Lua implementation.

<br>
