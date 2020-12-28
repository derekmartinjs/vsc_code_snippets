tag: user.code_operators
-
# pointer operators 
op dereference: user.code_operator_indirection()
op address of: user.code_operator_address_of()
op arrow: user.code_operator_structure_dereference()

# lamdba
op lamda: user.code_operator_lamda()

# subscript
op subscript: user.code_operator_subscript()

# increment/decrement operators
op (increment | plus plus): user.code_operator_increment_postfix()

op (plus plus | increment): user.code_operator_increment__prefix()
op (plus plus | increment) equals: user.code_operator_increment_assignment_prefix()

op (decrement | minus minus): user.code_operator_decrement_postfixx()
op (minus minus | decrement): user.code_operator_incrementr_prefix()
op (minus minus | decrement) equals: user.code_operator_increment_assignment_prefix()

# assignment 
op (minus | subtract): user.code_operator_subtraction()
op (minus | subtract) equals: user.code_operator_subtraction_assignment()
op (add | plus): user.code_operator_addition()
op (add | plus) equals: user.code_operator_addition_assignment()
op (times | multiply): user.code_operator_multiply()
op (times | multiply) equals: user.code_operator_multiplication_assignment()
op divide: user.code_operator_divide()
op divide equals: user.code_operator_divide_assignment()
op mod: user.code_operator_modulo()
op mod equals: user.code_operator_modulo_assignment()
(op (power | exponent) to the power of [of]): user.code_operator_exponent()
(op (power | exponent) to the power of [of]) equals: user.code_operator_exponent_assignment()

# logical NULLish
[op] bitwise and: user.code_operator_bitwise_and()
[op] bitwise nob: user.code_operator_bitwise_not()

(op | logical | bitwise) and equals: user.code_operator_bitwise_and_equals()
(op | logical | bitwise) or equals: user.code_operator_bitwise_or_equals()
[op] bitwise or: user.code_operator_bitwise_or()
(op | logical | bitwise) or equals: user.code_operator_bitwise_or_equals()
(op | logical | bitwise) (ex | exclusive) or: user.code_operator_bitwise_exclusive_or()
(op | logical | bitwise) (left shift | shift left): user.code_operator_bitwise_left_shift()
(op | logical | bitwise) (right shift | right left): user.code_operator_bitwise_right_shift()
(op | logical | bitwise) (ex | exclusive) or equals: user.code_operator_bitwise_exclusive_or_equals()
[(op | logical | bitwise)] (left shift | shift left) equals: user.code_operator_bitwise_left_shift_equals()
[(op | logical | bitwise)] (right shift | shift right) equals: user.code_operator_bitwise_right_shift_equals()x

# comparison operators 
(op | is) equal: user.code_operator_equal()
(op | is) strict equal: user.code_operator_equal_strict()
(op | is) not equal: user.code_operator_not_equal()
(op | is) not equal strict: user.code_operator_not_equal_strict()
(op | is) (greater | more): user.code_operator_greater_than()
(op | is) (less | below): user.code_operator_less_than()
(op | is) greater [than] or equal: user.code_operator_greater_than_or_equal_to()
(op | is) less [than] or equal: user.code_operator_less_than_or_equal_to()
(op | is) in: user.code_operator_in()
(op | is) in stance of: user.code_operator_instance_of()

# unary operator%

op typeof <user.text>: user.typeof_operator()
op varname <user.text>: user.variable_type_operator()
op void <user.text>: user.void_operator()
op delete: <user.text>: user.delete_type_operator()
(destructure | desctruct) (array | list): user.code_operator_destructure_list()
(destructure | desctruct) (ob | dict | object | kv): user.code_operator_destructure_object()

# Conditional (ternary) operator

# relational operators
# tbd
^op spread (postfix | post)$: "..."
^spread op (prefix | pre)$: "..."

(op | pad) colon: " : "
