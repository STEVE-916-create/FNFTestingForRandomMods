print("[LOG]: Running Mod...")
import arcade
import time
import datetime
import ctypes
import random
import math
import pyglet
import json
import os

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )


class FNFHaxe(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.lPressed = False
        self.dPressed = False
        self.uPressed = False
        self.rPressed = False
        arcade.set_background_color(arcade.color.BLACK)
        self.foreground = arcade.SpriteList()
        self.background = arcade.SpriteList()
        self.HUD = arcade.SpriteList()
        self.sky = arcade.SpriteList()
        self.NotesHUD = arcade.SpriteList()
        self.NotesHUDPl = arcade.SpriteList()
        self.Notes = arcade.SpriteList()
        self.Particles = arcade.SpriteList()
        self.center_window()
        self.middleOfScreen = self.get_location()

    def setup(self):
        pass

    def on_draw(self):

        arcade.start_render()
        arcade.set_viewport(
            (0 + (random.randint(-10, 10)/10)),
            (1000 + (random.randint(-10, 10)/10)),
            (0 + (random.randint(-10, 10)/10)),
            (500 + (random.randint(-10, 10)/10))
        )
        self.sky.draw()
        self.foreground.draw()
        self.background.draw()
        self.NotesHUD.draw()
        self.NotesHUDPl.draw()
        self.Notes.draw()
        self.HUD.draw()
        self.Particles.draw()
        arcade.draw_text(self.timeHoursRealTime + ":" + self.timeMintsRealTime + ":" + self.timeSecosRealTime, arcade.get_viewport()[0] + 10, arcade.get_viewport()[2] + 480, font_size=8)
        arcade.draw_text("Health: " + str(gameValues["playGame"]["health"]), arcade.get_viewport()[0] + 10, arcade.get_viewport()[2] + 460, font_size=8)
        arcade.draw_text("Misses: " + str(gameValues["playGame"]["misses"]), arcade.get_viewport()[0] + 10, arcade.get_viewport()[2] + 440, font_size=8)
        arcade.finish_render()
        pass

    def update(self, delta_time):
        self.timeHoursRealTime = str(datetime.datetime.now().time())[0:2]
        self.timeMintsRealTime = str(datetime.datetime.now().time())[3:5]
        self.timeSecosRealTime = str(datetime.datetime.now().time())[6:8]
        if gameValues["sinWave"] == False:
            gameValues["tickGame"] = gameValues["tickGame"] + 0.05
        else:
            gameValues["tickGame"] = gameValues["tickGame"] - 0.05

        if gameValues["tickGame"] > 1:
            gameValues["sinWave"] = True
        if gameValues["tickGame"] < -1:
            gameValues["sinWave"] = False

        if gameValues["menuScene"] == 5:
            if gameValues["isPlaying"] == False:
                self.loadSongFromFile("bopcat", "normal")

            gameValues["isPlaying"] = True
        
        if gameValues["isShaking"] == True:
            if gameValues["Shaking"] == True:
                self.set_location(self.get_location()[0] + random.randint(-10, 10), self.get_location()[1] + random.randint(-10, 10))
                gameValues["Shaking"] = False
            elif gameValues["Shaking"] == False:
                gameValues["Shaking"] = True
                self.center_window()
        else:
            if gameValues["Shaking"] == False:
                gameValues["Shaking"] = True
                self.center_window()
            else:
                gameValues["Shaking"] = False

        if gameValues["isPlaying"] == True and gameValues["isPaused"] == False:
            if gameValues["playGame"]["health"] < 0.1:
                arcade.close_window()
            gameValues["beatTicks"] = math.ceil(self.Music_playGame.time*994.6) + (660*(self.fileDataFNF["song"]["speed"] - ((self.fileDataFNF["song"]["speed"]-1)/0.8)))
            for noteMoverInNotes in self.Notes:
                noteMoverInNotes.center_y = noteMoverInNotes.center_y + (16.5*(self.fileDataFNF["song"]["speed"]))
                if arcade.check_for_collision_with_list(noteMoverInNotes, self.NotesHUD):
                    for nothingtoputherejusttrashvalues in range(20):
                        self.newNote = arcade.Sprite("assets/images/basic.png")
                        self.newNote.velocity = (random.randint(-20, 20), random.randint(-20, 20))
                        self.newNote.scale = 0.25
                        self.newNote.color = noteMoverInNotes.color
                        self.newNote.center_x = noteMoverInNotes.center_x
                        self.newNote.center_y = noteMoverInNotes.center_y
                        self.Particles.append(self.newNote)
                    noteMoverInNotes.kill()
                    self.Voices_playGame.volume = 1
                if arcade.check_for_collision_with_list(noteMoverInNotes, self.NotesHUDPl):
                    if noteMoverInNotes.center_x == 500 and self.lPressed == True:
                        noteMoverInNotes.kill()
                        self.Voices_playGame.volume = 1
                        for nothingtoputherejusttrashvalues in range(20):
                            self.newNote = arcade.Sprite("assets/images/basic.png")
                            self.newNote.velocity = (random.randint(-20, 20), random.randint(-20, 20))
                            self.newNote.scale = 0.25
                            self.newNote.color = noteMoverInNotes.color
                            self.newNote.center_x = noteMoverInNotes.center_x
                            self.newNote.center_y = noteMoverInNotes.center_y
                            self.Particles.append(self.newNote)
                        gameValues["playGame"]["health"] += 2.5
                    if noteMoverInNotes.center_x == 600 and self.dPressed == True:
                        noteMoverInNotes.kill()
                        self.Voices_playGame.volume = 1
                        for nothingtoputherejusttrashvalues in range(20):
                            self.newNote = arcade.Sprite("assets/images/basic.png")
                            self.newNote.velocity = (random.randint(-20, 20), random.randint(-20, 20))
                            self.newNote.scale = 0.25
                            self.newNote.color = noteMoverInNotes.color
                            self.newNote.center_x = noteMoverInNotes.center_x
                            self.newNote.center_y = noteMoverInNotes.center_y
                            self.Particles.append(self.newNote)
                        gameValues["playGame"]["health"] += 2.5
                    if noteMoverInNotes.center_x == 700 and self.uPressed == True:
                        noteMoverInNotes.kill()
                        self.Voices_playGame.volume = 1
                        for nothingtoputherejusttrashvalues in range(20):
                            self.newNote = arcade.Sprite("assets/images/basic.png")
                            self.newNote.velocity = (random.randint(-20, 20), random.randint(-20, 20))
                            self.newNote.scale = 0.25
                            self.newNote.color = noteMoverInNotes.color
                            self.newNote.center_x = noteMoverInNotes.center_x
                            self.newNote.center_y = noteMoverInNotes.center_y
                            self.Particles.append(self.newNote)
                        gameValues["playGame"]["health"] += 2.5
                    if noteMoverInNotes.center_x == 800 and self.rPressed == True:
                        noteMoverInNotes.kill()
                        self.Voices_playGame.volume = 1
                        for nothingtoputherejusttrashvalues in range(20):
                            self.newNote = arcade.Sprite("assets/images/basic.png")
                            self.newNote.velocity = (random.randint(-20, 20), random.randint(-20, 20))
                            self.newNote.scale = 0.25
                            self.newNote.color = noteMoverInNotes.color
                            self.newNote.center_x = noteMoverInNotes.center_x
                            self.newNote.center_y = noteMoverInNotes.center_y
                            self.Particles.append(self.newNote)
                        gameValues["playGame"]["health"] += 2.5
                if noteMoverInNotes.center_y > 550:
                    noteMoverInNotes.kill()
                    self.Voices_playGame.volume = 0
                    gameValues["playGame"]["health"] -= 5
                    gameValues["playGame"]["misses"] += 1
            for sectionCheckerThingy in self.noteDataInFNF:
                isAMostHitSectionFNFData = sectionCheckerThingy["mustHitSection"]
                for noteCheckerThingy in sectionCheckerThingy["sectionNotes"]:
                    if noteCheckerThingy[0] < gameValues["beatTicks"]:
                        self.newNote = arcade.Sprite("assets/images/basic.png")
                        if isAMostHitSectionFNFData == False:
                            self.newNote.center_x = (noteCheckerThingy[1] * 100) + 100
                        else:
                            if noteCheckerThingy[1] > 3:
                                self.newNote.center_x = ((noteCheckerThingy[1] - 4) * 100) + 100
                            else:
                                self.newNote.center_x = ((noteCheckerThingy[1] + 4) * 100) + 100
                        self.newNote.center_y = -30
                        self.newNote.scale = 2
                        if noteCheckerThingy[1] == 0:
                            self.newNote.color = arcade.color.PURPLE
                        if noteCheckerThingy[1] == 1:
                            self.newNote.color = arcade.color.CYAN
                        if noteCheckerThingy[1] == 2:
                            self.newNote.color = arcade.color.GREEN
                        if noteCheckerThingy[1] == 3:
                            self.newNote.color = arcade.color.RED
                        if noteCheckerThingy[1] == 4:
                            self.newNote.color = arcade.color.PURPLE
                        if noteCheckerThingy[1] == 5:
                            self.newNote.color = arcade.color.CYAN
                        if noteCheckerThingy[1] == 6:
                            self.newNote.color = arcade.color.GREEN
                        if noteCheckerThingy[1] == 7:
                            self.newNote.color = arcade.color.RED
                        self.Notes.append(self.newNote)
                        for noteDurationToHoldDataFNF in range(int((noteCheckerThingy[2]/30)*(1*self.fileDataFNF["song"]["speed"]))):
                            self.newNote = arcade.Sprite("assets/images/basic.png")
                            if isAMostHitSectionFNFData == False:
                                self.newNote.center_x = (noteCheckerThingy[1] * 100) + 100
                            else:
                                if noteCheckerThingy[1] > 3:
                                    self.newNote.center_x = ((noteCheckerThingy[1] - 4) * 100) + 100
                                else:
                                    self.newNote.center_x = ((noteCheckerThingy[1] + 4) * 100) + 100
                            self.newNote.center_y = noteDurationToHoldDataFNF * -60
                            self.newNote.scale = 0.75
                            if noteCheckerThingy[1] == 0:
                                self.newNote.color = arcade.color.PURPLE
                            if noteCheckerThingy[1] == 1:
                                self.newNote.color = arcade.color.CYAN
                            if noteCheckerThingy[1] == 2:
                                self.newNote.color = arcade.color.GREEN
                            if noteCheckerThingy[1] == 3:
                                self.newNote.color = arcade.color.RED
                            if noteCheckerThingy[1] == 4:
                                self.newNote.color = arcade.color.PURPLE
                            if noteCheckerThingy[1] == 5:
                                self.newNote.color = arcade.color.CYAN
                            if noteCheckerThingy[1] == 6:
                                self.newNote.color = arcade.color.GREEN
                            if noteCheckerThingy[1] == 7:
                                self.newNote.color = arcade.color.RED
                            self.Notes.append(self.newNote)
                        noteCheckerThingy[0] = 9999999999e+99
        for particleCheckerThing in self.Particles:
            if particleCheckerThing.center_x < -20 or particleCheckerThing.center_x > -1020 or particleCheckerThing.center_y < -20 or particleCheckerThing.center_y > 520:
                particleCheckerThing.kill()
        self.Particles.update()
        pass
    
    def on_key_press(self, key, keyMod):
        if gameValues["menuScene"] > 0:
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.lPressed = True
            if key == arcade.key.RIGHT or key == arcade.key.D:
                self.rPressed = True
            if key == arcade.key.UP or key == arcade.key.W:
                self.uPressed = True
                if gameValues["isInputUsed"] == True:
                    gameValues["menuSel"] = gameValues["menuSel"] - 1
                    self.sound_scrollMenu.play()
            if key == arcade.key.DOWN or key == arcade.key.S:
                self.dPressed = True
                if gameValues["isInputUsed"] == True:
                    gameValues["menuSel"] = gameValues["menuSel"] + 1
                    self.sound_scrollMenu.play()
            if key == arcade.key.ENTER:
                if gameValues["isEnterUsed"] == True:
                    self.enterPressed = True
            if key == arcade.key.BACKSPACE:
                if gameValues["isEnterUsed"] == True:
                    self.backPressed = True
        if key == arcade.key.F1:
            gameValues["isShaking"] = not gameValues["isShaking"]
        if key == arcade.key.F2:
            self.flixelSound = arcade.load_sound("assets/sound/flixel.ogg")
            self.flixelSound.play()
        if key == arcade.key.F3:
            self.Voices_playGame.pause()
            self.Music_playGame.pause()
        if key == arcade.key.F4:
            self.Voices_playGame.seek(0)
            self.Music_playGame.seek(0)
            self.noteDataInFNF = self.fileDataFNF["song"]["notes"]
        print(self.lPressed, self.dPressed, self.uPressed, self.rPressed)
        pass

    def on_key_release(self, key, keyMod):
        if gameValues["menuScene"] > 0:
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.lPressed = False
            if key == arcade.key.RIGHT or key == arcade.key.D:
                self.rPressed = False
            if key == arcade.key.UP or key == arcade.key.W:
                self.uPressed = False
            if key == arcade.key.DOWN or key == arcade.key.S:
                self.dPressed = False
        if key == arcade.key.F3:
            self.Voices_playGame.play()
            self.Music_playGame.play()
        print(self.lPressed, self.dPressed, self.uPressed, self.rPressed)
        pass
    def randomiseMusic(self):
        if random.randint(0, 2) == 1:
            self.music_menuMenu1.set_volume(1, self.playerMusic1)
            self.music_menuMenu2.set_volume(0, self.playerMusic2)
            self.music_menuMenu3.set_volume(0, self.playerMusic3)
        elif random.randint(0, 2) == 1:
            self.music_menuMenu1.set_volume(0, self.playerMusic1)
            self.music_menuMenu2.set_volume(0, self.playerMusic2)
            self.music_menuMenu3.set_volume(1, self.playerMusic3)
        else:
            self.music_menuMenu1.set_volume(0, self.playerMusic1)
            self.music_menuMenu2.set_volume(1, self.playerMusic2)
            self.music_menuMenu3.set_volume(0, self.playerMusic3)
        pass
    def loadSongFromFile(self, songNameFromFile, songModeFromFile):
        fileToOpen = open("assets/data/" + songNameFromFile + "/" + songModeFromFile + ".json")
        if fileToOpen != OSError:
            self.fileDataFNF = json.loads(fileToOpen.read())

            self.noteDataInFNF = self.fileDataFNF["song"]["notes"]
        
            
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 100
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUD.append(self.newNote)
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 200
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUD.append(self.newNote)
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 300
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUD.append(self.newNote)
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 400
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUD.append(self.newNote)
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 500
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUDPl.append(self.newNote)
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 600
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUDPl.append(self.newNote)
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 700
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUDPl.append(self.newNote)
            self.newNote = arcade.Sprite("assets/images/basic.png")
            self.newNote.center_x = 800
            self.newNote.center_y = 370
            self.newNote.scale = 2
            self.NotesHUDPl.append(self.newNote)
            self.Music_playGameData = arcade.load_sound("assets/songs/" + songNameFromFile + "/Inst.ogg")
            self.Voices_playGameData = arcade.load_sound("assets/songs/" + songNameFromFile + "/Voices.ogg")
            self.Music_playGame = self.Music_playGameData.play()
            self.Voices_playGame = self.Voices_playGameData.play()
        pass

gameValues = {
    "isShaking": False,
    "Shaking": False,
    "isPlaying": False,
    "isPaused": False,
    "isInputUsed": False,
    "isEnterUsed": False,
    "isBackUsed": False,
    "playGame": {
        "score": 0,
        "misses": 0,
        "health": 50,
    },
    "menuScene": 5,
    "menuVar": 0,
    "menuSel": 0,
    "startDuration": 0,
    "beatTicks": 800,
    "tickGame": 0,
    "sinWave": False,
    "flippy": False,
}

gamePort = FNFHaxe(1000, 500, "Friday Night Funkin'")
gamePort.setup()
arcade.set_background_color(arcade.color.BLACK)
arcade.run()
exit()