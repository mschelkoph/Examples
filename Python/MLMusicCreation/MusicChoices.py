from mingus.containers import Bar, Track, Note
import mingus.core.value as value
from mingus.midi import midi_file_out



def CreateNoteAction(t, choice):
####### Quarter Notes ##########
    if choice == 0:
        c = Note()
        t.add_notes(c.from_int(48), 4)
    elif choice == 1:
        c = Note()
        t.add_notes(c.from_int(49), 4)
    elif choice == 2:
        c = Note()
        t.add_notes(c.from_int(50), 4)
    elif choice == 3:
        c = Note()
        t.add_notes(c.from_int(51), 4)
    elif choice == 4:
        c = Note()
        t.add_notes(c.from_int(52), 4)
    elif choice == 5:
        c = Note()
        t.add_notes(c.from_int(53), 4)
    elif choice == 6:
        c = Note()
        t.add_notes(c.from_int(54), 4)
    elif choice == 7:
        c = Note()
        t.add_notes(c.from_int(55), 4)
    elif choice == 8:
        c = Note()
        t.add_notes(c.from_int(56), 4)
    elif choice == 9:
        c = Note()
        t.add_notes(c.from_int(57), 4)
    elif choice == 10:
        c = Note()
        t.add_notes(c.from_int(58), 4)
    elif choice == 11:
        c = Note()
        t.add_notes(c.from_int(59), 4)
    elif choice == 12:
        c = Note()
        t.add_notes(c.from_int(60), 4)
    elif choice == 13:
        c = Note()
        t.add_notes(c.from_int(61), 4)
    elif choice == 14:
        c = Note()
        t.add_notes(c.from_int(62), 4)
    elif choice == 15:
        c = Note()
        t.add_notes(c.from_int(63), 4)
    elif choice == 16:
        c = Note()
        t.add_notes(c.from_int(64), 4)
    elif choice == 17:
        c = Note()
        t.add_notes(c.from_int(65), 4)
    elif choice == 18:
        c = Note()
        t.add_notes(c.from_int(66), 4)
    elif choice == 19:
        c = Note()
        t.add_notes(c.from_int(67), 4)
    elif choice == 20:
        c = Note()
        t.add_notes(c.from_int(68), 4)
    elif choice == 21:
        c = Note()
        t.add_notes(c.from_int(69), 4)
    elif choice == 22:
        c = Note()
        t.add_notes(c.from_int(70), 4)
    elif choice == 23:
        c = Note()
        t.add_notes(c.from_int(71), 4)
    elif choice == 24:
        c = Note()
        t.add_notes(c.from_int(72), 4)

######### Half Notes ###################
    elif choice == 25:
        c = Note()
        t.add_notes(c.from_int(48), 2)
    elif choice == 26:
        c = Note()
        t.add_notes(c.from_int(49), 2)
    elif choice == 27:
        c = Note()
        t.add_notes(c.from_int(50), 2)
    elif choice == 28:
        c = Note()
        t.add_notes(c.from_int(51), 2)
    elif choice == 29:
        c = Note()
        t.add_notes(c.from_int(52), 2)
    elif choice == 30:
        c = Note()
        t.add_notes(c.from_int(53), 2)
    elif choice == 31:
        c = Note()
        t.add_notes(c.from_int(54), 2)
    elif choice == 32:
        c = Note()
        t.add_notes(c.from_int(55), 2)
    elif choice == 33:
        c = Note()
        t.add_notes(c.from_int(56), 2)
    elif choice == 34:
        c = Note()
        t.add_notes(c.from_int(57), 2)
    elif choice == 35:
        c = Note()
        t.add_notes(c.from_int(58), 2)
    elif choice == 36:
        c = Note()
        t.add_notes(c.from_int(59), 2)
    elif choice == 37:
        c = Note()
        t.add_notes(c.from_int(60), 2)
    elif choice == 38:
        c = Note()
        t.add_notes(c.from_int(61), 2)
    elif choice == 39:
        c = Note()
        t.add_notes(c.from_int(62), 2)
    elif choice == 40:
        c = Note()
        t.add_notes(c.from_int(63), 2)
    elif choice == 41:
        c = Note()
        t.add_notes(c.from_int(64), 2)
    elif choice == 42:
        c = Note()
        t.add_notes(c.from_int(65), 2)
    elif choice == 43:
        c = Note()
        t.add_notes(c.from_int(66), 2)
    elif choice == 44:
        c = Note()
        t.add_notes(c.from_int(67), 2)
    elif choice == 45:
        c = Note()
        t.add_notes(c.from_int(68), 2)
    elif choice == 46:
        c = Note()
        t.add_notes(c.from_int(69), 2)
    elif choice == 47:
        c = Note()
        t.add_notes(c.from_int(70), 2)
    elif choice == 48:
        c = Note()
        t.add_notes(c.from_int(71), 2)
    elif choice == 49:
        c = Note()
        t.add_notes(c.from_int(72), 2)

########### Whole Notes ##############
    elif choice == 50:
        c = Note()
        t.add_notes(c.from_int(48), 1)
    elif choice == 51:
        c = Note()
        t.add_notes(c.from_int(49), 1)
    elif choice == 52:
        c = Note()
        t.add_notes(c.from_int(50), 1)
    elif choice == 53:
        c = Note()
        t.add_notes(c.from_int(51), 1)
    elif choice == 54:
        c = Note()
        t.add_notes(c.from_int(52), 1)
    elif choice == 55:
        c = Note()
        t.add_notes(c.from_int(53), 1)
    elif choice == 56:
        c = Note()
        t.add_notes(c.from_int(54), 1)
    elif choice == 57:
        c = Note()
        t.add_notes(c.from_int(55), 1)
    elif choice == 58:
        c = Note()
        t.add_notes(c.from_int(56), 1)
    elif choice == 59:
        c = Note()
        t.add_notes(c.from_int(57), 1)
    elif choice == 60:
        c = Note()
        t.add_notes(c.from_int(58), 1)
    elif choice == 61:
        c = Note()
        t.add_notes(c.from_int(59), 1)
    elif choice == 62:
        c = Note()
        t.add_notes(c.from_int(60), 1)
    elif choice == 63:
        c = Note()
        t.add_notes(c.from_int(61), 1)
    elif choice == 64:
        c = Note()
        t.add_notes(c.from_int(62), 1)
    elif choice == 65:
        c = Note()
        t.add_notes(c.from_int(63), 1)
    elif choice == 66:
        c = Note()
        t.add_notes(c.from_int(64), 1)
    elif choice == 67:
        c = Note()
        t.add_notes(c.from_int(65), 1)
    elif choice == 68:
        c = Note()
        t.add_notes(c.from_int(66), 1)
    elif choice == 69:
        c = Note()
        t.add_notes(c.from_int(67), 1)
    elif choice == 70:
        c = Note()
        t.add_notes(c.from_int(68), 1)
    elif choice == 71:
        c = Note()
        t.add_notes(c.from_int(69), 1)
    elif choice == 72:
        c = Note()
        t.add_notes(c.from_int(70), 1)
    elif choice == 73:
        c = Note()
        t.add_notes(c.from_int(71), 1)
    elif choice == 74:
        c = Note()
        t.add_notes(c.from_int(72), 1)

######### Eighth Notes ###############
    elif choice == 75:
        c = Note()
        t.add_notes(c.from_int(48), 8)
    elif choice == 76:
        c = Note()
        t.add_notes(c.from_int(49), 8)
    elif choice == 77:
        c = Note()
        t.add_notes(c.from_int(50), 8)
    elif choice == 78:
        c = Note()
        t.add_notes(c.from_int(51), 8)
    elif choice == 79:
        c = Note()
        t.add_notes(c.from_int(52), 8)
    elif choice == 80:
        c = Note()
        t.add_notes(c.from_int(53), 8)
    elif choice == 81:
        c = Note()
        t.add_notes(c.from_int(54), 8)
    elif choice == 82:
        c = Note()
        t.add_notes(c.from_int(55), 8)
    elif choice == 83:
        c = Note()
        t.add_notes(c.from_int(56), 8)
    elif choice == 84:
        c = Note()
        t.add_notes(c.from_int(57), 8)
    elif choice == 85:
        c = Note()
        t.add_notes(c.from_int(58), 8)
    elif choice == 86:
        c = Note()
        t.add_notes(c.from_int(59), 8)
    elif choice == 87:
        c = Note()
        t.add_notes(c.from_int(60), 8)
    elif choice == 88:
        c = Note()
        t.add_notes(c.from_int(61), 8)
    elif choice == 89:
        c = Note()
        t.add_notes(c.from_int(62), 8)
    elif choice == 90:
        c = Note()
        t.add_notes(c.from_int(63), 8)
    elif choice == 91:
        c = Note()
        t.add_notes(c.from_int(64), 8)
    elif choice == 92:
        c = Note()
        t.add_notes(c.from_int(65), 8)
    elif choice == 93:
        c = Note()
        t.add_notes(c.from_int(66), 8)
    elif choice == 94:
        c = Note()
        t.add_notes(c.from_int(67), 8)
    elif choice == 95:
        c = Note()
        t.add_notes(c.from_int(68), 8)
    elif choice == 96:
        c = Note()
        t.add_notes(c.from_int(69), 8)
    elif choice == 97:
        c = Note()
        t.add_notes(c.from_int(70), 8)
    elif choice == 98:
        c = Note()
        t.add_notes(c.from_int(71), 8)
    elif choice == 99:
        c = Note()
        t.add_notes(c.from_int(72), 8)

######## Sixteenth Notes ###########
    if choice == 100:
        c = Note()
        t.add_notes(c.from_int(48), 4)
    elif choice == 101:
        c = Note()
        t.add_notes(c.from_int(49), 4)
    elif choice == 102:
        c = Note()
        t.add_notes(c.from_int(50), 4)
    elif choice == 103:
        c = Note()
        t.add_notes(c.from_int(51), 4)
    elif choice == 104:
        c = Note()
        t.add_notes(c.from_int(52), 4)
    elif choice == 105:
        c = Note()
        t.add_notes(c.from_int(53), 4)
    elif choice == 106:
        c = Note()
        t.add_notes(c.from_int(54), 4)
    elif choice == 107:
        c = Note()
        t.add_notes(c.from_int(55), 4)
    elif choice == 108:
        c = Note()
        t.add_notes(c.from_int(56), 4)
    elif choice == 109:
        c = Note()
        t.add_notes(c.from_int(57), 4)
    elif choice == 110:
        c = Note()
        t.add_notes(c.from_int(58), 4)
    elif choice == 111:
        c = Note()
        t.add_notes(c.from_int(59), 4)
    elif choice == 112:
        c = Note()
        t.add_notes(c.from_int(60), 4)
    elif choice == 113:
        c = Note()
        t.add_notes(c.from_int(61), 4)
    elif choice == 114:
        c = Note()
        t.add_notes(c.from_int(62), 4)
    elif choice == 115:
        c = Note()
        t.add_notes(c.from_int(63), 4)
    elif choice == 116:
        c = Note()
        t.add_notes(c.from_int(64), 4)
    elif choice == 117:
        c = Note()
        t.add_notes(c.from_int(65), 4)
    elif choice == 118:
        c = Note()
        t.add_notes(c.from_int(66), 4)
    elif choice == 119:
        c = Note()
        t.add_notes(c.from_int(67), 4)
    elif choice == 120:
        c = Note()
        t.add_notes(c.from_int(68), 4)
    elif choice == 121:
        c = Note()
        t.add_notes(c.from_int(69), 4)
    elif choice == 122:
        c = Note()
        t.add_notes(c.from_int(70), 4)
    elif choice == 123:
        c = Note()
        t.add_notes(c.from_int(71), 4)
    elif choice == 125:
        c = Note()
        t.add_notes(c.from_int(72), 4)
    
    if choice <= 24:
        return .5
    elif choice > 24 and choice <= 49:
        return 1
    elif choice > 49 and choice <= 74:
        return 2
    elif choice > 74 and choice <= 99:
        return .25
    elif choice > 99 and choice <= 125:
        return .125
