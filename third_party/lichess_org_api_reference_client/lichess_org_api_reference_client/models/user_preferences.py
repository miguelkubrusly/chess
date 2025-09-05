from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_preferences_piece_set import UserPreferencesPieceSet
from ..models.user_preferences_piece_set_3d import UserPreferencesPieceSet3D
from ..models.user_preferences_sound_set import UserPreferencesSoundSet
from ..models.user_preferences_theme import UserPreferencesTheme
from ..models.user_preferences_theme_3d import UserPreferencesTheme3D
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="UserPreferences")



@_attrs_define
class UserPreferences:
    """ 
        Attributes:
            dark (Union[Unset, bool]):
            transp (Union[Unset, bool]):
            bg_img (Union[Unset, str]):
            is3d (Union[Unset, bool]):
            theme (Union[Unset, UserPreferencesTheme]):
            piece_set (Union[Unset, UserPreferencesPieceSet]):
            theme3d (Union[Unset, UserPreferencesTheme3D]):
            piece_set_3_d (Union[Unset, UserPreferencesPieceSet3D]):
            sound_set (Union[Unset, UserPreferencesSoundSet]):
            blindfold (Union[Unset, int]):
            auto_queen (Union[Unset, int]):
            auto_threefold (Union[Unset, int]):
            takeback (Union[Unset, int]):
            moretime (Union[Unset, int]):
            clock_tenths (Union[Unset, int]):
            clock_bar (Union[Unset, bool]):
            clock_sound (Union[Unset, bool]):
            premove (Union[Unset, bool]):
            animation (Union[Unset, int]):
            piece_notation (Union[Unset, int]):
            captured (Union[Unset, bool]):
            follow (Union[Unset, bool]):
            highlight (Union[Unset, bool]):
            destination (Union[Unset, bool]):
            coords (Union[Unset, int]):
            replay (Union[Unset, int]):
            challenge (Union[Unset, int]):
            message (Union[Unset, int]):
            submit_move (Union[Unset, int]):
            confirm_resign (Union[Unset, int]):
            insight_share (Union[Unset, int]):
            keyboard_move (Union[Unset, int]):
            voice_move (Union[Unset, bool]):
            zen (Union[Unset, int]):
            ratings (Union[Unset, int]):
            move_event (Union[Unset, int]):
            rook_castle (Union[Unset, int]):
     """

    dark: Union[Unset, bool] = UNSET
    transp: Union[Unset, bool] = UNSET
    bg_img: Union[Unset, str] = UNSET
    is3d: Union[Unset, bool] = UNSET
    theme: Union[Unset, UserPreferencesTheme] = UNSET
    piece_set: Union[Unset, UserPreferencesPieceSet] = UNSET
    theme3d: Union[Unset, UserPreferencesTheme3D] = UNSET
    piece_set_3_d: Union[Unset, UserPreferencesPieceSet3D] = UNSET
    sound_set: Union[Unset, UserPreferencesSoundSet] = UNSET
    blindfold: Union[Unset, int] = UNSET
    auto_queen: Union[Unset, int] = UNSET
    auto_threefold: Union[Unset, int] = UNSET
    takeback: Union[Unset, int] = UNSET
    moretime: Union[Unset, int] = UNSET
    clock_tenths: Union[Unset, int] = UNSET
    clock_bar: Union[Unset, bool] = UNSET
    clock_sound: Union[Unset, bool] = UNSET
    premove: Union[Unset, bool] = UNSET
    animation: Union[Unset, int] = UNSET
    piece_notation: Union[Unset, int] = UNSET
    captured: Union[Unset, bool] = UNSET
    follow: Union[Unset, bool] = UNSET
    highlight: Union[Unset, bool] = UNSET
    destination: Union[Unset, bool] = UNSET
    coords: Union[Unset, int] = UNSET
    replay: Union[Unset, int] = UNSET
    challenge: Union[Unset, int] = UNSET
    message: Union[Unset, int] = UNSET
    submit_move: Union[Unset, int] = UNSET
    confirm_resign: Union[Unset, int] = UNSET
    insight_share: Union[Unset, int] = UNSET
    keyboard_move: Union[Unset, int] = UNSET
    voice_move: Union[Unset, bool] = UNSET
    zen: Union[Unset, int] = UNSET
    ratings: Union[Unset, int] = UNSET
    move_event: Union[Unset, int] = UNSET
    rook_castle: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dark = self.dark

        transp = self.transp

        bg_img = self.bg_img

        is3d = self.is3d

        theme: Union[Unset, str] = UNSET
        if not isinstance(self.theme, Unset):
            theme = self.theme.value


        piece_set: Union[Unset, str] = UNSET
        if not isinstance(self.piece_set, Unset):
            piece_set = self.piece_set.value


        theme3d: Union[Unset, str] = UNSET
        if not isinstance(self.theme3d, Unset):
            theme3d = self.theme3d.value


        piece_set_3_d: Union[Unset, str] = UNSET
        if not isinstance(self.piece_set_3_d, Unset):
            piece_set_3_d = self.piece_set_3_d.value


        sound_set: Union[Unset, str] = UNSET
        if not isinstance(self.sound_set, Unset):
            sound_set = self.sound_set.value


        blindfold = self.blindfold

        auto_queen = self.auto_queen

        auto_threefold = self.auto_threefold

        takeback = self.takeback

        moretime = self.moretime

        clock_tenths = self.clock_tenths

        clock_bar = self.clock_bar

        clock_sound = self.clock_sound

        premove = self.premove

        animation = self.animation

        piece_notation = self.piece_notation

        captured = self.captured

        follow = self.follow

        highlight = self.highlight

        destination = self.destination

        coords = self.coords

        replay = self.replay

        challenge = self.challenge

        message = self.message

        submit_move = self.submit_move

        confirm_resign = self.confirm_resign

        insight_share = self.insight_share

        keyboard_move = self.keyboard_move

        voice_move = self.voice_move

        zen = self.zen

        ratings = self.ratings

        move_event = self.move_event

        rook_castle = self.rook_castle


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dark is not UNSET:
            field_dict["dark"] = dark
        if transp is not UNSET:
            field_dict["transp"] = transp
        if bg_img is not UNSET:
            field_dict["bgImg"] = bg_img
        if is3d is not UNSET:
            field_dict["is3d"] = is3d
        if theme is not UNSET:
            field_dict["theme"] = theme
        if piece_set is not UNSET:
            field_dict["pieceSet"] = piece_set
        if theme3d is not UNSET:
            field_dict["theme3d"] = theme3d
        if piece_set_3_d is not UNSET:
            field_dict["pieceSet3d"] = piece_set_3_d
        if sound_set is not UNSET:
            field_dict["soundSet"] = sound_set
        if blindfold is not UNSET:
            field_dict["blindfold"] = blindfold
        if auto_queen is not UNSET:
            field_dict["autoQueen"] = auto_queen
        if auto_threefold is not UNSET:
            field_dict["autoThreefold"] = auto_threefold
        if takeback is not UNSET:
            field_dict["takeback"] = takeback
        if moretime is not UNSET:
            field_dict["moretime"] = moretime
        if clock_tenths is not UNSET:
            field_dict["clockTenths"] = clock_tenths
        if clock_bar is not UNSET:
            field_dict["clockBar"] = clock_bar
        if clock_sound is not UNSET:
            field_dict["clockSound"] = clock_sound
        if premove is not UNSET:
            field_dict["premove"] = premove
        if animation is not UNSET:
            field_dict["animation"] = animation
        if piece_notation is not UNSET:
            field_dict["pieceNotation"] = piece_notation
        if captured is not UNSET:
            field_dict["captured"] = captured
        if follow is not UNSET:
            field_dict["follow"] = follow
        if highlight is not UNSET:
            field_dict["highlight"] = highlight
        if destination is not UNSET:
            field_dict["destination"] = destination
        if coords is not UNSET:
            field_dict["coords"] = coords
        if replay is not UNSET:
            field_dict["replay"] = replay
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if message is not UNSET:
            field_dict["message"] = message
        if submit_move is not UNSET:
            field_dict["submitMove"] = submit_move
        if confirm_resign is not UNSET:
            field_dict["confirmResign"] = confirm_resign
        if insight_share is not UNSET:
            field_dict["insightShare"] = insight_share
        if keyboard_move is not UNSET:
            field_dict["keyboardMove"] = keyboard_move
        if voice_move is not UNSET:
            field_dict["voiceMove"] = voice_move
        if zen is not UNSET:
            field_dict["zen"] = zen
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if move_event is not UNSET:
            field_dict["moveEvent"] = move_event
        if rook_castle is not UNSET:
            field_dict["rookCastle"] = rook_castle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dark = d.pop("dark", UNSET)

        transp = d.pop("transp", UNSET)

        bg_img = d.pop("bgImg", UNSET)

        is3d = d.pop("is3d", UNSET)

        _theme = d.pop("theme", UNSET)
        theme: Union[Unset, UserPreferencesTheme]
        if isinstance(_theme,  Unset):
            theme = UNSET
        else:
            theme = UserPreferencesTheme(_theme)




        _piece_set = d.pop("pieceSet", UNSET)
        piece_set: Union[Unset, UserPreferencesPieceSet]
        if isinstance(_piece_set,  Unset):
            piece_set = UNSET
        else:
            piece_set = UserPreferencesPieceSet(_piece_set)




        _theme3d = d.pop("theme3d", UNSET)
        theme3d: Union[Unset, UserPreferencesTheme3D]
        if isinstance(_theme3d,  Unset):
            theme3d = UNSET
        else:
            theme3d = UserPreferencesTheme3D(_theme3d)




        _piece_set_3_d = d.pop("pieceSet3d", UNSET)
        piece_set_3_d: Union[Unset, UserPreferencesPieceSet3D]
        if isinstance(_piece_set_3_d,  Unset):
            piece_set_3_d = UNSET
        else:
            piece_set_3_d = UserPreferencesPieceSet3D(_piece_set_3_d)




        _sound_set = d.pop("soundSet", UNSET)
        sound_set: Union[Unset, UserPreferencesSoundSet]
        if isinstance(_sound_set,  Unset):
            sound_set = UNSET
        else:
            sound_set = UserPreferencesSoundSet(_sound_set)




        blindfold = d.pop("blindfold", UNSET)

        auto_queen = d.pop("autoQueen", UNSET)

        auto_threefold = d.pop("autoThreefold", UNSET)

        takeback = d.pop("takeback", UNSET)

        moretime = d.pop("moretime", UNSET)

        clock_tenths = d.pop("clockTenths", UNSET)

        clock_bar = d.pop("clockBar", UNSET)

        clock_sound = d.pop("clockSound", UNSET)

        premove = d.pop("premove", UNSET)

        animation = d.pop("animation", UNSET)

        piece_notation = d.pop("pieceNotation", UNSET)

        captured = d.pop("captured", UNSET)

        follow = d.pop("follow", UNSET)

        highlight = d.pop("highlight", UNSET)

        destination = d.pop("destination", UNSET)

        coords = d.pop("coords", UNSET)

        replay = d.pop("replay", UNSET)

        challenge = d.pop("challenge", UNSET)

        message = d.pop("message", UNSET)

        submit_move = d.pop("submitMove", UNSET)

        confirm_resign = d.pop("confirmResign", UNSET)

        insight_share = d.pop("insightShare", UNSET)

        keyboard_move = d.pop("keyboardMove", UNSET)

        voice_move = d.pop("voiceMove", UNSET)

        zen = d.pop("zen", UNSET)

        ratings = d.pop("ratings", UNSET)

        move_event = d.pop("moveEvent", UNSET)

        rook_castle = d.pop("rookCastle", UNSET)

        user_preferences = cls(
            dark=dark,
            transp=transp,
            bg_img=bg_img,
            is3d=is3d,
            theme=theme,
            piece_set=piece_set,
            theme3d=theme3d,
            piece_set_3_d=piece_set_3_d,
            sound_set=sound_set,
            blindfold=blindfold,
            auto_queen=auto_queen,
            auto_threefold=auto_threefold,
            takeback=takeback,
            moretime=moretime,
            clock_tenths=clock_tenths,
            clock_bar=clock_bar,
            clock_sound=clock_sound,
            premove=premove,
            animation=animation,
            piece_notation=piece_notation,
            captured=captured,
            follow=follow,
            highlight=highlight,
            destination=destination,
            coords=coords,
            replay=replay,
            challenge=challenge,
            message=message,
            submit_move=submit_move,
            confirm_resign=confirm_resign,
            insight_share=insight_share,
            keyboard_move=keyboard_move,
            voice_move=voice_move,
            zen=zen,
            ratings=ratings,
            move_event=move_event,
            rook_castle=rook_castle,
        )


        user_preferences.additional_properties = d
        return user_preferences

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
