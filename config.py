import re


TOKEN = '5482858677:AAHv1WAKe-wCYA--Fkrn3fZtAf1slCKiRoA'
Numbers = {1: ['а', 'и', 'с', 'ъ'], 2: ['б', 'й', 'т', 'ы'], 3: ['в', 'к', 'у', 'ь'], 4: ['г', 'л', 'ф', 'е'], 5: ['д', 'м', 'х', 'ю'],
    6: ['е', 'н', 'ц', 'я'], 7: ['ё', 'о', 'ч'], 8: ['ж','п','ш'], 9: ['з','р','щ']}




def transform_text(text: str):
    text = text.lower()
    arr = list(text)

    def repl_to_num(c: str):
        res = 0

        for key in Numbers:
            #print(Numbers)
            #print(key)
            for item in Numbers[key]:
                #print(Numbers[key])
                if(item == c):
                    res = key
        
        return res

    result = list(map(repl_to_num,arr))

    def check_number(n):
        if n > 9:
            value = list(str(n))
            result = [int(item) for item in value]
            return check_number(sum(result))
        else:
            return n

    return check_number(sum(result))


#print(check_number(3))

#result = list(map(repl_to_num,arr))
#print(repl_to_num(result))

#print(main('ваауы'))
#print(check_number(sum(result)))