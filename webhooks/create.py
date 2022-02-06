import requests
from .codes import codes


def create(channelId: str, name: str = "Captain Hook", avatar: str = None) -> str:
    """Generates a webhook and returns its url

    Args:
        `channelId` (str): The id of the channel where the webhook is going to be
        `name` (str, optional): The name of the new webhook. Defaults to "Captain Hook".
        `avatar` (str, optional): The avatar url of the webhook. Defaults to None.

    Returns:
            `str`: The webhook data
    """

    data = {
        "name": name,
    }

    if avatar is not None:
        data["avatar"] = avatar

    res = requests.post(f"https://discord.com/api/v9/channels/{channelId}/webhooks", data)

    return (f"{res.status_code}: {codes[res.status_code][0]}", res.json())
