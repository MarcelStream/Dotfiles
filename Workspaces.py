from libqtile.config import Click, Drag, Group, Key, Match, Screen

groups= [
    Group("1",
          label="",
          # spawn='vivaldi',
          matches=[Match(wm_class=["Vivaldi-stable"]),
                   Match(wm_class=["Icecat"]),
                   Match(wm_class=["Brave-browser"]),
                   Match(wm_class=["chromium"]),
                   ],
          ),

    Group("2",
          label="",
          matches=[Match(wm_class=["gedit"]),
                   Match(wm_class=["jetbrains-pycharm-ce"])
                   ],
          ),

    Group("3",
          label="",
          matches=[Match(wm_class=["pcmanfm"]),
                   Match(wm_class=["Org.gnome.Nautilus"]),
                   Match(wm_class=["qBittorrent"]),
                   ],
          ),
    Group("4",
                  label="🎵",
                            matches=[Match(wm_class=["audacity"])]
                                      ),
    Group("5",
                  label="",

    ),
    Group("6",
                  label="",
                                      ),
    Group("7",
                  label="",
                                      ),
    Group("8",
                  label="",
                                      ),
    Group("9",
                      label="",
                      matches=[Match(wm_class=["Mattermost"])]
    ),
    Group("10",
          label="✉",
          matches=[Match(wm_class=["Thunderbird"])]),
    Group("11",
                              label="",
                                                                                                ),
    Group("12",
                              label="",
                                                                                                ),
    Group("13",
                              label="",
                                                                                                ),
    Group("14",
                              label="",
                                                                                                ),
    Group("15",
                              label="",
                                                                                                ),
    Group("16",
                              label="",
                                                                                                ),
]
