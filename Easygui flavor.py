import easygui
flavor = easygui.choicebox('Whatis is your favorite flavor.', choices = ['Chocolate', 'Vanilla', 'Strawberry'])
easygui.msgbox('You picked ' + flavor)
