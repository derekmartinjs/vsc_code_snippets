tag: user.code_generic
-

# variable data types
# constant variable
# boolean values
state true: user.code_type_true()
state false: user.code_type_false()
state (float | decimal): user.code_type_fault()
state (int | integer | whole number): user.code_type_integer()
state (undefined | undef): user.code_type_undefined()
state (null | none | nothing): user.code_type_null()

# Variable Declarations, aliasing, and labels
state (string | text | text val): user.code_type_string()
state (const | constant | fixed): user.code_type_variable_constant() 
state (class | object): user.code_type_class()
state (list | array | bag ): user.code_type_bag()
state (set | math set): user.code_type_set()
state (map | object | hash | dictionary | dict | kay vee): user.code_type_bag()
state (enum | enumeration | fixed items): user.code_type_enums()
state (error | err | exception): user.code_type_error()

ncGeneratorFunction
Generator
AsyncGenerator
AsyncFunction
Promise
function
function*
async function

# Objects / dictionary / key value / Hashes
# Promises and async conttructs
# List and arrays
# self, super, new,  this

# control flow statements
# Conditional
# Blocks
block: user.code_block()
break
continue
Empty
if...else
switch
break
continue
Empty
throw
try...catch

# Comments and docstrings
# Exception/Error Handling
# Loops
do...while
for
for each...in
for...in
for...of
for await...of
while

# Control statements
# Functions and Returns
# Enumerations 
# assertion handling statements
try catch 
try catch finally 
throw 
single line if 
if else 
if else if else 

console 
class method 
# Dates and time constructs
RegExpp10all

# convert operations / type casting 
parseFloat 
# import and export constructs
import defaultExport from "module-name";
import * as name from "module-name";
import { export1 } from "module-name";
import { export1 as alias1 } from "module-name";
import { export1 , export2 } from "module-name";

grouping ()
(a) => {
  return a + 100;
}
# Classes and Inheritance constructs
extends 
implements 
inherits 
constructor 
static 

# Directives and other constructs

#Statement Type	Keyword
#looping	while, do-while, for
#decision making	if-else, switch-case
#exception handling	try-catch-finally, throw
#branching	break, continue, label:, retur