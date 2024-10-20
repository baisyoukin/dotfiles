# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#
# import
#
import os
import subprocess
from libqtile import bar, layout, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration

#
# variables
#
mod = "mod4"
terminal = "urxvt"
launcher = "rofi -show drun"

#
# keybinds
#
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Size
    Key([mod, "control"], "j", lazy.layout.shrink(),
        desc="shrink focused window"),
    Key([mod, "control"], "k", lazy.layout.grow(),
        desc="Grow focused window"),
    Key([mod, "control"], "n", lazy.layout.reset(),
        desc="Reset all window sizes"),
    Key([mod, "shift"], "n", lazy.layout.normalize(),
        desc="Normalize all window sizes"),

    Key([mod], "q", lazy.window.kill(),
        desc="Kill focused window"),
    Key(
        [mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen",
    ),
    Key([mod], "space", lazy.window.toggle_floating(),
        desc="Toggle floating"),

    # qtile system
    Key([mod, "control"], "r", lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),

    # Apps
    Key([mod], "r", lazy.spawn(launcher),
        desc="Spawn a rofi"),
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),
    # Key([mod], "p", lazy.spawncmd(),
    #     desc="Spawn a command using a prompt widget"),
]

#
# groups
#
groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod], i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group"
            ),
            # mod + shift + group number = switch to & move focused window
            Key(
                [mod, "shift"], i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch & move focused window to group",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

#
# layouts & theme
#
layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": "F59542",
    "border_normal": "#198844"
}
layouts = [
    # layout.Columns(),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#
# bar settings
#
widget_defaults = dict(
    font="Inter Display",
    fontsize=14,
    padding=3,
    foreground='#C5C8C6',
)
extension_defaults = widget_defaults.copy()

decor_left = {
    "decorations": [
        PowerLineDecoration(
            # path="arrow_left"
            # path="rounded_left"
            path="forward_slash"
            # path="back_slash"
        )
    ]
}
decor_right = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_right"
            # path="rounded_right"
            # path="forward_slash"
            # path="back_slash"
        )
    ]
}
widget_list = [
    widget.TextBox(
        text='',
        background='#1D1F21',
        foreground='#1793D1',
        fontsize=16,
        padding=10,
    ),
    widget.GroupBox(
        **decor_left,
        background='#1D1f21',
        disable_drag='True',
        margin_y=4,
        padding=2,
        highlight_method='line',
        highlight_color='#1D1f21',
        this_current_screen_border='#1793D1',
        borderwidth=2,
        active='#C5C8C6',
        inactive='#707880',
    ),
    widget.WindowName(
        **decor_right,
        background='#85678f',
        foreground='#000000',
    ),
    widget.Load(
        **decor_right,
        format=' {time} Uptime',
        background='#cc6666',
        foreground='#000000',
    ),
    widget.NvidiaSensors(
        **decor_right,
        format=' {temp}°C',
        background='#DE935F',
        foreground='#000000',
    ),
    widget.Clock(
        **decor_right,
        format="  %H:%M:%S",
        background='#f0c674',
        foreground='#000000',
    ),
    widget.Systray(),
]

screens = [
    Screen(
        top=bar.Bar(
            widget_list,
            28,
            background='#1D1F21',
            opacity=1,
        ),
        wallpaper='~/Wallpapers/kde.png',
        wallpaper_mode='fill',
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
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
# NOTE: I play minecraft with fpsreducer mod, so i dont need that
auto_minimize = False

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/xrandr.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
