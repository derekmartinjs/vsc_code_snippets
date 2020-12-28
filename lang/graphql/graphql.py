"""

\"""
\A simple GraphQL schema which is well described.
\"""

"""
"""
 import { GraphQLSchema } from 'graphql'; // ES6
var { GraphQLSchema } = require('graphql'); // CommonJS
Overview
Schema

class GraphQLSchema
A representation of the capabilities of a GraphQL Server.
Definitions

class GraphQLScalarType
A scalar type within GraphQL.
class GraphQLObjectType
An object type within GraphQL that contains fields.
class GraphQLInterfaceType
An interface type within GraphQL that defines fields implementations will contain.
class GraphQLUnionType
A union type within GraphQL that defines a list of implementations.
class GraphQLEnumType
An enum type within GraphQL that defines a list of valid values.
class GraphQLInputObjectType
An input object type within GraphQL that represents structured inputs.
class GraphQLList
A type wrapper around other types that represents a list of those types.
class GraphQLNonNull
A type wrapper around other types that represents a non-null version of those types.
Predicates

function isInputType
Returns if a type can be used as input types for arguments and directives.
function isOutputType
Returns if a type can be used as output types as the result of fields.
function isLeafType
Returns if a type can be a leaf value in a response.
function isCompositeType
Returns if a type can be the parent context of a selection set.
function isAbstractType
Returns if a type is a combination of object types.
Un-modifiers

function getNullableType
Strips any non-null wrappers from a type.
function getNamedType
Strips any non-null or list wrappers from a type.
Scalars

var GraphQLInt
A scalar type representing integers.
var GraphQLFloat
A scalar type representing floats.
var GraphQLString
A scalar type representing strings.
var GraphQLBoolean
A scalar type representing booleans.
var GraphQLID
A scalar type representing IDs.
Schema
GraphQLSchema
class GraphQLSchema {
  constructor(config: GraphQLSchemaConfig)
}
 
type GraphQLSchemaConfig = {
  query: GraphQLObjectType;
  mutation?: ?GraphQLObjectType;
}
A Schema is created by supplying the root types of each type of operation, query and mutation (optional). A schema definition is then supplied to the validator and executor.

Example
var MyAppSchema = new GraphQLSchema({
  query: MyAppQueryRootType
  mutation: MyAppMutationRootType
});
Definitions
GraphQLScalarType
class GraphQLScalarType<InternalType> {
  constructor(config: GraphQLScalarTypeConfig<InternalType>)
}
 
type GraphQLScalarTypeConfig<InternalType> = {
  name: string;
  description?: ?string;
  serialize: (value: mixed) => ?InternalType;
  parseValue?: (value: mixed) => ?InternalType;
  parseLiteral?: (valueAST: Value) => ?InternalType;
}
The leaf values of any request and input values to arguments are Scalars (or Enums) and are defined with a name and a series of serialization functions used to ensure validity.

Example
var OddType = new GraphQLScalarType({
  name: 'Odd',
  serialize: oddValue,
  parseValue: oddValue,
  parseLiteral(ast) {
    if (ast.kind === Kind.INT) {
      return oddValue(parseInt(ast.value, 10));
    }
    return null;
  }
});
 
function oddValue(value) {
  return value % 2 === 1 ? value : null;
}
GraphQLObjectType
class GraphQLObjectType {
  constructor(config: GraphQLObjectTypeConfig)
}
 
type GraphQLObjectTypeConfig = {
  name: string;
  interfaces?: GraphQLInterfacesThunk | Array<GraphQLInterfaceType>;
  fields: GraphQLFieldConfigMapThunk | GraphQLFieldConfigMap;
  isTypeOf?: (value: any, info?: GraphQLResolveInfo) => boolean;
  description?: ?string
}
 
type GraphQLInterfacesThunk = () => Array<GraphQLInterfaceType>;
 
type GraphQLFieldConfigMapThunk = () => GraphQLFieldConfigMap;
 
// See below about resolver functions.
type GraphQLFieldResolveFn = (
  source?: any,
  args?: {[argName: string]: any},
  context?: any,
  info?: GraphQLResolveInfo
) => any
 
type GraphQLResolveInfo = {
  fieldName: string,
  fieldNodes: Array<Field>,
  returnType: GraphQLOutputType,
  parentType: GraphQLCompositeType,
  schema: GraphQLSchema,
  fragments: { [fragmentName: string]: FragmentDefinition },
  rootValue: any,
  operation: OperationDefinition,
  variableValues: { [variableName: string]: any },
}
 
type GraphQLFieldConfig = {
  type: GraphQLOutputType;
  args?: GraphQLFieldConfigArgumentMap;
  resolve?: GraphQLFieldResolveFn;
  deprecationReason?: string;
  description?: ?string;
}
 
type GraphQLFieldConfigArgumentMap = {
  [argName: string]: GraphQLArgumentConfig;
};
 
type GraphQLArgumentConfig = {
  type: GraphQLInputType;
  defaultValue?: any;
  description?: ?string;
}
 
type GraphQLFieldConfigMap = {
  [fieldName: string]: GraphQLFieldConfig;
};
Almost all of the GraphQL types you define will be object types. Object types have a name, but most importantly describe their fields.

When two types need to refer to each other, or a type needs to refer to itself in a field, you can use a function expression (aka a closure or a thunk) to supply the fields lazily.

Note that resolver functions are provided the source object as the first parameter. However, if a resolver function is not provided, then the default resolver is used, which looks for a method on source of the same name as the field. If found, the method is called with (args, context, info). Since it is a method on source, that value can always be referenced with this.

Examples
var AddressType = new GraphQLObjectType({
  name: 'Address',
  fields: {
    street: { type: GraphQLString },
    number: { type: GraphQLInt },
    formatted: {
      type: GraphQLString,
      resolve(obj) {
        return obj.number + ' ' + obj.street
      }
    }
  }
});
 
var PersonType = new GraphQLObjectType({
  name: 'Person',
  fields: () => ({
    name: { type: GraphQLString },
    bestFriend: { type: PersonType },
  })
});
GraphQLInterfaceType
class GraphQLInterfaceType {
  constructor(config: GraphQLInterfaceTypeConfig)
}
 
type GraphQLInterfaceTypeConfig = {
  name: string,
  fields: GraphQLFieldConfigMapThunk | GraphQLFieldConfigMap,
  resolveType?: (value: any, info?: GraphQLResolveInfo) => ?GraphQLObjectType,
  description?: ?string
};
When a field can return one of a heterogeneous set of types, a Interface type is used to describe what types are possible, what fields are in common across all types, as well as a function to determine which type is actually used when the field is resolved.

Example
var EntityType = new GraphQLInterfaceType({
  name: 'Entity',
  fields: {
    name: { type: GraphQLString }
  }
});
GraphQLUnionType
class GraphQLUnionType {
  constructor(config: GraphQLUnionTypeConfig)
}
 
type GraphQLUnionTypeConfig = {
  name: string,
  types: GraphQLObjectsThunk | Array<GraphQLObjectType>,
  resolveType?: (value: any, info?: GraphQLResolveInfo) => ?GraphQLObjectType;
  description?: ?string;
};
 
type GraphQLObjectsThunk = () => Array<GraphQLObjectType>;
When a field can return one of a heterogeneous set of types, a Union type is used to describe what types are possible as well as providing a function to determine which type is actually used when the field is resolved.

Example
var PetType = new GraphQLUnionType({
  name: 'Pet',
  types: [ DogType, CatType ],
  resolveType(value) {
    if (value instanceof Dog) {
      return DogType;
    }
    if (value instanceof Cat) {
      return CatType;
    }
  }
});
GraphQLEnumType
class GraphQLEnumType {
  constructor(config: GraphQLEnumTypeConfig)
}
 
type GraphQLEnumTypeConfig = {
  name: string;
  values: GraphQLEnumValueConfigMap;
  description?: ?string;
}
 
type GraphQLEnumValueConfigMap = {
  [valueName: string]: GraphQLEnumValueConfig;
};
 
type GraphQLEnumValueConfig = {
  value?: any;
  deprecationReason?: string;
  description?: ?string;
}
 
type GraphQLEnumValueDefinition = {
  name: string;
  value?: any;
  deprecationReason?: string;
  description?: ?string;
}
Some leaf values of requests and input values are Enums. GraphQL serializes Enum values as strings, however internally Enums can be represented by any kind of type, often integers.

Note: If a value is not provided in a definition, the name of the enum value will be used as its internal value.

Example
var RGBType = new GraphQLEnumType({
  name: 'RGB',
  values: {
    RED: { value: 0 },
    GREEN: { value: 1 },
    BLUE: { value: 2 }
  }
});
GraphQLInputObjectType
class GraphQLInputObjectType {
  constructor(config: GraphQLInputObjectConfig)
}
 
type GraphQLInputObjectConfig = {
  name: string;
  fields: GraphQLInputObjectConfigFieldMapThunk | GraphQLInputObjectConfigFieldMap;
  description?: ?string;
}
 
type GraphQLInputObjectConfigFieldMapThunk = () => GraphQLInputObjectConfigFieldMap;
 
type GraphQLInputObjectFieldConfig = {
  type: GraphQLInputType;
  defaultValue?: any;
  description?: ?string;
}
 
type GraphQLInputObjectConfigFieldMap = {
  [fieldName: string]: GraphQLInputObjectFieldConfig;
};
 
type GraphQLInputObjectField = {
  name: string;
  type: GraphQLInputType;
  defaultValue?: any;
  description?: ?string;
}
 
type GraphQLInputObjectFieldMap = {
  [fieldName: string]: GraphQLInputObjectField;
};
An input object defines a structured collection of fields which may be supplied to a field argument.

Using NonNull will ensure that a value must be provided by the query

Example
var GeoPoint = new GraphQLInputObjectType({
  name: 'GeoPoint',
  fields: {
    lat: { type: new GraphQLNonNull(GraphQLFloat) },
    lon: { type: new GraphQLNonNull(GraphQLFloat) },
    alt: { type: GraphQLFloat, defaultValue: 0 },
  }
});
GraphQLList
class GraphQLList {
  constructor(type: GraphQLType)
}
A list is a kind of type marker, a wrapping type which points to another type. Lists are often created within the context of defining the fields of an object type.

Example
var PersonType = new GraphQLObjectType({
  name: 'Person',
  fields: () => ({
    parents: { type: new GraphQLList(PersonType) },
    children: { type: new GraphQLList(PersonType) },
  })
});
GraphQLNonNull
class GraphQLNonNull {
  constructor(type: GraphQLType)
}
A non-null is a kind of type marker, a wrapping type which points to another type. Non-null types enforce that their values are never null and can ensure an error is raised if this ever occurs during a request. It is useful for fields which you can make a strong guarantee on non-nullability, for example usually the id field of a database row will never be null.

Example
var RowType = new GraphQLObjectType({
  name: 'Row',
  fields: () => ({
    id: { type: new GraphQLNonNull(String) },
  })
});
Predicates
isInputType
function isInputType(type: ?GraphQLType): boolean
These types may be used as input types for arguments and directives.

isOutputType
function isOutputType(type: ?GraphQLType): boolean
These types may be used as output types as the result of fields

isLeafType
function isLeafType(type: ?GraphQLType): boolean
These types may describe types which may be leaf values

isCompositeType
function isCompositeType(type: ?GraphQLType): boolean
These types may describe the parent context of a selection set

isAbstractType
function isAbstractType(type: ?GraphQLType): boolean
These types may describe a combination of object types

Un-modifiers
getNullableType
function getNullableType(type: ?GraphQLType): ?GraphQLNullableType
If a given type is non-nullable, this strips the non-nullability and returns the underlying type.

getNamedType
function getNamedType(type: ?GraphQLType): ?GraphQLNamedType
If a given type is non-nullable or a list, this repeated strips the non-nullability and list wrappers and returns the underlying type.

Scalars
GraphQLInt
var GraphQLInt: GraphQLScalarType;
A GraphQLScalarType that represents an int.

GraphQLFloat
var GraphQLFloat: GraphQLScalarType;
A GraphQLScalarType that represents a float.

GraphQLString
var GraphQLString: GraphQLScalarType;
A GraphQLScalarType that represents a string.

GraphQLBoolean
var GraphQLBoolean: GraphQLScalarType;
A GraphQLScalarType that represents a boolean.

GraphQLID
var GraphQLID: GraphQLScalarType;
A GraphQLScalarType that represents an ID.

Continue Reading →
graphql/utilities



Document
Definitionlist
Definition
ExecutableDefinition
TypeSystemDefinition
TypeSystemExtension
ExecutableDefinition
OperationDefinition
FragmentDefinition
OperationDefinition
SelectionSet
OperationTypeNameoptVariableDefinitionsoptDirectivesoptSelectionSet
OperationType
query	mutation	subscription
SelectionSet
{Selectionlist}
Selection
Field
FragmentSpread
InlineFragment
Field
AliasoptNameArgumentsoptDirectivesoptSelectionSetopt
Alias
Name:
ArgumentsConst
(ArgumentConstlist)
ArgumentConst
Name:ValueConst
FragmentSpread
...FragmentNameDirectivesopt
InlineFragment
...TypeConditionoptDirectivesoptSelectionSet
FragmentDefinition
fragmentFragmentNameTypeConditionDirectivesoptSelectionSet
FragmentName
Nameon
TypeCondition
onNamedType
ValueConst
ConstVariable
IntValue
FloatValue
StringValue
BooleanValue
NullValue
EnumValue
ListValueConst
ObjectValueConst
BooleanValue
true	false
NullValue
null
EnumValue
Nametruefalsenull
ListValueConst
[]
[ValueConstlist]
ObjectValueConst
{}
{ObjectFieldConstlist}
ObjectFieldConst
Name:ValueConst
VariableDefinitions
(VariableDefinitionlist)
VariableDefinition
Variable:TypeDefaultValueopt
Variable
$Name
DefaultValue
=ValueConst
Type
NamedType
ListType
NonNullType
NamedType
Name
ListType
[Type]
NonNullType
NamedType!
ListType!
DirectivesConst
DirectiveConstlist
DirectiveConst
@NameArgumentsConstopt
TypeSystemDefinition
SchemaDefinition
TypeDefinition
DirectiveDefinition
TypeSystemExtension
SchemaExtension
TypeExtension
SchemaDefinition
schemaDirectivesConstopt{OperationTypeDefinitionlist}
SchemaExtension
extendschemaDirectivesConstopt{OperationTypeDefinitionlist}
extendschemaDirectivesConst
OperationTypeDefinition
OperationType:NamedType
Description
StringValue
TypeDefinition
ScalarTypeDefinition
ObjectTypeDefinition
InterfaceTypeDefinition
UnionTypeDefinition
EnumTypeDefinition
InputObjectTypeDefinition
TypeExtension
ScalarTypeExtension
ObjectTypeExtension
InterfaceTypeExtension
UnionTypeExtension
EnumTypeExtension
InputObjectTypeExtension
ScalarTypeDefinition
DescriptionoptscalarNameDirectivesConstopt
ScalarTypeExtension
extendscalarNameDirectivesConst
ObjectTypeDefinition
DescriptionopttypeNameImplementsInterfacesoptDirectivesConstoptFieldsDefinitionopt
ObjectTypeExtension
extendtypeNameImplementsInterfacesoptDirectivesConstoptFieldsDefinition
extendtypeNameImplementsInterfacesoptDirectivesConst
extendtypeNameImplementsInterfaces
ImplementsInterfaces
implements&optNamedType
ImplementsInterfaces&NamedType
FieldsDefinition
{FieldDefinitionlist}
FieldDefinition
DescriptionoptNameArgumentsDefinitionopt:TypeDirectivesConstopt
ArgumentsDefinition
(InputValueDefinitionlist)
InputValueDefinition
DescriptionoptName:TypeDefaultValueoptDirectivesConstopt
InterfaceTypeDefinition
DescriptionoptinterfaceNameDirectivesConstoptFieldsDefinitionopt
InterfaceTypeExtension
extendinterfaceNameDirectivesConstoptFieldsDefinition
extendinterfaceNameDirectivesConst
UnionTypeDefinition
DescriptionoptunionNameDirectivesConstoptUnionMemberTypesopt
UnionMemberTypes
=|optNamedType
UnionMemberTypes|NamedType
UnionTypeExtension
extendunionNameDirectivesConstoptUnionMemberTypes
extendunionNameDirectivesConst
EnumTypeDefinition
DescriptionoptenumNameDirectivesConstoptEnumValuesDefinitionopt
EnumValuesDefinition
{EnumValueDefinitionlist}
EnumValueDefinition
DescriptionoptEnumValueDirectivesConstopt
EnumTypeExtension
extendenumNameDirectivesConstoptEnumValuesDefinition
extendenumNameDirectivesConst
InputObjectTypeDefinition
DescriptionoptinputNameDirectivesConstoptInputFieldsDefinitionopt
InputFieldsDefinition
{InputValueDefinitionlist}
InputObjectTypeExtension
extendinputNameDirectivesConstoptInputFieldsDefinition
extendinputNameDirectivesConst
DirectiveDefinition
Descriptionoptdirective@NameArgumentsDefinitionoptonDirectiveLocations
DirectiveLocations
|optDirectiveLocation
DirectiveLocations|DirectiveLocation
DirectiveLocation
ExecutableDirectiveLocation
TypeSystemDirectiveLocation
ExecutableDirectiveLocation
QUERY
MUTATION
SUBSCRIPTION
FIELD
FRAGMENT_DEFINITION
FRAGMENT_SPREAD
INLINE_FRAGMENT
TypeSystemDirectiveLocation
SCHEMA
SCALAR
OBJECT
FIELD_DEFINITION
ARGUMENT_DEFINITION
INTERFACE
UNION
ENUM
ENUM_VALUE
INPUT_OBJECT
INPUT_FIELD_DEFINITION
§
"""