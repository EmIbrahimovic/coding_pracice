# Probelm

Make a cpp file, 

* have extensions installed in VSCode, 
* have gdb, gcc, g++ in `C:\msys64\ucrt64\bin\`

the run button does not show up

click on run and debug tab
> dialog shows up
> first step select GDB LLDB
> second step select g++

errors show up where there shouldn tbe

after setting up tasks, cpp c properties, launch i was getting this debug console
> ERROR: Unable to start debugging. Unexpected GDB output from command "-exec-run". During startup program exited with code 0xc0000139.
> The program 'C:\Users\emira\Documents\projects\coding_pracice\lc0001_two_sum\main.exe' has exited with code 0 (0x00000000)


# Solution

> unistalled Platform IO (needed for 6.1903)

* Went to my active file, called `Ctrl+Shift+P → "Debug: Add Configuration" → "C++ (GDB/LLDB)"`
    * This set up my launch.json - for setting up my debugger i think.
    * this made it so that there wasn't really an error when i click on run

eventually after getting the 000000139 msg
> Ah! 0xc0000139 is a very specific Windows error code: "Entry Point Not Found" or "DLL Not Found".
> This means your program is trying to run but can't find a required DLL (dynamic library).
> Your .exe was compiled with MinGW/MSYS2, and it needs certain DLLs to run, but Windows can't find them.

* the suggested fix was adding minGW to path, but it's already there
* the other suggested fix was add the `-static` flag to my task file and this actually did the trick

# Working with multiple files

1. To specify function definitions, create a `utils.h` file
    * Do ifndef and define and endif to prevent the file from being compiled multiple times or smthn
2. To specify the implementations, creata `utils.cpp` file, include the h file and implement the funcitons
3. In the file where you wanna use them, include `utils.h` and not cpp
4. To compile, if they're in different folders, go to `tasks.json` and add compiler flag `-I.` which will tell it to look for header files in the current directory (the one that vscode has opened rn) or `-I..` to tell it to look in the parent directory
    * NOTE: `-I.` doesn't work, use `-I..`


