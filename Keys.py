from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Group, Key, Match, Screen
mod = "mod4"
keys = [

    #---    Switch between windows  ---#
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    #---    Move windows    ---#
    Key([mod, "control"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "control"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "control"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up()),

    #---    Resi    ze windows  ---#
    Key([mod, "shift"], "Left", lazy.layout.grow_left()),
    Key([mod, "shift"], "Right", lazy.layout.grow_right()),
    Key([mod, "shift"], "Down", lazy.layout.grow_down()),
    Key([mod, "shift"], "Up", lazy.layout.grow_up()),

    #---   open nautilus   ---#
    Key([mod], "n", lazy.spawn("nautilus")),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),

    #---    Browser     ---#
    Key([mod], "f", lazy.spawn("chromium")),

    #---    Terminal    ---#
    Key([mod], "Return", lazy.spawn("alacritty")),

    #---    Toogle layout   ---#
    Key([mod], "Tab", lazy.next_layout()),

    #---    Kill window     ---#
    Key([mod], "x", lazy.window.kill()),

    #---    Reload Qtile    ---#
    Key([mod, "shift"], "r", lazy.reload_config()),

    #---    Exit Qtile      ---#
    Key([mod, "shift"], "e", lazy.shutdown()),

    #---    Lock screen ---#
    Key([], "F1", lazy.spawn("betterlockscreen --lock blur")),
    
    #---   Transparency plus ---#
    Key([mod], "p", lazy.spawn("bash /home/marcel/pycharm/pycharm-community-2021.3.1/bin/pycharm.sh")),
    
    #---   Transparency minus --#
    Key([mod], "l", lazy.spawn("picom-trans -c -t 100")),
    
    #---   Transparency reset --#
    Key([mod, "shift"], "p", lazy.spawn("picom-trans -r")), 
    
    Key([mod], "t", lazy.spawn("thunderbird")),
    
    Key([mod], "y", lazy.spawn("firefox 'www.youtube.com'"), lazy.window.togroup("5")),

    Key([mod], "s", lazy.next_screen(), desc='Next monitor'),
    
    Key([mod], "m", lazy.spawn("mattermost-desktop")),
    Key([mod], "a", lazy.spawn("audacity")),
    Key([mod], "q", lazy.shutdown())
]
