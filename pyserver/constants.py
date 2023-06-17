IMAGE_FORMATS = [
    'png',
    'jpg',
    'jpeg',
    'webp',
    'gif'    
]

ROOM_SERVER_POST_MSG_EX = {
    'normal': {
        'summary': 'Regular post.',
        'value': {
            "author": "60e94ad49a39c29595d1589e",
            "content": "Sample post."
        }
    },
    'reply': {
        'summary': 'Reply to an existing post.',
        'value': {
            "author": "60e94ad49a39c29595d1589e",
            "content": "Sample post.",
            "message_reference": "60fa98581a4f3a1516ce5be3"
        }
    }
}

SERVER_MODIFY_EX = {
    'addrole': {
        'summary': 'Add roles.',
        'value': {
            "roles": {
                "name": "Test Role",
                "color": "green",
                "hoist": True,
                "position": 0,
                "permissions": 64,
                "mentionable": True
            },
        }
    }
}

SERVER_EX = '60fe857d91197bda2a76831f'

CHANNEL_EX = '60fe857d91197bda2a76831d'

SERVER_USER_EX = '60f85ed853d2239340b4f693'

ROOM_EX = '60fec9ae4df75bf9b1b203f8'

SPECIFIC_MSG_EX = '60fc16b49266bba58312b09e'

EMOJI_EX = '60fbdaafe543db85aae14974'