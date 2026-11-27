"""
Pytconf param types
"""


import abc
import typing
from typing import Any, override

from pytconf.convert import (
    convert_bool_to_str,
    convert_int_or_none_to_str,
    convert_int_to_str,
    convert_list_int_to_str,
    convert_list_str_to_str,
    convert_str_or_none_to_str,
    convert_str_to_bool,
    convert_str_to_int,
    convert_str_to_int_default,
    convert_str_to_int_or_none,
    convert_str_to_list_int,
    convert_str_to_list_str,
    convert_str_to_str,
    convert_str_to_str_or_none,
)
from pytconf.enum_subset import EnumSubset
from pytconf.extended_enum import enum_type_to_list_str, str_to_enum_value
from pytconf.param_collector import the_collector

if typing.TYPE_CHECKING:
    from collections.abc import Callable
    from enum import Enum

NO_HELP = "No help for this configuration option"


class Unique:
    """ A object with a unique value """


NO_DEFAULT = Unique()


class Param(abc.ABC):
    """
    Parent class of all parameters of configuration
    """

    def __init__(
        self,
        help_string: str = NO_HELP,
        default: Any = NO_DEFAULT,
        type_name: str | None = None,
    ) -> None:
        super().__init__()
        self.help_string = help_string
        self.required = default is NO_DEFAULT
        self.default = default
        self.type_name = type_name

    def get_type_name(self) -> str | None:
        """ get the type name of the current object """
        return self.type_name

    def collect(self) -> None:
        """ collect the current object """
        the_collector.add_data(self)

    @abc.abstractmethod
    def s2t(self, s: str) -> object:
        """ translate string ot this type """

    def s2t_generate_from_default(self, s: str) -> object:
        """ generate object from default string """
        raise ValueError(f"we do not support generation from default [{s}]")

    @abc.abstractmethod
    def t2s(self, t: object) -> str:
        """ translate self to string """

    def more_help(self) -> str | None:
        """ get more help """
        return None


class ParamFunctions(Param):
    """
    Parent class of all parameters of configuration
    """

    def __init__(
        self,
        function_s2t: Callable[..., Any],
        function_s2t_generate_from_default: Callable[..., Any],
        function_t2s: Callable[[Any], str],
        help_string: str = NO_HELP,
        default: Any = None,
        type_name: str | None = None,
    ) -> None:
        super().__init__(
            help_string=help_string,
            default=default,
            type_name=type_name,
        )
        self.function_s2t = function_s2t
        self.function_t2s = function_t2s
        self.function_s2t_generate_from_default = function_s2t_generate_from_default
        super().collect()

    def s2t(self, s: str) -> Any:
        return self.function_s2t(s)

    @override
    def s2t_generate_from_default(self, s: str) -> Any:
        return self.function_s2t_generate_from_default(self.default, s)

    def t2s(self, t: Any) -> str:
        return self.function_t2s(t)


class ParamFilename(Param):
    def __init__(
        self,
        help_string: str = NO_HELP,
        default: Unique | str = NO_DEFAULT,
        type_name: str | None = None,
        suffixes: list[str] | None = None,
    ) -> None:
        super().__init__(
            help_string=help_string,
            default=default,
            type_name=type_name,
        )
        self.suffixes = suffixes
        super().collect()

    def s2t(self, s: str):
        if self.suffixes is not None:
            assert any(
                s.endswith(x) for x in self.suffixes
            ), "filename suffix is not accepted"
        return s

    def t2s(self, t: Any) -> str:
        return str(t)

    @override
    def more_help(self) -> str:
        if self.suffixes is None:
            return "no limitation on suffixes"
        return f"allowed suffixes are {self.suffixes}"


class ParamEnum(Param):
    def __init__(
        self,
        enum_type: type[Enum],
        help_string: str = NO_HELP,
        default: Any = NO_DEFAULT,
    ) -> None:
        super().__init__(
            help_string=help_string,
            default=default,
            type_name="enum",
        )
        self.enum_type = enum_type
        super().collect()

    @override
    def get_type_name(self) -> str:
        return f"Enum[{self.enum_type.__name__}]"

    def s2t(self, s: str) -> Any:
        return str_to_enum_value(s, self.enum_type)

    def t2s(self, t: Any) -> str:
        return str(t.name)

    @override
    def more_help(self) -> str:
        return f"allowed values {enum_type_to_list_str(self.enum_type)}"


class ParamEnumSubset(Param):
    def __init__(
        self,
        help_string: str = NO_HELP,
        default: Any = NO_DEFAULT,
        enum_type: type[Enum] | None = None,
    ) -> None:
        super().__init__(
            help_string=help_string,
            default=default,
            type_name="enum",
        )
        self.enum_type = enum_type
        super().collect()

    @override
    def get_type_name(self) -> str:
        name = self.enum_type.__name__ if self.enum_type is not None else "None"
        return f"EnumSubset[{name}]"

    def s2t(self, s: str) -> EnumSubset:
        assert self.enum_type is not None, "ParamEnumSubset requires enum_type"
        return EnumSubset.from_string(e=self.enum_type, s=s)

    def t2s(self, t: Any) -> str:
        return str(t.to_string())

    @typing.override
    def s2t_generate_from_default(self, s: str) -> EnumSubset | None:
        return None

    @override
    def more_help(self) -> str | None:
        if self.enum_type is None:
            return None
        return f"allowed values {enum_type_to_list_str(self.enum_type)}"


class ParamChoice(Param):
    def __init__(
        self,
        help_string: str = NO_HELP,
        default: str | Unique = NO_DEFAULT,
        choice_list: list[str] | None = None
    ) -> None:
        super().__init__(
            help_string=help_string,
            default=default,
            type_name="Choice",
        )
        self.choice_list = choice_list
        super().collect()

    def s2t(self, s: str) -> Any:
        return s

    def t2s(self, t: Any) -> str:
        return str(t)

    @override
    def more_help(self) -> str:
        all_choice_list = ",".join(self.choice_list or [])
        return f"allowed values {all_choice_list}"


class ParamCreator:
    """
    Static namespace with all the param creation functions.
    """

    @staticmethod
    def create_int(
        help_string: str = NO_HELP,
        default: int | Unique = NO_DEFAULT,
    ) -> int:
        """
        Create an int parameter
        :param help_string:
        :param default:
        :return:
        """
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="int",
            function_s2t=convert_str_to_int,
            function_t2s=convert_int_to_str,
            function_s2t_generate_from_default=convert_str_to_int_default,
        )
        return typing.cast("int", default)

    @staticmethod
    def create_list_int(
        help_string: str = NO_HELP,
        default: list[int] | Unique | None = None,
    ) -> list[int]:
        """
        Create a list[int] parameter
        :param help_string:
        :param default: None (the default) means an empty list
        :return:
        """
        if default is None:
            default = []
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="list[int]",
            function_s2t=convert_str_to_list_int,
            function_t2s=convert_list_int_to_str,
            function_s2t_generate_from_default=convert_str_to_list_int,
        )
        if not isinstance(default, list):
            return []
        return default

    @staticmethod
    def create_list_str(
        help_string: str = NO_HELP,
        default: list[str] | Unique | None = None,
    ) -> list[str]:
        """
        Create a list[str] parameter
        :param help_string:
        :param default: None (the default) means an empty list
        :return:
        """
        if default is None:
            default = []
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="list[str]",
            function_s2t=convert_str_to_list_str,
            function_t2s=convert_list_str_to_str,
            function_s2t_generate_from_default=convert_str_to_list_str,
        )
        if not isinstance(default, list):
            return []
        return default

    @staticmethod
    def create_int_or_none(
        help_string: str = NO_HELP,
        default: int | Unique | None = NO_DEFAULT,
    ) -> int | None:
        """
        Create an int parameter
        :param help_string:
        :param default:
        :return:
        """
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="Optional[int]",
            function_s2t=convert_str_to_int_or_none,
            function_t2s=convert_int_or_none_to_str,
            function_s2t_generate_from_default=convert_str_to_int_or_none,
        )
        return typing.cast("int | None", default)

    @staticmethod
    def create_str(
        help_string: str = NO_HELP,
        default: str | Unique = NO_DEFAULT,
    ) -> str:
        """
        Create a string parameter
        :param help_string:
        :param default:
        :return:
        """
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="str",
            function_s2t=convert_str_to_str,
            function_s2t_generate_from_default=convert_str_to_str,
            function_t2s=convert_str_to_str,
        )
        return typing.cast("str", default)

    @staticmethod
    def create_str_or_none(
        help_string: str = NO_HELP,
        default: str | Unique | None = NO_DEFAULT,
    ) -> str | None:
        """
        Create a string parameter
        :param help_string:
        :param default:
        :return:
        """
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="str_or_none",
            function_s2t=convert_str_to_str_or_none,
            function_s2t_generate_from_default=convert_str_to_str_or_none,
            function_t2s=convert_str_or_none_to_str,
        )
        return typing.cast("str | None", default)

    @staticmethod
    def create_bool(
        help_string: str = NO_HELP,
        *,
        default: bool | Unique = NO_DEFAULT,
    ) -> bool:
        """
        Create a bool parameter
        :param help_string:
        :param default:
        :return:
        """
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="bool",
            function_s2t=convert_str_to_bool,
            function_s2t_generate_from_default=convert_str_to_bool,
            function_t2s=convert_bool_to_str,
        )
        if default is NO_DEFAULT:
            return False
        return bool(default)

    @staticmethod
    def create_new_file(
        help_string: str = NO_HELP,
        default: str | Unique = NO_DEFAULT,
        suffixes: list[str] | None = None,
    ) -> str:
        """
        Create a new file parameter
        :param help_string:
        :param default:
        :param suffixes:
        :return:
        """
        ParamFilename(
            help_string=help_string,
            default=default,
            type_name="new_file",
            suffixes=suffixes,
        )
        return typing.cast("str", default)

    @staticmethod
    def create_existing_file(
        help_string: str = NO_HELP,
        default: str | Unique = NO_DEFAULT,
        suffixes: list[str] | None = None,
    ) -> str:
        """
        Create a new file parameter
        :param help_string:
        :param default:
        :param suffixes:
        :return:
        """
        ParamFilename(
            help_string=help_string,
            default=default,
            type_name="existing_file",
            suffixes=suffixes,
        )
        return typing.cast("str", default)

    @staticmethod
    def create_existing_folder(
        help_string: str = NO_HELP,
        default: str | Unique = NO_DEFAULT,
        suffixes: list[str] | None = None,
    ) -> str:
        """
        Create a new folder parameter
        :param help_string:
        :param default:
        :param suffixes:
        :return:
        """
        ParamFilename(
            help_string=help_string,
            default=default,
            type_name="existing_folder",
            suffixes=suffixes,
        )
        return typing.cast("str", default)

    @staticmethod
    def create_choice(
        choice_list: list[str],
        help_string: str = NO_HELP,
        default: str | Unique = NO_DEFAULT,
    ) -> str:
        """
        Create a choice config
        :param choice_list:
        :param help_string:
        :param default:
        :return:
        """
        ParamChoice(
            help_string=help_string,
            default=default,
            choice_list=choice_list,
        )
        return typing.cast("str", default)

    @staticmethod
    def create_enum(
        enum_type: type[Enum],
        help_string: str = NO_HELP,
        default: Enum | Unique = NO_DEFAULT,
    ) -> Enum:
        """
        Create an enum config
        :param enum_type:
        :param help_string:
        :param default:
        :return:
        """
        ParamEnum(
            help_string=help_string,
            default=default,
            enum_type=enum_type,
        )
        return typing.cast("Enum", default)

    @staticmethod
    def create_enum_subset(
        enum_type: type[Enum],
        help_string: str = NO_HELP,
        default: EnumSubset | Unique = NO_DEFAULT,
    ) -> EnumSubset:
        """
        Create an enum config
        :param enum_type:
        :param help_string:
        :param default:
        :return:
        """
        ParamEnumSubset(
            help_string=help_string,
            default=default,
            enum_type=enum_type,
        )
        return typing.cast("EnumSubset", default)

    @staticmethod
    def create_existing_bucket(
        help_string: str = NO_HELP,
        default: str | Unique = NO_DEFAULT,
    ) -> str:
        """
        Create a bucket name on gcp
        :param help_string:
        :param default:
        :return:
        """
        ParamFunctions(
            help_string=help_string,
            default=default,
            type_name="bucket_name",
            function_s2t=convert_str_to_str,
            function_s2t_generate_from_default=convert_str_to_str,
            function_t2s=convert_str_to_str,
        )
        return typing.cast("str", default)
