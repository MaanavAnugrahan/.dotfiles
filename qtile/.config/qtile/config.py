import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, hook
from libqtile.config import DropDown, Click, Drag, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy

from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.windowname import WindowName
from libqtile.widget.textbox import TextBox 
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.volume import Volume
from libqtile.widget.systray import Systray
from libqtile.widget.battery import Battery
from libqtile.widget.clock import Clock
from libqtile.widget.sep import Sep
from libqtile.widget.spacer import Spacer

from qtile_extras import widget


mod = "mod4"
mod1 = "alt"
mod2 = "control"
terminal = "kitty"

def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")

keys = [
    Key([mod, "shift"], "n", lazy.spawn("obsidian"),),
    Key([mod,], "i", lazy.spawn("nitrogen"),),
    Key([mod], "w", lazy.spawn("brave"),),
    Key([mod, "shift"], "m", lazy.spawn("/home/maanav/Rofi-Beats/rofi-beats"),),
    Key([mod, "shift"], "Return", lazy.spawn("/home/maanav/.config/rofi/launchers/ribbon/launcher.sh"),),
    Key([mod, "shift"], "p", lazy.spawn("/home/maanav/.config/rofi/powermenu/powermenu.sh"),),
     Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill(),),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = []

group_names = ["1", "2", "3", "4", "5", "6", ]
group_labels = ["", "", "ﴬ", "", "", "", ]
# group_labels = ["", "", "", "", "", "", ]
group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

def init_layout_theme():
    return {"margin":9,
            "border_width":3,
            "border_focus": "#F2CDCD",
            "border_normal": "#C3BAC6",
            "border_normal_stack": "#F2CDCD",
            "border_focus_stack": "#C3BAC6",
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=10, border_width=3, border_focus="#F2CDCD", border_normal="#C3BAC6"),
    layout.MonadWide(margin=10, border_width=3, border_focus="#F2CDCD", border_normal="#C3BAC6"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

widget_defaults = dict(
    # font='Iosevka Term',
    font='Iosevka Term',
    fontsize=9,
    padding=3,
)

extension_defaults = widget_defaults.copy()

#Theme name : ArcoLinux Default
def init_colors():
    return [["#302D41", "#302D41"], # color 0
            ["#1A1826", "#1A1826"], # color 1
            ["#1E1E2E", "#1E1E2E"], # color 2
            ["#C3BAC6", "#C3BAC6"], # color 3
            ["#2aa198", "#2aa198"], # color 4
            ["#DDB6F2", "#DDB6F2"], # color 5
            ["#F28FAD", "#F28FAD"], # color 6
            ["#ABE9B3", "#ABE9B3"], # color 7
            ["#89DCEB", "#89DCEB"], # color 8
            ["#F2CDCD", "#F2CDCD"], # color 9
            ["#F8BD96", "#F8BD96"], # color 10
            ["#B5E8E0", "#B5E8E0"]] # color 11


colors = init_colors()



screens = [
    Screen(
        top=bar.Bar(
            [
                 widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[0],
                    background=colors[1],
                    padding=-10,
                    scale=0.30,
                ),
                GroupBox(
                    font="Font Awesome 6 Free",
                    disable_drag=True,
                    active=colors[9],
                    inactive=colors[0],
                    highlight_method='block',
                    rounded=True,
                    foreground=colors[0],
                    fontsize=12,
                    background=colors[1],
                    block_highlight_text_color=colors[1],
                    this_current_screen_border=colors[9],
                    borderwidth=4,
                    padding=5,
                    ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[1],
                    background=colors[1],
                    padding=10,
                    size_percent=50,
                        ),
                TextBox(
                        text="墳",
                        fontsize=19,
                        font="Font Awesome 6 Free",
                        foreground=colors[9],
                        background=colors[1],),
               Volume(
                    foreground=colors[9],
                   background=colors[1],
                   ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[1],
                    background=colors[1],
                    padding=10,
                    size_percent=50,
                        ),
                TextBox(
                        text="",
                        fontsize=13,
                        font="Font Awesome 6 Free",
                        foreground=colors[8],
                        background=colors[1],),
                CPU(
                    format='{load_percent}%',
                    foreground=colors[8],
                    background=colors[1],
                    ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[1],
                    background=colors[1],
                    padding=10,
                    size_percent=50,
                        ),
                TextBox(
                        text="",
                        fontsize=12,
                        font="Font Awesome 6 Free",
                        foreground=colors[6],
                        background=colors[1],),
                widget.ThermalSensor(
                        threshold=90,
                        background=colors[1],
                        foreground=colors[6],
                        ),
                widget.Spacer(),
                widget.TextBox(
                        text="类",
                    font="Font Awesome 6",
                        fontsize=16,
                        foreground=colors[3],
                        ),
               widget.WindowName(
                   fmt="{}",
				    foreground=colors[3],
				    background=colors[1],
                    width=bar.CALCULATED,
                    empty_group_string="Desktop",
                    max_chars=130,
                    mouse_callbacks={"Button2": kill_window},
				),
               widget.Spacer(background=colors[1]),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[1],
                    background=colors[1],
                    padding=10,
                    size_percent=50,
                        ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6",
                    fontsize=12,
                    foreground=colors[10],  # fontsize=38
                    background=colors[1],
                ),
                Clock(
                    foreground=colors[10],
                    background=colors[1],
                    format='%a, %b %d'
                    ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[1],
                    background=colors[1],
                    padding=10,
                    size_percent=50,
                        ),
                 widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free",
                    fontsize=12,
                    foreground=colors[11],  # fontsize=38
                    background=colors[1],
                ),
                Clock(
                    foreground=colors[11],
                    background=colors[1],
                    format='%I:%M %p'
                    ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[1],
                    background=colors[1],
                    padding=10,
                    size_percent=50,
                        ),
                TextBox(
                        text="",
                        fontsize=12,
                        font="Font Awesome 6 Free",
                        foreground=colors[7],
                        background=colors[1],),
                Battery(
                        background=colors[1],
                        foreground=colors[7],
                        format='{percent:2.0%}'
                    ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[1],
                    background=colors[1],
                    padding=10,
                    size_percent=50,
                ),
                Systray(
                    padding=2,
                    background=colors[1],
                ),
            ],
            40,
            margin=[0, 0, 21, 0],
            background=colors[1],
            border_width=[0, 0, 3, 0],
            border_color=colors[1],
        ),
        bottom=bar.Gap(18),
        left=bar.Gap(18),
        right=bar.Gap(18),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
        float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        # Match(wm_class="pavucontrol"),
        Match(wm_class="zoom"),
        Match(wm_class="bitwarden"),
        Match(wm_class="kdenlive"),
    ])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'kitty', width=0.4, height=0.5, x=0.3, y=0.1, opacity=1),
    DropDown('update', 'kitty sudo pacman -Syu', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('pomo', 'pomotroid', x=0.4, y=0.2, opacity=1),
    DropDown('nnn', 'kitty nnn',
             width=0.4, height=0.8, x=0.3, y=0.1, opacity=1),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('update')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('pomo')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('nnn')),
])

