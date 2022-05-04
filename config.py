#  $$$$$$\    $$\     $$\ $$\
# $$  __$$\   $$ |    \__|$$ |
# $$ /  $$ |$$$$$$\   $$\ $$ | $$$$$$\
# $$ |  $$ |\_$$  _|  $$ |$$ |$$  __$$\
# $$ |  $$ |  $$ |    $$ |$$ |$$$$$$$$ |
# $$ $$\$$ |  $$ |$$\ $$ |$$ |$$   ____|
# \$$$$$$ /   \$$$$  |$$ |$$ |\$$$$$$$\
#  \___$$$\    \____/ \__|\__| \_______|
#      \___|
#
# https://github.com/jorgeloopzz/dotfiles

import os
import sys
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.bar import Bar
from qtile_extras.widget import ALSAWidget
from libqtile import hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger
from qtile_extras.popup.toolkit import *
import time
import json
import glob
from Keys import keys, mod
from Workspaces import groups


#-----------#
# FUNCTIONS #
#-----------#

def test_function(qtile):
    logger.warning("In the test function")
    test = PopupGridLayout(qtile, rows=6, cols=6, controls=[
        PopupText(text='ASDAS',row=1,col_span=6),
        PopupText(text='ASDAS',row=2,col_span=6),
        PopupText(text='ASDAS',row=3,col_span=6),
        PopupText(text='ASDAS',row=4,col_span=6),
        PopupText(text='ASDAS',row=5,col_span=6),
    ])
    test.show(centered=True)
wallpapers=[
    '/home/marcel/Pictures/wallpaper_turkise.jpg',
    '/home/marcel/Pictures/anime_red.jpg',
    '/home/marcel/Pictures/Green_Wallpaper.jpg',
    '/home/marcel/Pictures/efeu_wallpaper.jpg'
]
current_wallpaper=0

@lazy.function
def wallpaper_switch(qtile):
    global wallpapers
    global current_wallpaper
    global screens
    logger.warning("CALLED!")
    wp_name = wallpapers[current_wallpaper]
    qtile.cmd_spawn(f"wal -i {wp_name} -s -t")
    time.sleep(0.5)
    current_wallpaper += 1
    if current_wallpaper >= len(wallpapers):
        current_wallpaper = 0
    screens[0].cmd_set_wallpaper(wp_name)
    screens[1].cmd_set_wallpaper(wp_name)
    wp_name = wp_name.replace("/","_")
    wp_name = wp_name.replace(".","_")
    for f_name in glob.glob("/home/marcel/.cache/wal/schemes/*.json"):
        only_fname = f_name.split("/")[-1]
        logger.warning(only_fname)
        logger.warning(wp_name)
        if only_fname.startswith(wp_name):
            f = open(f_name, "r")
            data = json.load(f)
            colors = data["colors"]
            color_list = [colors[key] for key in colors]
            logger.warning(str(color_list))
            add_color(color_list)
            break
           
    
def add_spacer_sep(f_c, b_c, orientation, widget_list):
    spacer_added = 0
    if orientation == 'left':
        i=0
        while i < 100:
            i = i+5
            spacer_added += 1
            widget_list.append(widget.Sep(size_percent=i, padding=0, background=b_c, foreground=f_c))
    elif orientation == 'right':
        i=100
        while i > 0:
            widget_list.append(widget.Sep(size_percent=i, padding=0, background=b_c, foreground=f_c))
            i = i - 5
            spacer_added += 1
    return widget_list, spacer_added
    
def add_color(colours):
    global widget_list0, widget_list1, btn_wdg0, btn_wdg1
    global bar0, bar1, btn_bar0, btn_bar1
    # it seems that very dark colours like black are at the beginning of the list, it is more robust to
    # start from the end
    #colours.reverse()
    
    dark_background = colours[0]
    light_text = colours[-1]
    foreground_color_widgets = [2, 12, 14, 15, 16]
    foreground_light_widgets = [1,3,4,5,6, 13]
    spacer_widgets=[8,9,10]
    ending_widgets = [7, 11]
    
    btn_colour = [0, 4, 5, 6]
    btn_foreground = [1]
    btn_foreground_light = [2, 3]
    btn_spacer = [7]
    

    widget_list0[0].active=colours[1]
    widget_list0[0].highlight_color=colours[2]
    widget_list0[0].this_current_screen_border=colours[2]
    widget_list0[0].other_current_screen_border=colours[2]
    widget_list0[0].inactive=light_text
    widget_list1[0].active=colours[1]
    widget_list1[0].highlight_color=colours[2]
    widget_list1[0].this_current_screen_border=colours[2]
    widget_list1[0].other_current_screen_border=colours[2]
    widget_list1[0].inactive=light_text
    
    last_colour = 1
    for wdg_index in range(17):
        if wdg_index in foreground_color_widgets:
            widget_list0[wdg_index].foreground = colours[last_colour]
            widget_list1[wdg_index].foreground = colours[last_colour]
            last_colour += 1
            if last_colour >= len(colours)-1:
                last_colour = 1
        elif wdg_index in foreground_light_widgets:
            widget_list0[wdg_index].foreground = light_text
            widget_list1[wdg_index].foreground = light_text
        
        if wdg_index not in spacer_widgets and wdg_index not in ending_widgets:
            widget_list0[wdg_index].background = dark_background
            widget_list1[wdg_index].background = dark_background
        if wdg_index in ending_widgets:
            widget_list0[wdg_index].foreground=dark_background
            widget_list0[wdg_index].background="#00000000"
            widget_list1[wdg_index].foreground=dark_background
            widget_list1[wdg_index].background="#00000000"
            
    last_colour = 3
    for wdg_index in range(10):
        if wdg_index in btn_colour:
            btn_wdg0[wdg_index].background = colours[2]
            btn_wdg0[wdg_index].foreground = dark_background
            btn_wdg1[wdg_index].background = colours[2]
            btn_wdg1[wdg_index].foreground = dark_background
        else:
            btn_wdg0[wdg_index].background = dark_background
            btn_wdg1[wdg_index].background = dark_background
        
        if wdg_index in btn_foreground:
            btn_wdg0[wdg_index].foreground = colours[2]
            btn_wdg1[wdg_index].foreground = colours[2]         
        elif wdg_index in btn_foreground_light:
            btn_wdg0[wdg_index].foreground = light_text
            btn_wdg1[wdg_index].foreground = light_text
        elif wdg_index not in btn_spacer and wdg_index not in btn_colour:
            btn_wdg0[wdg_index].foreground = colours[last_colour]
            btn_wdg1[wdg_index].foreground = colours[last_colour]
            last_colour += 1
            if last_colour >= len(colours)-1:
                last_colour = 3
    bar0.background="#00000000"
    bar0.foreground="#00000000"
    bar1.background="#00000000"
    bar1.foreground="#00000000"
    btn_bar0.background = "#00000000"
    btn_bar0.foreground = "#00000000"
    btn_bar1.background = "#00000000"
    btn_bar1.foreground = "#00000000"
    #bar0.background=dark_background
    #bar1.background=dark_background
    bar0.draw()
    bar1.draw()
    btn_bar0.draw()
    btn_bar1.draw()
  
def grab_cava():
    cava_file = open("/tmp/cava_output.txt", "r", encoding='utf-8', errors='ignore')
    line = cava_file.readlines()
    if len(line) > 0:
        line = line[-1]
    else:
        line=''
    cava_file.close()
    return line

#---------------#
#   SUPER KEY   #
#---------------#

#---------------#
#   KEYBINDINGS #
#---------------#

#---------------#
#   WORKSPACES  #
#---------------#


#---------------------------#
#   WINDOW STYLE IN LAYOUTS #
#---------------------------#

layouts = [
    layout.Columns(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=30),
    layout.Max(),
    # layout.Matrix(),
]

#-----#
# BAR #
#-----#

#own
colours =  [
    ["#00000000"],      # Colour 0
    ["#2e3440"],        # Colour 1
    ["#226bc9"],        # Colour 2
    ["#c3e88d"],        # Colour 3
    ["#37a6a2"],        # Colour 4
    ["#07aaeb"],        # Colour 5
    ["#456eb5"],        # Colour 6
    ["#6a44c2"],        # Colour 7
    ["#F2779C"],        # Colour 8
    ["#4e86a6"],        # Colour 9
    ["#ff6e6e"]]        # Colour 10


widget_defaults = dict(
    font="monospace",
    fontsize=18,
    padding=6,
)
extension_defaults = widget_defaults.copy()

xx=15
xf="ubuntumono nerd font bold"
widget_list0 = []
widget_list1 = []

# -------------GROUP BOX------------------
widget_list0.append(
    widget.GroupBox( #0
		font=xf,
		fontsize=xx,
		background=colours[1],
		margin_y=4,
		margin_x=5,
		padding_y=3,
		padding_x=2,
		border_width=8,
		inactive="#ffffff",
		active=colours[2],
		rounded=False,
		highlight_color=colours[4],
		highlight_method="block",
		this_current_screen_border=colours[4],
		block_highlight_text_color=colours[1],
		visible_groups=[str(x) for x in range(1,9)],
    ),
)
widget_list1.append(
    widget.GroupBox(
		font=xf,
		fontsize=xx,
		background=colours[1],
		margin_y=4,
		margin_x=5,
		padding_y=3,
		padding_x=2,
		border_width=8,
		inactive=colours[9],
		active=colours[2],
		rounded=True,
		highlight_color=colours[4],
		highlight_method="block",
		this_current_screen_border=colours[4],
		block_highlight_text_color=colours[1],
		visible_groups=[str(x) for x in range(9,17)],
    ),
)

# -------------CLOCK---------------------------
widget_list0.extend([
    widget.TextBox(text='⟍', fontsize=100, padding=-10, width=40), #1
    widget.TextBox(text="", foreground=colours[9], fontsize=xx), #2
	widget.Clock( #3
        format="%H:%M",
        update_interval=60.0,
        foreground="#ffffff",
        background=colours[1],
        padding=0,
        fontsize=xx
    ),
])
widget_list1.extend([
    widget.TextBox(text='⟍', fontsize=100, padding=-10, width=40), 
    widget.TextBox(text="", foreground=colours[9], fontsize=xx),
	widget.Clock(
        format="%H:%M",
        update_interval=60.0,
        foreground="#ffffff",
        background=colours[1],
        padding=0,
        fontsize=xx
    ),
])

# ------------------THEME SWITCHER-------------------
widget_list0.extend([
    #widget.Sep(foreground="#ffffff", linewidth=8, size_percent=100, padding=10), #4
    widget.TextBox(text='⟍', fontsize=120, padding=-10, width=50), 
    widget.TextBox(text="", foreground="#ffffff", padding=0, #5
        mouse_callbacks={
            'Button1': wallpaper_switch
        }
    ),
     widget.CurrentLayoutIcon( #6
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.4,
        background=colours[1],
        padding=0
    ),
    widget.TextBox(text="◤", foreground=colours[1], fontsize=100, padding=-35), #7
    widget.Spacer(), #8
    widget.Spacer(), #9
    widget.Spacer(length=400) #10
])
widget_list1.extend([
    widget.TextBox(text='⟍', fontsize=120, padding=-10, width=50), 
    widget.TextBox(text="", foreground="#ffffff", padding=0,
        mouse_callbacks={
            'Button1': wallpaper_switch
        }
    ),
     widget.CurrentLayoutIcon( #2
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.4,
        background=colours[1],
        padding=0
    ),
    widget.TextBox(text="◤", foreground=colours[1], fontsize=100, padding=-35),
    widget.Spacer(),
    widget.Spacer(),
    widget.Spacer(length=400)
])

# --------------WINDOW NAME------------------------
widget_list0.extend([
    widget.TextBox(text="◥", foreground=colours[1], fontsize=100, padding=-35), #11
    widget.WindowName(background=colours[1],foreground=colours[2], maxchars=20, fmt='{:^40}', padding=0, empty_group_string='Window Name'), #12
    widget.TextBox(text="⟋", background=colours[1], foreground="#FFFFFF", fontsize=120, padding=-15) #13
])
widget_list1.extend([
    widget.TextBox(text="◥", foreground=colours[1], fontsize=100, padding=-35),
    widget.WindowName(background=colours[1],foreground=colours[2], maxchars=20, fmt='{:^40}', padding=0, empty_group_string='Window Name'),
    widget.TextBox(text="⟋", background=colours[1], foreground="#FFFFFF", fontsize=120, padding=-15)
])
    
# --------------CALENDAR------------------------------
widget_list0.append(
    widget.Clock( #14
        format=" %d %b, %a",
        mouse_callbacks = {
            'Button1': lazy.spawn('gsimplecal')
        },
        foreground=colours[4],
        background=colours[1],
        fontsize=xx
    )
)
widget_list1.append(
    widget.Clock(
        format=" %d %b, %a",
        mouse_callbacks = {
            'Button1': lazy.spawn('gsimplecal')
        },
        foreground=colours[4],
        background=colours[1],
        fontsize=xx
    )
)

# -----------------VOLUME--------------------------
widget_list0.append(
    widget.Volume( #15
        mouse_callbacks={'Button1': lazy.spawn('pavucontrol')},
        update_interval=0.001,
        fmt="{}",
        foreground=colours[7],
        background=colours[1],
        fontsize=xx
    )
)
widget_list1.append(
    widget.Volume(
        mouse_callbacks={'Button1': lazy.spawn('pavucontrol')},
        update_interval=0.001,
        fmt="{}",
        foreground=colours[7],
        background=colours[1],
        fontsize=xx
    )
)
# --------------POWER DOWN-------------------------
widget_list0.append( #16
    widget.TextBox(text="", foreground="#FFFFFF", fontsize=xx)
)
widget_list1.append(
    widget.TextBox(text="", foreground="#FFFFFF", fontsize=xx)
)

# --------------EMAIL CHECK------------------------
'''
widget_list0.append(
    widget.GenPollText( #16
        name = 'checkmails',
        func = lambda: subprocess.check_output(
            '/home/marcel/.config/qtile/checkmails.sh',
        ).decode('utf-8'),
        # 1800 sec equals to 30 min
        update_interval = 1800,
        max_chars = 3,
        fmt = ' {}',
        mouse_callbacks = {
            'Button1': lazy.widget['checkmails'].eval('self.update(self.poll())'),
        },
        foreground=colours[6],
        background=colours[1],
    )
)
widget_list1.append(
    widget.GenPollText(
        name = 'checkmails',
        func = lambda: subprocess.check_output(
            '/home/marcel/.config/qtile/checkmails.sh',
        ).decode('utf-8'),
        # 1800 sec equals to 30 min
        update_interval = 1800,
        max_chars = 3,
        fmt = ' {}',
        mouse_callbacks = {
            'Button1': lazy.widget['checkmails'].eval('self.update(self.poll())'),
        },
        foreground=colours[6],
        background=colours[1],
    )
)
'''
# ------------------BOTTOM BAR WIDGETS----------------
cava_wdg = widget.GenPollText(update_interval=0.01, func=grab_cava)
artist_wdg = widget.GenPollText(update_interval=10, fontsize=xx, func=lambda: subprocess.check_output(['spotify-now', '-i', '"%artist - %title"', '-e', '"Not playing"', '-p', '"Not playing"']).strip().decode('utf-8').strip('"'))
mail_wdg = widget.GenPollText(
        name = 'checkmails',
        func = lambda: subprocess.check_output(
            '/home/marcel/.config/qtile/checkmails.sh',
        ).decode('utf-8'),
        # 1800 sec equals to 30 min
        update_interval = 1800,
        max_chars = 3,
        fmt = ' {}',
        mouse_callbacks = {
            'Button1': lazy.widget['checkmails'].eval('self.update(self.poll())'),
        },
        foreground=colours[6],
        background=colours[1],
)
weather_wdg = widget.OpenWeather(
    location='Vienna',
    format='{location_city}: {main_temp} °{units_temperature} {icon}',
    fontsize=xx
)
btn_wdg0 = [
    widget.TextBox(text="🔍", fontsize=xx, mouse_callbacks={'Button1':lazy.spawn('rofi -show run')}), #0
    widget.TextBox(text="", fontsize=xx), #1
    cava_wdg, #2
    artist_wdg, #3
    widget.TextBox(text="⏮", fontsize=xx), #4
    widget.TextBox(text="⏸", fontsize=xx), #5
    widget.TextBox(text="⏭", fontsize=xx), #6
    widget.Spacer(), #7
    weather_wdg, #8
    mail_wdg, #9
]
btn_wdg1 = [
    widget.TextBox(text="🔍", fontsize=xx),
    widget.TextBox(text="", fontsize=xx),
    cava_wdg,
    artist_wdg,
    widget.TextBox(text="⏮", fontsize=xx), #4
    widget.TextBox(text="⏸", fontsize=xx), #5
    widget.TextBox(text="⏭", fontsize=xx), #6
    widget.Spacer(), #7
    weather_wdg, #8
    mail_wdg, #9
]
# ------------------BARS-------------------------------
bar0=bar.Bar(
    widget_list0,
    30,
    background="#00000000",
    foreground="#00000000",
    opacity=0.9,
    border_width=0,
)
btn_bar0=bar.Bar(
    btn_wdg0,
    30,
    background="#00000000",
    foreground="#00000000",
    opacity=0.9,
    border_width=0,
)
bar1=bar.Bar(
    widget_list1,
    30,
    background="#00000000",
    foreground="#00000000",
    opacity=0.9,
    border_width=0,
)
btn_bar1=bar.Bar(
    btn_wdg1,
    30,
    background="#00000000",
    foreground="#00000000",
    opacity=0.9,
    border_width=0,
)
screens = [
    Screen(
        top=bar0,
        bottom=btn_bar0,
        wallpaper='/home/marcel/Pictures/wallpaper_turkise.jpg',
        wallpaper_mode='stretch'
    ),
    Screen(
        top=bar1,
        bottom=btn_bar1,
        wallpaper='/home/marcel/Pictures/wallpaper_turkise.jpg',
        wallpaper_mode='stretch'
    )
]


#--------------#
# Group Hotkey #
#--------------#


for i in groups:
    int_i = int(i.name)
    if int_i <= 8:
        keys.extend([
            # Switch to workspace N        
            Key([mod], i.name, lazy.group[i.name].toscreen(0)),
            # Send window to workspace N
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ])
    else:
        keys.extend([
            Key([mod, "control"], str(int_i-8), lazy.group[i.name].toscreen(1)),
            Key([mod, "shift", "control"], str(int_i-8), lazy.window.togroup(i.name))
        ])

#-----------------------#
#   FLOATING WINDOWS    #
#-----------------------#

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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
    ],
    border_focus="#9ccfd8",
    border_normal="#31748f"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

#---------------#
#   AUTOSTART   #
#---------------#

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

    
@hook.subscribe.client_new
def slight_delay(window):
    time.sleep(0.01)
    

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
