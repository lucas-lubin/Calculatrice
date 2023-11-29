def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Erreur : Division par zéro.")

def evaluer_expression(expression):

    i = 1
    while i < len(expression):
        if expression[i] == '*':
            expression[i-1] = multiplication(expression[i-1], expression[i+1])
            expression.pop(i)
            expression.pop(i)
        elif expression[i] == '/':
            expression[i-1] = division(expression[i-1], expression[i+1])
            expression.pop(i)
            expression.pop(i)
        else:
            i += 2

    result = expression[0]
    for i in range(1, len(expression), 2):
        if expression[i] == '+':
            result = addition(result, expression[i+1])
        elif expression[i] == '-':
            result = soustraction(result, expression[i+1])

    return result

def calculatrice():
    while True:
        try:
            expression = input("Entrez une expression mathématique (ou 'exit' pour quitter) : ")

            if expression.lower() == 'exit':
                print("Au revoir !")
                break

            elements = []
            nombre_actuel = ''

            for char in expression:
                if char.isdigit() or char == '.':
                    nombre_actuel += char
                else:
                    if nombre_actuel:
                        elements.append(float(nombre_actuel))
                        nombre_actuel = ''
                    if char in ['+', '-', '*', '/']:
                        elements.append(char)

            if nombre_actuel:
                elements.append(float(nombre_actuel))

            resultat = evaluer_expression(elements)

            print(f"Le résultat de l'expression est égal à {resultat}")

        except ValueError as e:
            print(f"Erreur : {e}")
        except IndexError:
            print("Erreur : Format d'expression incorrect.")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

calculatrice()