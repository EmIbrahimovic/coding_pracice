

```powershell
param(
    [string]$Text,              # String
    [int]$Number,               # Integer
    [bool]$Flag,                # Boolean ($true/$false)
    [switch]$Enable,            # Switch (present or not)
    [array]$List,               # Array
    [string[]]$Files,           # Array of strings
    
    [Parameter(Mandatory=$true)]
    [string]$Required,          # Required parameter
    
    [ValidateSet("A", "B", "C")]
    [string]$Choice,            # Only allows specific values
    
    [ValidateRange(1, 100)]
    [int]$Percent,              # Number must be in range
    
    [ValidatePattern("^[A-Z]")] 
    [string]$Code               # Must match regex pattern
)
```