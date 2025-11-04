# Utility to decode the flags argument given to open() using glibc on Linux.
# For more information on what these flags do, see:
    # https://man7.org/linux/man-pages/man2/open.2.html
# The values in this script are taken from glibc version 2.40. Mirror:
    # https://github.com/bminor/glibc/blob/release/2.40/master/sysdeps/unix/sysv/linux/bits/fcntl-linux.h
# Oscar T 2025

FLAG_VALUES = {
    "O_RDONLY": 0o0,
    "O_WRONLY": 0o1,
    "O_RDWR": 0o2,
    "O_CREAT": 0o100,
    "O_EXCL": 0o200,
    "O_NOCTTY": 0o400,
    "O_TRUNC": 0o1000,
    "O_APPEND": 0o2000,
    "(O_NONBLOCK/O_NDELAY)": 0o4000,
    "(O_SYNC/O_FSYNC)": 0o4010000,
    "O_ASYNC": 0o20000,
    "__O_LARGEFILE": 0o100000,
    "__O_DIRECTORY": 0o200000,
    "__O_NOFOLLOW": 0o400000,
    "__O_CLOEXEC": 0o2000000,
    "__O_DIRECT": 0o040000,
    "__O_NOATIME": 0o01000000,
    "__O_PATH": 0o010000000,
    "__O_DSYNC": 0o010000,
    "(__O_TMPFILE)": 0o20000000 | 0o200000
    # O_TMPFILE won't work if the file is not a directory, so O_TMPFILE sets 
    # O_DIRECTORY.
}

if __name__ == "__main__":
    flags_string = input("Please enter the flags argument:\n> ")

    if flags_string.startswith("0o"):
        flags = int(flags_string, 8)
    elif flags_string.startswith("0x"):
        flags = int(flags_string, 16)
    else:
        flags = int(flags_string, 10)

    set_options = []

    for flag in FLAG_VALUES.keys():
        if flags & FLAG_VALUES[flag] != 0:
            set_options.append(flag)

    print("The following flags are set:")
    for flag in set_options:
        print(f"\t{flag}")

    # Checking if all the flags ORed together equal the set value. If not, the
    # flags argument is not valid.

    control_value = 0
    for flag in set_options:
        control_value = control_value | FLAG_VALUES[flag]

    if control_value != flags:
        print("The given flags argument is not valid.")
        print("It contains values other than the defined Linux open() flags.")
        print(f"your flags ^ known flags: {oct(control_value ^ flags)}")
