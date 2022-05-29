# Imports
import os
import subprocess
from typing import List  # noqa: F401
import psutil
from libqtile.config import (
    Key,
    Screen,
    Group,
    Drag,
    Click,
    ScratchPad,
    DropDown,
    Match,
)
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration

# Variables
mod = "mod4"
terminal = "kitty"

keys = [
    # The essential hotkeys
      Key(
        [mod],
        "z",
        lazy.spawn("zathura"),
        desc="Zathura -a pdf viewer",
    ),
      Key(
        [mod],
        "x",
        lazy.spawn("archlinux-logout"),
        desc="Logout menu",
    ),
      Key(
        [mod],
        "e",
        lazy.spawn("/home/maanav/.config/rofi/launchers/ribbon/launcher.sh"),
        desc="Rofi app launcher",
    ),
      Key(
        [mod],
        "w",
        lazy.spawn("brave"),
        desc="Brave - the web browser",
    ),
      Key(
        [mod],
        "i",
        lazy.spawn("nitrogen"),
        desc="Rofi app launcher",
    ),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

workspaces = [
    {"name": "", "key": "1", "matches": [Match(wm_class="firefox")], "lay": "bsp"},
    {
        "name": "",
        "key": "2",
        "matches": [
            Match(wm_class="geary"),
            Match(wm_class="ptask"),
            Match(wm_class="io.elementary.calendar"),
        ],
        "lay": "bsp",
    },
    {"name": "", "key": "3", "matches": [], "lay": "bsp"},
    {"name": "", "key": "4", "matches": [Match(wm_class="emacs")], "lay": "bsp"},
    {
        "name": "",
        "key": "5",
        "matches": [
            Match(wm_class="joplin"),
            Match(wm_class="zathura"),
            Match(wm_class="libreoffice"),
            Match(wm_class="evince"),
        ],
        "lay": "columns",
    },
    {
        "name": "",
        "key": "6",
        "matches": [
            Match(wm_class="slack"),
            Match(wm_class="discord"),
            Match(wm_class="srain"),
        ],
        "lay": "bsp",
    },
    {
        "name": "",
        "key": "7",
        "matches": [Match(wm_class="lollypop")],
        "lay": "bsp",
    },
    {"name": "", "key": "8", "matches": [Match(wm_class="Steam")], "lay": "bsp"},
    {
        "name": "",
        "key": "9",
        "matches": [Match(wm_class="Thunar")],
        "lay": "bsp",
    },
    {
        "name": "",
        "key": "0",
        "matches": [
            Match(wm_class="lxappearance"),
            Match(wm_class="pavucontrol"),
        ],
        "lay": "floating",
    },
]

groups = [
    ScratchPad(
        "scratchpad",
        [
            # define a drop down terminal.
            DropDown(
                "term",
                "alacritty --class dropdown -e tmux new -As Dropdown",
                height=0.6,
                on_focus_lost_hide=False,
                opacity=1,
                warp_pointer=False,
            ),
        ],
    ),
]
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=workspace["lay"]))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=True),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another group",
        )
    )

colors = [
    ["#282828", "#282828"],  # 0 background
    ["#ebdbb2", "#ebdbb2"],  # 1 foreground
    ["#3c3826", "#3c2826"],  # 2 background lighter
    ["#cc241d", "#cc241d"],  # 3 red
    ["#98971a", "#98971a"],  # 4 green
    ["#d79921", "#d79921"],  # 5 yellow
    ["#83a598", "#83a598"],  # 6 blue
    ["#b16286", "#b16286"],  # 7 magenta
    ["#B5E8E0", "#B5E8E0"],  # 8 cyan
    ["#D9E0EE", "#D9E0EE"],  # 9 white
    ["#6E6C7E", "#6E6C7E"],  # 10 grey
    ["#d65d0e", "#d65d0e"],  # 11 orange
    ["#689d6a", "#689d6a"],  # 12 super cyan
    ["#458588", "#458588"],  # 13 super blue
    ["#1A1826", "#1A1826"],  # 14 super dark background
]

group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[1],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[7],
    "highlight_method": "block",
    "this_current_screen_border": colors[0],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[0],
    "other_screen_border": colors[0],
    "foreground": colors[1],
    "urgent_border": colors[3],
}

                                         # Layouts
layout_theme = {
    "border_width": 3,
    "margin": 14,
    "border_focus": "#b16286",
    "border_normal": "#282828",
    "font": "Humrit Nerd Font",
    "grow_amount": 2,
}

layouts = [
    # layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme, fair=False, border_on_single=True),
    layout.Columns(
        **layout_theme,
        border_on_single=True,
        num_columns=2,
        border_focus_stack="#3b4252",
        border_normal_stack="#3b4252",
        split=False,
        wrap_focus_columns=True,
        wrap_focus_rows=True,
        wrap_focus_stacks=True,
    ),
    # Plasma(**layout_theme, border_normal_fixed='#3b4252', border_focus_fixed='#3b4252', border_width_single=3),
     layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
     layout.Matrix(**layout_theme, columns=3),
    # layout.Zoomy(**layout_theme),
    # layout.Slice(**layout_theme, width=1920, fallback=layout.TreeTab(), match=Match(wm_class="joplin"), side="right"),
     layout.MonadTall(**layout_theme),
     layout.Max(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    layout.Floating(**layout_theme),
]


widget_defaults = dict(
    font="Hurmit Nerd Font",
    fontsize=8,
    padding=3,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
       top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.5,
                    padding=-10,
                    foreground=colors[7]),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Free",
                    fontsize=10,
                    **group_box_settings,
                    ),
                widget.Sep(
                    linewidth=2,
                    foreground=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                        text=" ",
                        foreground=colors[1],
                       font="Font Awesome 6 Free",
                       fontsize=12,
                         ),
                widget.WindowName(
                    foreground=colors[1],
                    empty_group_string="Desktop",
                    ),
                widget.Systray(),
                widget.Sep(
                    linewidth=2,
                    foreground=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[7],
                    font="Font Awesome 6 Free",
                    fontsize=16,
                    ),
                widget.Memory(
                        foreground=colors[7],
                        ),
                widget.Sep(
                    linewidth=2,
                    foreground=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[3],
                    fontsize=12,
                ),
                widget.ThermalSensor(
                        foreground=colors[3],
                        ),
                widget.Sep(
                    linewidth=2,
                    foreground=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[5],  # fontsize=38
                    fontsize=12,
                ),
                widget.Clock(
                    format="%a, %b %d",
                    foreground=colors[5],
                ),
                widget.Sep(
                    linewidth=2,
                    foreground=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[12],  # fontsize=38
                    fontsize=12,
                ),
                widget.Clock(
                        format="%I:%M %p",
                        foreground=colors[12],
                        ),
                widget.Sep(
                    linewidth=2,
                    foreground=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free",
                    fontsize=12,
                    foreground=colors[4],
                    ),
                widget.Battery(
                    foreground=colors[4],
                    format="{percent:2.0%}",
                    ),
                widget.Sep(
                    linewidth=2,
                    foreground=colors[0],
                    padding=10,
                    size_percent=50,
                )
            ],
            40,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Autostart script
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
