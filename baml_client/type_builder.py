###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import typing
from baml_py.type_builder import FieldType, TypeBuilder as _TypeBuilder, ClassPropertyBuilder, EnumValueBuilder, EnumBuilder, ClassBuilder

class TypeBuilder(_TypeBuilder):
    def __init__(self):
        super().__init__(classes=set(
          ["Answer","BookAnalysis","CharacterDescription","Citation","Company","Context","CytoscapeEdge","CytoscapeEdgeData","CytoscapeJSON","CytoscapeNode","Document","DynamicOutput","Education","Elements","Event","Message","PopularityOverTime","Ranking","Resume","Score","Speaker","Spells","WordCount",]
        ), enums=set(
          ["Category","MyEnum","Role",]
        ))



    @property
    
    def DynamicOutput(self) -> "DynamicOutputBuilder":
        return DynamicOutputBuilder(self)




class DynamicOutputBuilder:
    def __init__(self, tb: _TypeBuilder):
        self.__bldr = tb._tb.class_("DynamicOutput")
        self.__properties = set([])
        self.__props = DynamicOutputProperties(self.__bldr, self.__properties)

    def type(self) -> FieldType:
        return self.__bldr.field()

    @property
    def props(self) -> "DynamicOutputProperties":
        return self.__props
    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyBuilder]]:
        return [(name, self.__bldr.property(name)) for name in self.__properties]

    def add_property(self, name: str, type: FieldType) -> ClassPropertyBuilder:
        if name in self.__properties:
            raise ValueError(f"Property {name} already exists.")
        return ClassPropertyBuilder(self.__bldr.property(name).type(type))

class DynamicOutputProperties:
    def __init__(self, cls_bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = cls_bldr
        self.__properties = properties

    

    def __getattr__(self, name: str) -> ClassPropertyBuilder:
        if name not in self.__properties:
            raise AttributeError(f"Property {name} not found.")
        return ClassPropertyBuilder(self.__bldr.property(name))




__all__ = ["TypeBuilder"]