"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeBotCommand, TypeBotCommandScope, TypeBotMenuButton, TypeChatAdminRights, TypeDataJSON, TypeEmojiStatus, TypeInputMedia, TypeInputUser



class AddPreviewMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x17aeb75a
    SUBCLASS_OF_ID = 0x562abc2d

    def __init__(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia'):
        """
        :returns BotPreviewMedia: Instance of BotPreviewMedia.
        """
        self.bot = bot
        self.lang_code = lang_code
        self.media = media

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        self.media = utils.get_input_media(self.media)

    def to_dict(self):
        return {
            '_': 'AddPreviewMediaRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'lang_code': self.lang_code,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media
        }

    def _bytes(self):
        return b''.join((
            b'Z\xb7\xae\x17',
            self.bot._bytes(),
            self.serialize_bytes(self.lang_code),
            self.media._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _lang_code = reader.tgread_string()
        _media = reader.tgread_object()
        return cls(bot=_bot, lang_code=_lang_code, media=_media)


class AllowSendMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf132e3ef
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, bot: 'TypeInputUser'):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.bot = bot

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'AllowSendMessageRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot
        }

    def _bytes(self):
        return b''.join((
            b'\xef\xe32\xf1',
            self.bot._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        return cls(bot=_bot)


class AnswerWebhookJSONQueryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe6213f4d
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, query_id: int, data: 'TypeDataJSON'):
        """
        :returns Bool: This type has no constructors.
        """
        self.query_id = query_id
        self.data = data

    def to_dict(self):
        return {
            '_': 'AnswerWebhookJSONQueryRequest',
            'query_id': self.query_id,
            'data': self.data.to_dict() if isinstance(self.data, TLObject) else self.data
        }

    def _bytes(self):
        return b''.join((
            b'M?!\xe6',
            struct.pack('<q', self.query_id),
            self.data._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _query_id = reader.read_long()
        _data = reader.tgread_object()
        return cls(query_id=_query_id, data=_data)


class CanSendMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1359f4e6
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser'):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'CanSendMessageRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot
        }

    def _bytes(self):
        return b''.join((
            b'\xe6\xf4Y\x13',
            self.bot._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        return cls(bot=_bot)


class CheckDownloadFileParamsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x50077589
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser', file_name: str, url: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot
        self.file_name = file_name
        self.url = url

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'CheckDownloadFileParamsRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'file_name': self.file_name,
            'url': self.url
        }

    def _bytes(self):
        return b''.join((
            b'\x89u\x07P',
            self.bot._bytes(),
            self.serialize_bytes(self.file_name),
            self.serialize_bytes(self.url),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _file_name = reader.tgread_string()
        _url = reader.tgread_string()
        return cls(bot=_bot, file_name=_file_name, url=_url)


class DeletePreviewMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2d0135b3
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser', lang_code: str, media: List['TypeInputMedia']):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot
        self.lang_code = lang_code
        self.media = media

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        _tmp = []
        for _x in self.media:
            _tmp.append(utils.get_input_media(_x))

        self.media = _tmp

    def to_dict(self):
        return {
            '_': 'DeletePreviewMediaRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'lang_code': self.lang_code,
            'media': [] if self.media is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.media]
        }

    def _bytes(self):
        return b''.join((
            b'\xb35\x01-',
            self.bot._bytes(),
            self.serialize_bytes(self.lang_code),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.media)),b''.join(x._bytes() for x in self.media),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _lang_code = reader.tgread_string()
        reader.read_int()
        _media = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _media.append(_x)

        return cls(bot=_bot, lang_code=_lang_code, media=_media)


class EditPreviewMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8525606f
    SUBCLASS_OF_ID = 0x562abc2d

    def __init__(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia', new_media: 'TypeInputMedia'):
        """
        :returns BotPreviewMedia: Instance of BotPreviewMedia.
        """
        self.bot = bot
        self.lang_code = lang_code
        self.media = media
        self.new_media = new_media

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        self.media = utils.get_input_media(self.media)
        self.new_media = utils.get_input_media(self.new_media)

    def to_dict(self):
        return {
            '_': 'EditPreviewMediaRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'lang_code': self.lang_code,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media,
            'new_media': self.new_media.to_dict() if isinstance(self.new_media, TLObject) else self.new_media
        }

    def _bytes(self):
        return b''.join((
            b'o`%\x85',
            self.bot._bytes(),
            self.serialize_bytes(self.lang_code),
            self.media._bytes(),
            self.new_media._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _lang_code = reader.tgread_string()
        _media = reader.tgread_object()
        _new_media = reader.tgread_object()
        return cls(bot=_bot, lang_code=_lang_code, media=_media, new_media=_new_media)


class GetBotCommandsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe34c0dd6
    SUBCLASS_OF_ID = 0xfae91529

    def __init__(self, scope: 'TypeBotCommandScope', lang_code: str):
        """
        :returns Vector<BotCommand>: This type has no constructors.
        """
        self.scope = scope
        self.lang_code = lang_code

    def to_dict(self):
        return {
            '_': 'GetBotCommandsRequest',
            'scope': self.scope.to_dict() if isinstance(self.scope, TLObject) else self.scope,
            'lang_code': self.lang_code
        }

    def _bytes(self):
        return b''.join((
            b'\xd6\rL\xe3',
            self.scope._bytes(),
            self.serialize_bytes(self.lang_code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _scope = reader.tgread_object()
        _lang_code = reader.tgread_string()
        return cls(scope=_scope, lang_code=_lang_code)


class GetBotInfoRequest(TLRequest):
    CONSTRUCTOR_ID = 0xdcd914fd
    SUBCLASS_OF_ID = 0xca7b2235

    def __init__(self, lang_code: str, bot: Optional['TypeInputUser']=None):
        """
        :returns bots.BotInfo: Instance of BotInfo.
        """
        self.lang_code = lang_code
        self.bot = bot

    async def resolve(self, client, utils):
        if self.bot:
            self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'GetBotInfoRequest',
            'lang_code': self.lang_code,
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot
        }

    def _bytes(self):
        return b''.join((
            b'\xfd\x14\xd9\xdc',
            struct.pack('<I', (0 if self.bot is None or self.bot is False else 1)),
            b'' if self.bot is None or self.bot is False else (self.bot._bytes()),
            self.serialize_bytes(self.lang_code),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _bot = reader.tgread_object()
        else:
            _bot = None
        _lang_code = reader.tgread_string()
        return cls(lang_code=_lang_code, bot=_bot)


class GetBotMenuButtonRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9c60eb28
    SUBCLASS_OF_ID = 0x4c71bd3c

    def __init__(self, user_id: 'TypeInputUser'):
        """
        :returns BotMenuButton: Instance of either BotMenuButtonDefault, BotMenuButtonCommands, BotMenuButton.
        """
        self.user_id = user_id

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'GetBotMenuButtonRequest',
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id
        }

    def _bytes(self):
        return b''.join((
            b'(\xeb`\x9c',
            self.user_id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _user_id = reader.tgread_object()
        return cls(user_id=_user_id)


class GetPopularAppBotsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xc2510192
    SUBCLASS_OF_ID = 0x7b64be7d

    def __init__(self, offset: str, limit: int):
        """
        :returns bots.PopularAppBots: Instance of PopularAppBots.
        """
        self.offset = offset
        self.limit = limit

    def to_dict(self):
        return {
            '_': 'GetPopularAppBotsRequest',
            'offset': self.offset,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'\x92\x01Q\xc2',
            self.serialize_bytes(self.offset),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _offset = reader.tgread_string()
        _limit = reader.read_int()
        return cls(offset=_offset, limit=_limit)


class GetPreviewInfoRequest(TLRequest):
    CONSTRUCTOR_ID = 0x423ab3ad
    SUBCLASS_OF_ID = 0xf0c27f35

    def __init__(self, bot: 'TypeInputUser', lang_code: str):
        """
        :returns bots.PreviewInfo: Instance of PreviewInfo.
        """
        self.bot = bot
        self.lang_code = lang_code

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'GetPreviewInfoRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'lang_code': self.lang_code
        }

    def _bytes(self):
        return b''.join((
            b'\xad\xb3:B',
            self.bot._bytes(),
            self.serialize_bytes(self.lang_code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _lang_code = reader.tgread_string()
        return cls(bot=_bot, lang_code=_lang_code)


class GetPreviewMediasRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa2a5594d
    SUBCLASS_OF_ID = 0xf9862a78

    def __init__(self, bot: 'TypeInputUser'):
        """
        :returns Vector<BotPreviewMedia>: This type has no constructors.
        """
        self.bot = bot

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'GetPreviewMediasRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot
        }

    def _bytes(self):
        return b''.join((
            b'MY\xa5\xa2',
            self.bot._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        return cls(bot=_bot)


class InvokeWebViewCustomMethodRequest(TLRequest):
    CONSTRUCTOR_ID = 0x87fc5e7
    SUBCLASS_OF_ID = 0xad0352e8

    def __init__(self, bot: 'TypeInputUser', custom_method: str, params: 'TypeDataJSON'):
        """
        :returns DataJSON: Instance of DataJSON.
        """
        self.bot = bot
        self.custom_method = custom_method
        self.params = params

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'InvokeWebViewCustomMethodRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'custom_method': self.custom_method,
            'params': self.params.to_dict() if isinstance(self.params, TLObject) else self.params
        }

    def _bytes(self):
        return b''.join((
            b'\xe7\xc5\x7f\x08',
            self.bot._bytes(),
            self.serialize_bytes(self.custom_method),
            self.params._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _custom_method = reader.tgread_string()
        _params = reader.tgread_object()
        return cls(bot=_bot, custom_method=_custom_method, params=_params)


class ReorderPreviewMediasRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb627f3aa
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser', lang_code: str, order: List['TypeInputMedia']):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot
        self.lang_code = lang_code
        self.order = order

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        _tmp = []
        for _x in self.order:
            _tmp.append(utils.get_input_media(_x))

        self.order = _tmp

    def to_dict(self):
        return {
            '_': 'ReorderPreviewMediasRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'lang_code': self.lang_code,
            'order': [] if self.order is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.order]
        }

    def _bytes(self):
        return b''.join((
            b"\xaa\xf3'\xb6",
            self.bot._bytes(),
            self.serialize_bytes(self.lang_code),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.order)),b''.join(x._bytes() for x in self.order),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _lang_code = reader.tgread_string()
        reader.read_int()
        _order = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _order.append(_x)

        return cls(bot=_bot, lang_code=_lang_code, order=_order)


class ReorderUsernamesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9709b1c2
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser', order: List[str]):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot
        self.order = order

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'ReorderUsernamesRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'order': [] if self.order is None else self.order[:]
        }

    def _bytes(self):
        return b''.join((
            b'\xc2\xb1\t\x97',
            self.bot._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.order)),b''.join(self.serialize_bytes(x) for x in self.order),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        reader.read_int()
        _order = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_string()
            _order.append(_x)

        return cls(bot=_bot, order=_order)


class ResetBotCommandsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3d8de0f9
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, scope: 'TypeBotCommandScope', lang_code: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.scope = scope
        self.lang_code = lang_code

    def to_dict(self):
        return {
            '_': 'ResetBotCommandsRequest',
            'scope': self.scope.to_dict() if isinstance(self.scope, TLObject) else self.scope,
            'lang_code': self.lang_code
        }

    def _bytes(self):
        return b''.join((
            b'\xf9\xe0\x8d=',
            self.scope._bytes(),
            self.serialize_bytes(self.lang_code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _scope = reader.tgread_object()
        _lang_code = reader.tgread_string()
        return cls(scope=_scope, lang_code=_lang_code)


class SendCustomRequestRequest(TLRequest):
    CONSTRUCTOR_ID = 0xaa2769ed
    SUBCLASS_OF_ID = 0xad0352e8

    def __init__(self, custom_method: str, params: 'TypeDataJSON'):
        """
        :returns DataJSON: Instance of DataJSON.
        """
        self.custom_method = custom_method
        self.params = params

    def to_dict(self):
        return {
            '_': 'SendCustomRequestRequest',
            'custom_method': self.custom_method,
            'params': self.params.to_dict() if isinstance(self.params, TLObject) else self.params
        }

    def _bytes(self):
        return b''.join((
            b"\xedi'\xaa",
            self.serialize_bytes(self.custom_method),
            self.params._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _custom_method = reader.tgread_string()
        _params = reader.tgread_object()
        return cls(custom_method=_custom_method, params=_params)


class SetBotBroadcastDefaultAdminRightsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x788464e1
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, admin_rights: 'TypeChatAdminRights'):
        """
        :returns Bool: This type has no constructors.
        """
        self.admin_rights = admin_rights

    def to_dict(self):
        return {
            '_': 'SetBotBroadcastDefaultAdminRightsRequest',
            'admin_rights': self.admin_rights.to_dict() if isinstance(self.admin_rights, TLObject) else self.admin_rights
        }

    def _bytes(self):
        return b''.join((
            b'\xe1d\x84x',
            self.admin_rights._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _admin_rights = reader.tgread_object()
        return cls(admin_rights=_admin_rights)


class SetBotCommandsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x517165a
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, scope: 'TypeBotCommandScope', lang_code: str, commands: List['TypeBotCommand']):
        """
        :returns Bool: This type has no constructors.
        """
        self.scope = scope
        self.lang_code = lang_code
        self.commands = commands

    def to_dict(self):
        return {
            '_': 'SetBotCommandsRequest',
            'scope': self.scope.to_dict() if isinstance(self.scope, TLObject) else self.scope,
            'lang_code': self.lang_code,
            'commands': [] if self.commands is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.commands]
        }

    def _bytes(self):
        return b''.join((
            b'Z\x16\x17\x05',
            self.scope._bytes(),
            self.serialize_bytes(self.lang_code),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.commands)),b''.join(x._bytes() for x in self.commands),
        ))

    @classmethod
    def from_reader(cls, reader):
        _scope = reader.tgread_object()
        _lang_code = reader.tgread_string()
        reader.read_int()
        _commands = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _commands.append(_x)

        return cls(scope=_scope, lang_code=_lang_code, commands=_commands)


class SetBotGroupDefaultAdminRightsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x925ec9ea
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, admin_rights: 'TypeChatAdminRights'):
        """
        :returns Bool: This type has no constructors.
        """
        self.admin_rights = admin_rights

    def to_dict(self):
        return {
            '_': 'SetBotGroupDefaultAdminRightsRequest',
            'admin_rights': self.admin_rights.to_dict() if isinstance(self.admin_rights, TLObject) else self.admin_rights
        }

    def _bytes(self):
        return b''.join((
            b'\xea\xc9^\x92',
            self.admin_rights._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _admin_rights = reader.tgread_object()
        return cls(admin_rights=_admin_rights)


class SetBotInfoRequest(TLRequest):
    CONSTRUCTOR_ID = 0x10cf3123
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, lang_code: str, bot: Optional['TypeInputUser']=None, name: Optional[str]=None, about: Optional[str]=None, description: Optional[str]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.lang_code = lang_code
        self.bot = bot
        self.name = name
        self.about = about
        self.description = description

    async def resolve(self, client, utils):
        if self.bot:
            self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'SetBotInfoRequest',
            'lang_code': self.lang_code,
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'name': self.name,
            'about': self.about,
            'description': self.description
        }

    def _bytes(self):
        return b''.join((
            b'#1\xcf\x10',
            struct.pack('<I', (0 if self.bot is None or self.bot is False else 4) | (0 if self.name is None or self.name is False else 8) | (0 if self.about is None or self.about is False else 1) | (0 if self.description is None or self.description is False else 2)),
            b'' if self.bot is None or self.bot is False else (self.bot._bytes()),
            self.serialize_bytes(self.lang_code),
            b'' if self.name is None or self.name is False else (self.serialize_bytes(self.name)),
            b'' if self.about is None or self.about is False else (self.serialize_bytes(self.about)),
            b'' if self.description is None or self.description is False else (self.serialize_bytes(self.description)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 4:
            _bot = reader.tgread_object()
        else:
            _bot = None
        _lang_code = reader.tgread_string()
        if flags & 8:
            _name = reader.tgread_string()
        else:
            _name = None
        if flags & 1:
            _about = reader.tgread_string()
        else:
            _about = None
        if flags & 2:
            _description = reader.tgread_string()
        else:
            _description = None
        return cls(lang_code=_lang_code, bot=_bot, name=_name, about=_about, description=_description)


class SetBotMenuButtonRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4504d54f
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, user_id: 'TypeInputUser', button: 'TypeBotMenuButton'):
        """
        :returns Bool: This type has no constructors.
        """
        self.user_id = user_id
        self.button = button

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'SetBotMenuButtonRequest',
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'button': self.button.to_dict() if isinstance(self.button, TLObject) else self.button
        }

    def _bytes(self):
        return b''.join((
            b'O\xd5\x04E',
            self.user_id._bytes(),
            self.button._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _user_id = reader.tgread_object()
        _button = reader.tgread_object()
        return cls(user_id=_user_id, button=_button)


class ToggleUserEmojiStatusPermissionRequest(TLRequest):
    CONSTRUCTOR_ID = 0x6de6392
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser', enabled: bool):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot
        self.enabled = enabled

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'ToggleUserEmojiStatusPermissionRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'enabled': self.enabled
        }

    def _bytes(self):
        return b''.join((
            b'\x92c\xde\x06',
            self.bot._bytes(),
            b'\xb5ur\x99' if self.enabled else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _enabled = reader.tgread_bool()
        return cls(bot=_bot, enabled=_enabled)


class ToggleUsernameRequest(TLRequest):
    CONSTRUCTOR_ID = 0x53ca973
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser', username: str, active: bool):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot
        self.username = username
        self.active = active

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'ToggleUsernameRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'username': self.username,
            'active': self.active
        }

    def _bytes(self):
        return b''.join((
            b's\xa9<\x05',
            self.bot._bytes(),
            self.serialize_bytes(self.username),
            b'\xb5ur\x99' if self.active else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _username = reader.tgread_string()
        _active = reader.tgread_bool()
        return cls(bot=_bot, username=_username, active=_active)


class UpdateUserEmojiStatusRequest(TLRequest):
    CONSTRUCTOR_ID = 0xed9f30c5
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, user_id: 'TypeInputUser', emoji_status: 'TypeEmojiStatus'):
        """
        :returns Bool: This type has no constructors.
        """
        self.user_id = user_id
        self.emoji_status = emoji_status

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'UpdateUserEmojiStatusRequest',
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'emoji_status': self.emoji_status.to_dict() if isinstance(self.emoji_status, TLObject) else self.emoji_status
        }

    def _bytes(self):
        return b''.join((
            b'\xc50\x9f\xed',
            self.user_id._bytes(),
            self.emoji_status._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _user_id = reader.tgread_object()
        _emoji_status = reader.tgread_object()
        return cls(user_id=_user_id, emoji_status=_emoji_status)

