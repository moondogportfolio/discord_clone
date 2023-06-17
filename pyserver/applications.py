from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List, Union
from devtools import debug

class AppCommandOption(BaseModel):
    # type: 'string' #TODO 
    name: str
    description: str
    required: bool = False
    choices: Optional[Union[str, int]]
    options: Optional[List[AppCommandOption]] = None

AppCommandOption.update_forward_refs()

class AppCommand(BaseModel):
    # type: #TODO
    name: str
    description: str
    options: Optional[List[AppCommandOption]] = None
    default_permission: bool = True


def generate_default_apps():
    tableflip = AppCommand.construct(
        name = 'tableflip',
        description = 'Flip a table.'
    )
    shrug = AppCommand.construct(
        name = 'shrug',
        description = f'Append a ¯\_(ツ)_/¯ at the end of your messages.',
        options = [AppCommandOption(
            name = 'message',
            type = 'Message.',
            description = f'¯\_(ツ)_/¯'
        )]
    )
    nick = AppCommand.construct(
        name = 'nick',
        description = 'Change nickname on this server.',
        options = [AppCommandOption(
            name = 'new_nick',
            type = 'string',
            description = 'Change nickname on this server.',
            required = True
        )]
    )
    test = AppCommand.construct(
        name = 'test',
        description = 'Test.',
        options = [
            AppCommandOption(
                name = 'option1',
                type = 'string',
                description = 'Description for OPTION ONE.',
                required = True
            ),
            AppCommandOption(
                name = 'option2',
                type = 'string',
                description = 'Description for OPTION TWO.',
                required = True
            ),
            AppCommandOption(
                name = 'option3',
                type = 'string',
                description = 'Description for OPTION THREE.',
                required = True
            )
        ]
    )
    return [tableflip, nick, shrug, test]
