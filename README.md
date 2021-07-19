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

## Examples

[helloworld.sy](examples/helloworld.sy)

Prints `Hello World!\n`.

```bash
H.e.l..o. # print 'Hello'
A/. # print ' ' (char code 32)
W.o.r.l.d. # print 'World'
B/. # print '!' (char code 33)
9+. # print '\n' (char code 10)
```

[forloop.sy](examples/forloop.sy)

Prints `0123456789`.

```bash
9+ # set first cell to 10
[ # repeat while first cell nonzero
>: # print number in second cell
+ # increment second cell
<- # decrement first cell
] # repeat while first cell nonzero
```

[fizzbuzz.sy](examples/fizzbuzz.sy)

Prints the first 100 [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) numbers.

```bash
->d>>9+>>>>>>>>>>>>>>>+<<<<<<<<<<<<<<<<<[>+>> # set up 15-tape
[<F.i.z..B.u.z..9+.>>>>>>>>>>>>>>>>++[-<+]->>>>-] # n % 15 = 0
>[<<<:>.>+>-] # n % 15 = 1
>[<<<<:>.>>+>-] # n % 15 = 2
>[<<<<F.i.z..9+.>>>+>-] # n % 15 = 3
>[<<<<<<:>.>>>>+>-] # n % 15 = 4
>[<<<<<<B.u.z..9+.>>>>>+>-] # n % 15 = 5
>[<<<<<<<F.i.z..9+.>>>>>>+>-] # n % 15 = 6
>[<<<<<<<<<:>.>>>>>>>+>-] # n % 15 = 7
>[+[-<+]->>:>.>>>>>>>>+>-] # n % 15 = 8
>[<<<<<<<<<<F.i.z..9+.>>>>>>>>>+>-] # n % 15 = 9
>[+[-<+]->>>B.u.z..9+.>>>>>>>>>>+>-] # n % 15 = 10
>[+[-<+]->>:>.>>>>>>>>>>>+>-] # n % 15 = 11
>[+[-<+]->>>F.i.z..9+.>>>>>>>>>>>>+>-] # n % 15 = 12
>[+[-<+]->>:>.>>>>>>>>>>>>>+>-] # n % 15 = 13
>[+[-<+]->>:>.>>>>>>>>>>>>>>+>-] # n % 15 = 14
>[<+>-]+[-<+]->-] # increment 15-tape
```
