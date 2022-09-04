import itertools
import random
import pickle

class SakClass:
    lets = {'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
        'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
        'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
        'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
        'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]}

    def __init__(self):
        self.sak = []

    def randomizeSak(self):
        for key in SakClass.lets:
            for i in range(SakClass.lets[key][0]):
                self.sak.append(key)
        random.shuffle(self.sak)
        # self.sak = ['Α','Β','Α','Ζ','Θ','Η','Τ','Ι','Ι','Ο','Ω','Μ','Ν','Ω','Α','Ι','Ω','Ε','Ε','Σ']
    
    '''0<=n'''
    def getLetters(self, n):
        letters = []
        i = 0
        while len(self.sak) > 0 and i < n:
            letter = random.choice(self.sak)
            self.sak.remove(letter)
            letters.append(letter)
            i += 1
        return letters
    
    '''κεφαλαία μόνο'''
    def putBackLetters(self, letters):
        for i in range(len(letters)):
            self.sak.insert(random.randrange(0, len(self.sak)), letters[i])
    
    '''κεφαλαία μονο'''
    def lettersInSak(self):
        return len(self.sak)
    
    def updateLetters(self, letters, word):
        if word == 'p':
            self.putBackLetters(letters)
            letters = []
            new_letters = self.getLetters(7)
            for letter in new_letters:
                letters.append(letter)
        else: 
            for letter in word:
                letters.remove(letter)
            new_letters = self.getLetters(len(word))
            for letter in new_letters:
                letters.append(letter)
        return letters

class Logic:
    lets = {'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
        'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
        'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
        'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
        'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]}
    
    words = []
    with open ('greek7.txt','r',encoding='utf-8') as f:
        words = f.read().splitlines()
    
    words_values = {}
    for word in words:
        value = 0
        for letter in word:
            value += lets[letter][1]
        words_values.setdefault(word, value)

    def letterValues(letters):
        letter_values = []
        for letter in letters:
            letter_values.append(Logic.lets.get(letter)[1])
        return letter_values

    def wordValue(word):
        if word == 'p' or word == 'q':
            return 0
        else:
            return Logic.wordValueDict(word)
    
    def wordValueDict(word):
        return Logic.words_values.get(word)

    def lettersInWord(letters, word):
        letters_duplicate = letters.copy()
        for letter in word:
            if letter in letters_duplicate:
                letters_duplicate.remove(letter)
            else:
                return False
        return True

    def wordInDict(word):
        if word in Logic.words:
            return True
        return False
    
class Player:
    def __init__(self, name = " "):
        self.name = name
    
    def __repr__(self) -> str:
        return "Παίκτης: " + self.name

    def display(self, score, letters, letter_count):
        InputOutput.stars()
        InputOutput.playerStats(self.name, score)
        InputOutput.lettersRemaining(letter_count)
        letter_values = Logic.letterValues(letters)
        InputOutput.lettersAndValues(letters, letter_values)

class Human(Player):
    def __init__(self, name=" ", score = 0, wins = 0):
        super().__init__(name)
        self.score = score
        self.wins = wins
    
    def __repr__(self) -> str:
        return super().__repr__() + ", Συνολικό σκορ: " + str(self.score) + ", Νίκες: " + str(self.wins)

    def play(self, letters):
        word = InputOutput.inputWord()
        invalid = True
        while word != 'p' and word != 'q' and invalid:
            if not(Logic.lettersInWord(letters, word)):
                InputOutput.wrongLetters()
                word = InputOutput.inputWord()
            elif not(Logic.wordInDict(word)):
                InputOutput.wrongWord()
                word = InputOutput.inputWord()
            else:
                invalid = False
        return word

class Computer(Player):
    def __init__(self, name="PC", mode="MAX"):
        super().__init__(name)
        self.mode = mode
    
    def play(self, letters):
        if self.mode == "MIN":
            for i in range(2, len(letters) + 1):
                words = itertools.permutations(letters, i)
                for word in words:
                    wordstr = ''.join(list(word))
                    if Logic.wordInDict(wordstr):
                        return wordstr
        elif self.mode == "MAX": 
            for i in range(len(letters), 1, -1):
                words = itertools.permutations(letters, i)
                for word in words:
                    wordstr = ''.join(list(word))
                    if Logic.wordInDict(wordstr):
                        return wordstr
        else:
            total_words = []
            valid_words = False
            for i in range(2, len(letters) + 1):
                words = itertools.permutations(letters, i)
                for word in words:
                    wordstr = ''.join(list(word))
                    if Logic.wordInDict(wordstr):
                        valid_words = True
                        total_words.append(wordstr)
            if valid_words:
                maxv = 0
                maxind = 0
                for i in range(len(total_words)):
                    if Logic.wordValueDict(total_words[i]) > maxv:
                        maxv = Logic.wordValueDict(total_words[i])
                        maxind = i
                return total_words[maxind]
        return 'p'

class GameStats():
    def __init__(self, player_name, player_score, pc_score, total_moves, match_result) -> None:
        self.player_name = player_name
        self.player_score = player_score
        self.pc_score = pc_score
        self.total_moves = total_moves
        self.match_result = match_result

    def __repr__(self) -> str:
        return ("Σκορ παίκτη: " + str(self.player_score) 
        + ", Σκορ υπολογιστή: " + str(self.pc_score) + ", Συνολικές κινήσεις: " + str(self.total_moves) + 
        ", Αποτέλεσμα: " + self.match_result)

class Game:
    def __init__(self) -> None:
        self.ph = Human()
        self.pc = Computer()
        self.sak = SakClass()
        self.players = []
        self.stats = []
    
    def __repr__(self) -> str:
        return 'game instance'
    
    def setup(self):
        self.players = InputOutput.loadFromFile("names.pkl")
        self.stats = InputOutput.loadFromFile("stats.pkl")
        
        InputOutput.giveName()
        name = InputOutput.inputAns()
        playerExists = False
        for player in self.players:
            if name == player.name:
                playerExists = True
                self.ph = player
        if not playerExists:
            self.players.append(Human(name))
            for player in self.players:
                if name == player.name:
                    self.ph = player

    def run(self):
        self.setup()
        
        InputOutput.menu()
        ans = InputOutput.inputAns()
        while ans != 'q':
            
            if ans == '1':
                print("\n" + repr(self.ph))
                game_count = 0
                InputOutput.gamesTitle()
                for s in self.stats:
                    if s.player_name == self.ph.name:
                        game_count += 1
                        InputOutput.statEntry(game_count, s, False, True)
                if game_count == 0: 
                    InputOutput.noGamesYet()

            elif ans == '2':
                InputOutput.settings()
                choice = InputOutput.inputAns()
                while not(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5'):
                    InputOutput.wrongMenuInput()
                    choice = InputOutput.inputAns()
                if choice == '1':
                    self.pc.mode = "MIN"
                    InputOutput.algorithm(self.pc.mode)
                elif choice == '2':
                    self.pc.mode = "MAX"
                    InputOutput.algorithm(self.pc.mode)
                elif choice == '3':
                    self.pc.mode = "SMART"
                    InputOutput.algorithm(self.pc.mode)
                elif choice == '4':
                    if len(self.players) != 0:
                        InputOutput.playersTitle()
                        for p in self.players:
                            print(repr(p))
                    else:
                        InputOutput.noEntries()
                else:
                    if len(self.stats) != 0:
                        index = 0
                        InputOutput.statsTitle()
                        for s in self.stats:
                            index += 1
                            InputOutput.statEntry(index, s, True, False)
                    else:
                        InputOutput.noEntries()
            
            elif ans == '3':
                self.sak.randomizeSak()
                letters_human = self.sak.getLetters(7)
                score_human = 0
                letters_pc = self.sak.getLetters(7)
                score_pc = 0
                word_points = 0
                total_moves = 0 
                game_ended = False
                while len(letters_human) == 7 and len(letters_pc) == 7 and not game_ended:
                    self.ph.display(score_human, letters_human, self.sak.lettersInSak())
                    word = self.ph.play(letters_human)
                    word_points = Logic.wordValue(word)
                    InputOutput.wordFeedback(word, word_points, False, True)
                    if word != 'q':
                        total_moves += 2
                        score_human += word_points
                        InputOutput.newScore(score_human)
                        letters_human = self.sak.updateLetters(letters_human, word)

                        self.pc.display(score_pc, letters_pc, self.sak.lettersInSak())
                        word = self.pc.play(letters_pc)
                        word_points = Logic.wordValue(word)
                        InputOutput.wordFeedback(word, word_points, True, False)
                        score_pc += word_points
                        InputOutput.newScore(score_pc)
                        letters_pc = self.sak.updateLetters(letters_pc, word)
                    else:
                        game_ended = True
                        
                self.ph.score += score_human
                match_result = "Ισοπαλία"
                if score_pc > score_human:
                    InputOutput.winnerLoser(self.pc.name, self.ph.name, score_pc, score_human)
                    match_result = "Νίκη PC"
                elif score_pc < score_human:
                    self.ph.wins += 1
                    InputOutput.winnerLoser(self.ph.name, self.pc.name, score_human, score_pc)
                    match_result = "Νίκη " + self.ph.name
                else:
                    InputOutput.draw()
                self.stats.append(GameStats(self.ph.name, score_human, score_pc, total_moves, match_result))
            else:
                InputOutput.wrongMenuInput()
            InputOutput.menu()
            ans = InputOutput.inputAns()
        InputOutput.exited()
        
        self.end()
      
    def end(self):
        InputOutput.saveOnFile("names.pkl", self.players)
        InputOutput.saveOnFile("stats.pkl", self.stats)

'''Κλάση με όλες τις μεθόδους με τιμές που εκτυπώνονται στο χρήστη'''
class InputOutput:
    def menu():
        print("\n*****SCRABBLE*****\n---------------\n1: Σκορ\n2: Ρυθμίσεις\n3: Παιχνίδι\nq: Έξοδος\n---------------")
    
    def stars():
        print("\n***********************************************************")
    
    def lettersRemaining(letter_count):
        print("Γράμματα μέσα στο σακουλάκι: ",letter_count)
    
    def wrongLetters():
        print("Η λέξη που δόθηκε περιλαμβάνει γράμματα εκτός των διαθέσιμων.")
    
    def wrongWord():
        print("Η λέξη που δόθηκε δεν θεωρείται έγκυρη.")
    
    def wrongMenuInput():
        print("Λάθος είσοδος!")
    
    def wordFeedback(word, word_points, showWord, showWordAccepted):
        if showWord:
            print("Λέξη που δόθηκε: ", word)
        if word == 'p':
            print("Πήγες πάσο!")
        elif word == 'q':
            print("Έξοδος παιχνιδιού")
        else:
            if showWordAccepted:
                print("Αποδεκτή λέξη!")
            print("Πόντοι λέξης: ", word_points)

    def lettersAndValues(letters, letter_values):
        print("Διαθέσιμα γράμματα: ",end="")
        for i in range(len(letters) - 1):
            print(letters[i],letter_values[i],sep=",",end=" - ")
        print(letters[i + 1],letter_values[i + 1],sep=",")

    def settings():
        print("\nΓια MIN mode πληκτρολόγησε 1")
        print("Για MAX mode πληκτρολόγησε 2")
        print("Για SMART mode πληκτρολόγησε 3")
        print("Για εμφάνιση στατιστικών όλων των παικτών πληκτρολόγησε 4")
        print("Για εμφάνιση στατιστικών όλων των παιχνιδιών πληκτρολόγησε 5")
    
    def exited():
        print("Βγήκες από το παιχνίδι.")
    
    def giveName():
        print("Δώσε όνομα")
    
    def winnerLoser(winner, loser, scorew, scorel):
        print("\nΟ παίκτης", winner, "νίκησε τον παίκτη", loser, "με διαφορά σκορ: ", scorew, " - ", scorel)
    
    def gamesTitle():
        print("-------Παιχνίδια-------")

    def noGamesYet():
        print("Δεν έχει παιχτεί κανένα παιχνίδι ακόμη!")

    def draw():
        print("\nΙσοπαλία!")
    
    def playerStats(name, score):
        print("*** Παίκτης:", name, " *** Σκορ:", score)
    
    def newScore(score):
        print("Νέο σκορ: ", score)
    
    def algorithm(mode):
        print("\nΟ αλγόριθμος που θα χρησιμοποιήσει ο υπολογιστής είναι ο: ", mode)

    def statEntry(index, s, showName, showIndex):
        if showName:
            print("Παίκτης " + s.player_name, end=", ")
        if showIndex:
            print(str(index) + ". ", end="")
        print(repr(s))

    def statsTitle():
        print("\n------ΣΤΑΤΙΣΤΙΚΑ ΠΑΙΧΝΙΔΙΩΝ------")

    def playersTitle():
        print("\n------ΠΑΙΚΤΕΣ------")

    def noEntries():
        print("\nΔεν υπάρχει καμία καταχώρηση!")

    def inputWord():
        return input("Λέξη (δώσε 'p' για πάσο, 'q' για έξοδο): ")
    
    def inputAns():
        return input("Απάντηση: ")
    
    def loadFromFile(filename):
        data = []
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
        except FileNotFoundError:
            print("Δημιουργία αρχείου " + filename)
            with open(filename, "wb") as f:
                pickle.dump(data, f)
        except:
            print("Γενικό σφάλμα κατά το άνοιγμα του αρχείου" + filename    )
        return data

    def saveOnFile(filename, data):
        try:
            with open(filename,'wb') as f:
                pickle.dump(data, f)  
        except FileNotFoundError as err:
            print("Σφάλμα κατά το άνοιγμα του αρχείου " + filename)
            print(err)
        except:
            print("Γενικό σφάλμα κατά το άνοιγμα του αρχείου " + filename)
            print
        