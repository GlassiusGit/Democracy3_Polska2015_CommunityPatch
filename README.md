# Democracy3_Polska2015_CommunityPatch
Patch for Democracy 3 mod named "Polska 2015: Dobra zmiana". Original by CD Project

## Introduction
[Polska 2015: Dobra zmiana mod location](https://steamcommunity.com/sharedfiles/filedetails/?id=674367345). Mod version 1.01 has some problems I decided to fix. Also, I wanted to learn Git. This is my first Git project!

## Installation and deletion
It seems many people have problem with that, so this must be the first thing about fixing.
### Installation
1. Subscribe mod in Steam
2. Enable mod ingame. **NOTE: I did not find a way to make all simulation files mod exclusive. You may gain Łiczer event while playing France, for example.**
### Uninstall
1. Disable mod ingame.
2. Unsubscribe in Steam.
### In case of crashes
1. Do the same steps like for Uninstall.
2. Remove \steamapps\common\Democracy 3\data\mods\Polska2015.txt
3. Remove \steamapps\common\Democracy 3\Polska2015
4. Remove \Documents\My Games\democracy3\mod_status.ini
5. Remove \Documents\My Games\democracy3\mod_dates.ini
6. Run Democracy 3 with Steam overlay (it restores two above ini files).

## Wrong diactrics
Original author of Democracy 3, cliffski, [introduced Unicode support](https://www.positech.co.uk/cliffsblog/2017/09/18/the-democracy-3-unicode-post-oh-yes/). However, Polish version of the game still uses some peculiar encoding. This encoding is unknown to [other Polish encodings](https://pl.wikipedia.org/wiki/Kodowanie_polskich_znak%C3%B3w). It codes Polish diactric signs using one byte, beyond ASCII coding. It causes multiple Polish words to be wrongly interpreted. In the branch investigate_diactrics I've made a research to find all encodings of Polish signs. File investigate.py documents this effort. After successfull investigation, I've prepared switch_coding.py which allows to quickly change between Democracy 3 format to Windows-1250 for Polish diactrics. With that, I was able to fix all those errors. Fixed files were merged back to master branch. Python files remains in investigate_diactrics branch for future use.
