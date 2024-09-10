"""Telegram Media 模型。"""
# autogenerated by codegen.py, do not edit manually.
# ruff: noqa: D101, D102, A002
# pylint: disable=missing-class-docstring

from typing import Optional, Union

from pydantic import BaseModel

from .message import TelegramMessage
from .model import (
    InputFile,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    InputPaidMedia,
    InputPollOption,
    LabeledPrice,
)


class TelegramMedia(BaseModel):
    pass


class Photo(TelegramMedia):
    photo: Union[InputFile, str]
    caption: Union[None, str, TelegramMessage] = None
    show_caption_above_media: Optional[bool] = None
    has_spoiler: Optional[bool] = None


class Audio(TelegramMedia):
    audio: Union[InputFile, str]
    caption: Union[None, str, TelegramMessage] = None
    duration: Optional[int] = None
    performer: Optional[str] = None
    title: Optional[str] = None
    thumbnail: Optional[Union[InputFile, str]] = None


class Document(TelegramMedia):
    document: Union[InputFile, str]
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Union[None, str, TelegramMessage] = None
    disable_content_type_detection: Optional[bool] = None


class Video(TelegramMedia):
    video: Union[InputFile, str]
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Union[None, str, TelegramMessage] = None
    show_caption_above_media: Optional[bool] = None
    has_spoiler: Optional[bool] = None
    supports_streaming: Optional[bool] = None


class Animation(TelegramMedia):
    animation: Union[InputFile, str]
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Union[None, str, TelegramMessage] = None
    show_caption_above_media: Optional[bool] = None
    has_spoiler: Optional[bool] = None


class Voice(TelegramMedia):
    voice: Union[InputFile, str]
    caption: Union[None, str, TelegramMessage] = None
    duration: Optional[int] = None


class VideoNote(TelegramMedia):
    video_note: Union[InputFile, str]
    duration: Optional[int] = None
    length: Optional[int] = None
    thumbnail: Optional[Union[InputFile, str]] = None


class PaidMedia(TelegramMedia):
    star_count: int
    media: list[InputPaidMedia]
    payload: Optional[str] = None
    caption: Union[None, str, TelegramMessage] = None
    show_caption_above_media: Optional[bool] = None


class MediaGroup(TelegramMedia):
    media: Union[
        list[InputMediaAudio],
        list[InputMediaDocument],
        list[InputMediaPhoto],
        list[InputMediaVideo],
    ]


class Location(TelegramMedia):
    latitude: float
    longitude: float
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None


class Venue(TelegramMedia):
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None


class Contact(TelegramMedia):
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None


class Poll(TelegramMedia):
    question: Union[None, str, TelegramMessage] = None
    options: list[InputPollOption]
    is_anonymous: Optional[bool] = None
    type: Optional[str] = None
    allows_multiple_answers: Optional[bool] = None
    correct_option_id: Optional[int] = None
    explanation: Union[None, str, TelegramMessage] = None
    open_period: Optional[int] = None
    close_date: Optional[int] = None
    is_closed: Optional[bool] = None


class Dice(TelegramMedia):
    emoji: Optional[str] = None


class ChatAction(TelegramMedia):
    action: str


class Sticker(TelegramMedia):
    sticker: Union[InputFile, str]
    emoji: Optional[str] = None


class Invoice(TelegramMedia):
    title: str
    description: str
    payload: str
    provider_token: Optional[str] = None
    currency: str
    prices: list[LabeledPrice]
    max_tip_amount: Optional[int] = None
    suggested_tip_amounts: Optional[list[int]] = None
    start_parameter: Optional[str] = None
    provider_data: Optional[str] = None
    photo_url: Optional[str] = None
    photo_size: Optional[int] = None
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    need_name: Optional[bool] = None
    need_phone_number: Optional[bool] = None
    need_email: Optional[bool] = None
    need_shipping_address: Optional[bool] = None
    send_phone_number_to_provider: Optional[bool] = None
    send_email_to_provider: Optional[bool] = None
    is_flexible: Optional[bool] = None


class Game(TelegramMedia):
    game_short_name: str
