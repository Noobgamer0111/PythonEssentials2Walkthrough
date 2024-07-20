# File naming schemes:

# Windows: A typical path to a Windows file is of X:\directory\filename.ext
# Linux: A typical path to a Linux file is of /directory/filename.ext

# However, your Python script must be written to be compensate for the differences in file naming schemes.
# --------------------------
# Python can compensate for the differences in file naming schemes by converting the 
# the slashes to backslashes or vice versa. E.g:

name ="dir/file.ext"
# is the same as
name = "C:/dir/file.ext"

# Why? Because Python does not actually interact the file, but utilises handles and streams to 
# access the file. The file is accessed as a stream of data, and the file is read or written to.