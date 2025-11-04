# linux-open-flag-decoder
Small script to decode which flags have been set in the _flags_ argument to a glibc open() call on Linux.

Use python integer prefixes to indicate what base the integer is, e.g. 0o1234 for an octal number, 0x12ab for a hexademical integer.
