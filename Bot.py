import time
import pyautogui
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading

class FallGuysBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fall Guys Bot - by jordan123pal")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Variables
        self.running = False
        self.bot_instance = None
        self.bot_thread = None
        self.exp = 0
        self.money = 0
        
        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Fall Guys Bot", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Author
        author_label = ttk.Label(main_frame, text="by jordan123pal", font=("Arial", 10))
        author_label.pack(pady=5)
        
        # Mode selection frame
        mode_frame = ttk.LabelFrame(main_frame, text="Select Mode")
        mode_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Mode buttons
        stable_btn = ttk.Button(mode_frame, text="Stable Mode (1080p and 720p)", 
                               command=self.start_stable_mode)
        stable_btn.pack(fill=tk.X, padx=5, pady=5)
        
        beta_btn = ttk.Button(mode_frame, text="Beta Mode (Other Resolutions)", 
                             command=self.start_beta_mode)
        beta_btn.pack(fill=tk.X, padx=5, pady=5)
        
        event_btn = ttk.Button(mode_frame, text="Event Mode (1080p and 720p)", 
                              command=self.start_event_mode)
        event_btn.pack(fill=tk.X, padx=5, pady=5)
        
        # Control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.start_btn = ttk.Button(control_frame, text="Start", command=self.start_bot, state=tk.DISABLED)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = ttk.Button(control_frame, text="Stop", command=self.stop_bot, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        # Stats frame
        stats_frame = ttk.LabelFrame(main_frame, text="Statistics")
        stats_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Stats display
        exp_frame = ttk.Frame(stats_frame)
        exp_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(exp_frame, text="Experience:").pack(side=tk.LEFT)
        self.exp_var = tk.StringVar(value="0")
        ttk.Label(exp_frame, textvariable=self.exp_var).pack(side=tk.LEFT, padx=5)
        
        money_frame = ttk.Frame(stats_frame)
        money_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(money_frame, text="Money:").pack(side=tk.LEFT)
        self.money_var = tk.StringVar(value="0")
        ttk.Label(money_frame, textvariable=self.money_var).pack(side=tk.LEFT, padx=5)
        
        # Log display
        log_frame = ttk.LabelFrame(main_frame, text="Bot Log")
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.log_text.config(state=tk.DISABLED)
    
    def log(self, message):
        """Add message to log display"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        
    def update_stats(self, exp, money):
        """Update displayed stats"""
        self.exp = exp
        self.money = money
        self.exp_var.set(str(exp))
        self.money_var.set(str(money))
        
    def start_stable_mode(self):
        """Set up stable mode"""
        self.log("Starting Stable Mode (1080p and 720p)...")
        self.mode = 1
        self.start_btn.config(state=tk.NORMAL)
    
    def start_beta_mode(self):
        """Set up beta mode"""
        self.log("Starting Beta Mode (Other Resolutions)...")
        self.mode = 2
        self.start_btn.config(state=tk.NORMAL)
    
    def start_event_mode(self):
        """Set up event mode"""
        self.log("Starting Event Mode (1080p and 720p)...")
        self.mode = 3
        self.start_btn.config(state=tk.NORMAL)
        
    def start_bot(self):
        """Start the bot in a separate thread"""
        if self.bot_thread and self.bot_thread.is_alive():
            return
            
        self.running = True
        self.stop_btn.config(state=tk.NORMAL)
        self.start_btn.config(state=tk.DISABLED)
        
        # Start the bot in a separate thread
        self.bot_thread = threading.Thread(target=self.run_bot)
        self.bot_thread.daemon = True
        self.bot_thread.start()
        
    def stop_bot(self):
        """Stop the bot"""
        self.running = False
        self.log("Stopping bot...")
        self.stop_btn.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)
    
    def run_bot(self):
        """Run the bot according to selected mode"""
        try:
            if self.mode == 1:
                self.log("Starting Stable Mode...")
                check = checkresolution()
                if check is not None:
                    self.bot_instance = check
                    self.log("Resolution detected. Starting bot...")
                    self.bot_instance.lobby()
                else:
                    self.log("No valid resolution detected.")

            elif self.mode == 2:
                self.log("Starting Beta Mode...")
                self.log("Minimize console please...")
                time.sleep(3)
                self.bot_instance = a
                a.lobby()

            elif self.mode == 3:
                self.log("Starting Event Mode...")
                self.log("Minimize console please...")
                check1 = checkresolutionEvent()
                time.sleep(3)
                if check1 is not None:
                    self.bot_instance = check1
                    self.log("Resolution detected. Starting bot...")
                    self.bot_instance.lobby()
                else:
                    self.log("No valid resolution detected.")
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.stop_bot()
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading

class bot:
    def __init__(self, resolution="1080", gui=None):
        self.resolution = resolution
        self.gui = gui

        # path

        self.lobby_path = ".\\{}\\lobby.png".format(self.resolution)
        self.ingame_path = ".\\{}\\ingame.png".format(self.resolution)
        self.exit_path = ".\\{}\\exit.png".format(self.resolution)
        self.ok_path = ".\\{}\\ok.png".format(self.resolution)
        self.confirm_path = ".\\{}\\confirm.png".format(self.resolution)
        self.lvlup_path = ".\\{}\\lvlup.png".format(self.resolution)

        # Path error

        self.error_path = ".\\{}\\error.png".format(self.resolution)
        self.error1_path = ".\\{}\\error1.png".format(self.resolution)
        self.error2_path = ".\\{}\\error2.png".format(self.resolution)
        self.error3_path = ".\\{}\\error3.png".format(self.resolution)
        self.error4_path = ".\\{}\\error4.png".format(self.resolution)
        self.error5_path = ".\\{}\\error5.png".format(self.resolution)
        self.error6_path = ".\\{}\\error6.png".format(self.resolution)
        self.error7_path = ".\\{}\\error7.png".format(self.resolution)
        self.error8_path = ".\\{}\\error8.png".format(self.resolution)

        # Save exp

        self.exp = 0
        self.money = 0
        
    def log(self, message):
        """Log a message to GUI or console"""
        print(message)
        if self.gui:
            self.gui.log(message)
            
    def update_stats(self):
        """Update statistics in GUI"""
        if self.gui:
            self.gui.update_stats(self.exp, self.money)

    def lobby(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            self.error()
            self.log("Waiting lobby...")
            time.sleep(2)
            lobby = pyautogui.locateOnScreen(self.lobby_path, confidence=0.8)
            if lobby is not None:
                self.log("Lobby detected ")
                pyautogui.click(lobby)
                pyautogui.press("space")
                self.ingame()
                break

    def ingame(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            self.error()
            ingame = pyautogui.locateOnScreen(self.ingame_path, confidence=0.8)
            if ingame is not None:
                self.log("Ingame detected")
                self.exit()
                break

    def exit(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            self.error()
            salir = pyautogui.locateOnScreen(self.exit_path, confidence=0.8)
            if salir is not None:
                self.log("exit detected")
                pyautogui.press("esc")
                self.ok()
                break

    def ok(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            self.error()
            ok2 = pyautogui.locateOnScreen(self.ok_path, confidence=0.8)
            if ok2 is not None:
                time.sleep(1)
                pyautogui.press("space")
                self.results()
                break

    def results(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            self.error()
            result = pyautogui.locateOnScreen(self.confirm_path, confidence=0.8)
            lvlup = pyautogui.locateOnScreen(self.lvlup_path, confidence=0.8)
            if result is not None:
                pyautogui.click(result)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                self.log(f"You have won {self.money} money")
                self.log(f"You have won {self.exp} exp")
                self.update_stats()
                time.sleep(5)
                pyautogui.press("space")
                self.ingame()

            if lvlup is not None:
                self.log("lvl Up Detected")
                pyautogui.press("space")
                time.sleep(3)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                self.log(f"You have won {self.money} money")
                self.log(f"You have won {self.exp} exp")
                self.update_stats()
                time.sleep(5)
                pyautogui.press("space")
                pyautogui.press("space")
                self.ingame()

    def error(self):
        error = pyautogui.locateOnScreen(self.error_path, confidence=0.8)
        error1 = pyautogui.locateOnScreen(self.error1_path, confidence=0.8)
        error2 = pyautogui.locateOnScreen(self.error2_path, confidence=0.8)
        error3 = pyautogui.locateOnScreen(self.error3_path, confidence=0.8)
        error4 = pyautogui.locateOnScreen(self.error4_path, confidence=0.8)
        error5 = pyautogui.locateOnScreen(self.error5_path, confidence=0.8)
        error6 = pyautogui.locateOnScreen(self.error6_path, confidence=0.8)
        error7 = pyautogui.locateOnScreen(self.error7_path, confidence=0.8)
        error8 = pyautogui.locateOnScreen(self.error8_path, confidence=0.8)
        if error is not None or error1 is not None or error2 is not None or error3 is not None or \
                error4 is not None or error5 is not None or error6 is not None or \
                error7 is not None or error8 is not None:
            self.log("error")
            pyautogui.press("space")
            time.sleep(1)
            pyautogui.click()
            self.lobby()


class bot1:
    def __init__(self, gui=None):
        self.money = 0
        self.exp = 0
        self.gui = gui
        
    def log(self, message):
        """Log a message to GUI or console"""
        print(message)
        if self.gui:
            self.gui.log(message)
            
    def update_stats(self):
        """Update statistics in GUI"""
        if self.gui:
            self.gui.update_stats(self.exp, self.money)

    def lobby(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            self.log("-----> Waiting lobby")
            lobby = pyautogui.locateOnScreen("1080/lobby.png")
            lobby1 = pyautogui.locateOnScreen("720/lobby.png")
            lobby2 = pyautogui.locateOnScreen("1080/lobby.png", confidence=0.6)
            lobby3 = pyautogui.locateOnScreen("720/lobby.png", confidence=0.6)
            if lobby is not None or lobby1 is not None or lobby2 is not None or lobby3 is not None:
                self.log("Lobby detected")
                if lobby is not None:
                    pyautogui.click(lobby)
                if lobby1 is not None:
                    pyautogui.click(lobby1)
                if lobby2 is not None:
                    pyautogui.click(lobby2)
                if lobby3 is not None:
                    pyautogui.click(lobby3)

                pyautogui.press("space")
                self.ingame()

    def ingame(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            ingame = pyautogui.locateOnScreen("1080/ingame.png")
            ingame1 = pyautogui.locateOnScreen("720/ingame.png")
            ingame2 = pyautogui.locateOnScreen("1080/ingame.png", confidence=0.6)
            ingame3 = pyautogui.locateOnScreen("720/ingame.png", confidence=0.6)
            if ingame is not None or ingame1 is not None or ingame2 is not None or ingame3 is not None:
                self.log("Ingame detected")
                self.exit()

    def exit(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            exits = pyautogui.locateOnScreen("1080/exit.png")
            exits1 = pyautogui.locateOnScreen("720/exit.png")
            exits2 = pyautogui.locateOnScreen("1080/exit.png", confidence=0.6)
            exits3 = pyautogui.locateOnScreen("720/exit.png", confidence=0.6)
            if exits is not None or exits1 is not None or exits2 is not None or exits3 is not None:
                self.log("exit detected")
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("space")
                pyautogui.press("space")
                self.result()

    def result(self):
        while True:
            if self.gui and not self.gui.running:
                break
                
            results = pyautogui.locateOnScreen("1080/confirm.png")
            results1 = pyautogui.locateOnScreen("720/confirm.png")
            results2 = pyautogui.locateOnScreen("1080/confirm.png", confidence=0.6)
            results3 = pyautogui.locateOnScreen("720/confirm.png", confidence=0.6)
            if results is not None or results1 is not None or results2 is not None or results3 is not None:
                self.log("Results Detected")
                time.sleep(2)
                self.money += 30
                self.exp += 15
                self.log(f"You have won {self.money} money")
                self.log(f"You have won {self.exp} exp")
                self.update_stats()
                time.sleep(5)
                pyautogui.press("space")
                pyautogui.press("space")
                self.ingame()

            lvlup = pyautogui.locateOnScreen("1080/lvlup.png")
            lvlup1 = pyautogui.locateOnScreen("720/lvlup.png")
            lvlup2 = pyautogui.locateOnScreen("1080/lvlup.png", confidence=0.6)
            lvlup3 = pyautogui.locateOnScreen("720/lvlup.png", confidence=0.6)
            if lvlup is not None or lvlup1 is not None or lvlup2 is not None or lvlup3 is not None:
                pyautogui.press("space")
                time.sleep(5)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                self.log(f"You have won {self.money} money")
                self.log(f"You have won {self.exp} exp")
                self.update_stats()
                time.sleep(5)
                pyautogui.press("space")
                pyautogui.press("space")
                self.ingame()


def checkresolution(gui=None):
    for i in range(0, 9):
        fullhd = pyautogui.locateOnScreen("1080/lobby.png", confidence=0.8)
        if fullhd is not None:
            if gui:
                gui.log("Full HD detected")
            else:
                print("Full HD detected")
            return bot(gui=gui)

        hd = pyautogui.locateOnScreen("720/lobby.png", confidence=0.8)
        if hd is not None:
            if gui:
                gui.log("HD detected")
            else:
                print("HD detected")
            return bot(resolution="720", gui=gui)


def checkresolutionEvent(gui=None):
    fullhdEvent = pyautogui.locateOnScreen("1080/Event/lobby.png", confidence=0.8)
    if fullhdEvent is not None:
        if gui:
            gui.log("Full HD detected")
        else:
            print("Full HD detected")
        return bot(resolution="1080/Event", gui=gui)

    hdEvent = pyautogui.locateOnScreen("720/Event/lobby.png", confidence=0.8)
    if hdEvent is not None:
        if gui:
            gui.log("HD detected")
        else:
            print("HD detected")
        return bot(resolution="720/Event", gui=gui)


def menu():
    """Display either console menu or GUI based on parameter"""
    # Create the tkinter GUI
    root = tk.Tk()
    app = FallGuysBotGUI(root)
    
    # Make sure the bot instance has a reference to the GUI
    global a
    a = bot1(gui=app)
    
    # Start the tkinter main loop
    root.mainloop()


a = bot1()

if __name__ == "__main__":
    menu()

