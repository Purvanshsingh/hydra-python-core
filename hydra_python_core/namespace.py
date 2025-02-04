"""
Namespace for hydra vocabulary
"""

hydraNamespace = "http://www.w3.org/ns/hydra/core#"

hydra = {
    "namespace": hydraNamespace,
    "apiDocumentation": hydraNamespace + "apiDocumentation",
    "description": hydraNamespace + "description",
    "entrypoint": hydraNamespace + "entrypoint",
    "supportedClass": hydraNamespace + "supportedClass",
    "title": hydraNamespace + "title",

    "ApiDocumentation": hydraNamespace + "ApiDocumentation",

    "mapping": hydraNamespace + "mapping",
    "object": hydraNamespace + "object",
    "property": hydraNamespace + "property",
    "subject": hydraNamespace + "subject",
    "template": hydraNamespace + "template",
    "variable": hydraNamespace + "variable",
    "variableRepresentation": hydraNamespace + "variableRepresentation",

    "BasicRepresentation": hydraNamespace + "BasicRepresentation",
    "IriTemplate": hydraNamespace + "IriTemplate",
    "IriTemplateMapping": hydraNamespace + "IriTemplateMapping",
    "Link": hydraNamespace + "Link",
    "TemplatedLink": hydraNamespace + "TemplatedLink",
    "VariableRepresentation": hydraNamespace + "VariableRepresentation",

    "collection": hydraNamespace + "collection",
    "manages": hydraNamespace + "manages",
    "member": hydraNamespace + "member",
    "pageIndex": hydraNamespace + "pageIndex",
    "pageReference": hydraNamespace + "pageReference",
    "totalItems": hydraNamespace + "totalItems",

    "Collection": hydraNamespace + "Collection",
    "PartialCollectionView": hydraNamespace + "PartialCollectionView",

    "readable": hydraNamespace + "readable",
    "required": hydraNamespace + "required",
    "supportedOperation": hydraNamespace + "supportedOperation",
    "supportedProperty": hydraNamespace + "supportedProperty",
    "writeable": hydraNamespace + "writeable",

    "Class": hydraNamespace + "Class",
    "SupportedProperty": hydraNamespace + "SupportedProperty",

    "expects": hydraNamespace + "expects",
    "expectsHeader": hydraNamespace + "expectsHeader",
    "method": hydraNamespace + "method",
    "possibleStatus": hydraNamespace + "possibleStatus",
    "returns": hydraNamespace + "returns",
    "returnsHeader": hydraNamespace + "returnsHeader",
    "statusCode": hydraNamespace + "statusCode",

    "Operation": hydraNamespace + "Operation",
    "Status": hydraNamespace + "Status",

    "operation": hydraNamespace + "operation",

    "Resource": hydraNamespace + "Resource",

    "first": hydraNamespace + "first",
    "freetextQuery": hydraNamespace + "freetextQuery",
    "last": hydraNamespace + "last",
    "next": hydraNamespace + "next",
    "previous": hydraNamespace + "previous",
    "search": hydraNamespace + "search",
    "view": hydraNamespace + "view"
}
rdfNamespace = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

rdf = {
    "namespace": rdfNamespace,
    "Property": rdfNamespace + "Property",
    "type": rdfNamespace + "type"
}
rdfsNamespace = "http://www.w3.org/2000/01/rdf-schema#"

rdfs = {
    "namespace": rdfsNamespace,
    "comment": rdfsNamespace + "comment",
    "domain": rdfsNamespace + "domain",
    "label": rdfsNamespace + "label",
    "range": rdfsNamespace + "range"
}
