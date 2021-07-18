# Symbl

An interpreted symbol-based language inspired by BF.

## Installation

Clone source repository: `git clone https://github.com/csaye/symbl`<br />
Change directory to `symbl/`: `cd symbl/`<br />
Install requirements: `pip install -r requirements.txt`<br />
Give permission to run `run.sh`:`chmod +x run.sh`<br />
Run `run.sh` on your program file: `./run.sh <program>`

## Symbols

`>` increment pointer<br />
`<` decrement pointer<br />
`+` increment byte<br />
`-` decrement byte<br />
`*` lshift byte<br />
`/` rshift byte<br />
`.` output byte<br />
`:` output number<br />
`,` input byte<br />
`;` input number<br />
`[` start loop<br />
`]` end loop<br />
`a-zA-Z` set byte<br />
`0-9` set number<br />
`#` comment
