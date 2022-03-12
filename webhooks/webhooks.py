"""Main module used to send messages with a created webhook"""

import types

import requests
from .codes import codes


class Webhook:
    """Main instance used to send webhook and create them"""

    def __init__(
        self,
        url: str,
        username: str = None,
        avatar: str = None,
    ) -> None:
        """Initialize the class

        Args:
            `url` (str): The Url of the webhook
            `username` (str, optional): The username the webhook will have
            `avatar` (str, optional): The avatar url the webhook will have. Defaults to None.
        """
        self.url = url
        self.username = username
        self.avatar = avatar

    def send_message(self, msg: str) -> codes:
        """Sends a message with the webhook

        Args:
            `msg` (str): The message

        Returns:
            `codes`: The status code of the response
        """
        data = {"content": msg, "tts": False}

        if not isinstance(self.avatar, types.NoneType):
            data["avatar_url"] = self.avatar

        if not isinstance(self.avatar, types.NoneType):
            data["username"] = self.username

        res = requests.post(f"{self.url}?wait=true", data)

        return f"{res.status_code}: {codes[res.status_code][0]}"

    def change(self, prop: str, value: any) -> bool:
        """Change a property from the webhook

        Args:
            `property` (str): [description]
            `value` (any): [description]

        Returns:
            `bool`: True or False if the operation was correct or not
        """
        if not self.__getattribute__(prop):
            return False
        else:
            self.__setattr__(prop, value)
            return True
