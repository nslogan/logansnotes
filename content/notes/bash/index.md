+++
title = "bash"
date = 2021-01-02
# updated = 
+++

- Clearing cache: https://unix.stackexchange.com/questions/5609/how-do-i-clear-bashs-cache-of-paths-to-executables
	+ e.g. "I removed the apt-provided docker-compose and put the new github version in a different location (/usr/bin -> /usr/local/bin)"

## Text Input

`bash` uses the [`readline` library](https://tiswww.case.edu/php/chet/readline/rltop.html) for [line-editing](https://en.wikipedia.org/wiki/Line_editor). `readline` supports both `vi` and `Emacs` mode, I have left mine in `Emacs` mode so far so any content on this page about editing modes will use `Emacs` shortcuts.

Q: Reload `~/.inputrc`
A: `C-x C-r` bound to `re-read-init-file` (default)

```bash
# Making a ~/.inputrc file overrides the /etc/inputrc file which in Ubuntu
# includes settings to use ctrl-arrow. See
# https://stackoverflow.com/questions/5029118/bash-ctrl-to-move-cursor-between-words-strings.

# Include Ubuntu default bindings
$include  /etc/inputrc

# Make GDB ctrl-l behave like bash default
$if Gdb
"\C-l": "shell clear\n"
$endif

"\ep": history-search-backward
"\en": history-search-forward
```
